# -*- coding: utf-8 -*-
"""
HỆ THỐNG QUẢN LÝ LỚP HỌC, TÀI KHOẢN HỌC SINH VÀ SỔ ĐIỂM ĐIỆN TỬ
Tác giả: Thầy giáo Đinh Văn Thành - Hotline / Zalo: 0915.213717
Đơn vị: Trường THCS Đồng Yên
Hỗ trợ:
- Tạo lớp học trực tuyến
- Nhập danh sách học sinh từ Excel/Word và tự động sinh tài khoản + mật khẩu
- Đăng nhập học sinh cá nhân hoá
- Thống kê tỷ lệ nộp bài, phổ điểm, sổ điểm điện tử theo chuẩn Bộ GD&ĐT
- Xuất danh sách tài khoản và bảng điểm ra Excel
"""

import os
import json
import uuid
import re
from datetime import datetime
import tempfile
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

BASE_WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if os.environ.get("VERCEL") or not os.access(BASE_WORKSPACE, os.W_OK):
    DATA_DIR = os.path.join(tempfile.gettempdir(), "global_learning_data")
else:
    DATA_DIR = os.path.join(BASE_WORKSPACE, "data")

CLASSES_FILE = os.path.join(DATA_DIR, "classes.json")
STUDENTS_FILE = os.path.join(DATA_DIR, "students.json")

try:
    os.makedirs(DATA_DIR, exist_ok=True)
except Exception:
    pass

# Helper đọc ghi file
def _read_json(filepath, default):
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return default
    return default

def _write_json(filepath, data):
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Warning: could not write json {filepath}: {e}")

def _remove_vietnamese_accents(text: str) -> str:
    """Chuyển tiếng Việt có dấu thành không dấu để tạo username đẹp"""
    s1 = "àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ"
    s2 = "a"*17 + "e"*11 + "i"*5 + "o"*17 + "u"*11 + "y"*5 + "d"
    s1_upper = s1.upper()
    s2_upper = s2.upper()
    
    trans_table = str.maketrans(s1 + s1_upper, s2 + s2_upper)
    return text.translate(trans_table)

# =========================================================================
# 1. QUẢN LÝ LỚP HỌC (CLASS MANAGEMENT)
# =========================================================================
def get_all_classes():
    classes = _read_json(CLASSES_FILE, None)
    if classes is None:
        # Tạo sẵn các lớp mẫu
        classes = {
            "6A": {"id": "CLASS_6A", "name": "Lớp 6A", "grade": "6", "school_year": "2026 - 2027", "teacher": "Thầy Đinh Văn Thành"},
            "6B": {"id": "CLASS_6B", "name": "Lớp 6B", "grade": "6", "school_year": "2026 - 2027", "teacher": "Thầy Đinh Văn Thành"},
            "7A": {"id": "CLASS_7A", "name": "Lớp 7A", "grade": "7", "school_year": "2026 - 2027", "teacher": "Thầy Đinh Văn Thành"},
            "8A": {"id": "CLASS_8A", "name": "Lớp 8A", "grade": "8", "school_year": "2026 - 2027", "teacher": "Thầy Đinh Văn Thành"},
            "9A": {"id": "CLASS_9A", "name": "Lớp 9A", "grade": "9", "school_year": "2026 - 2027", "teacher": "Thầy Đinh Văn Thành"}
        }
        _write_json(CLASSES_FILE, classes)
    return list(classes.values())

def create_class(class_name: str, grade: str, school_year: str = "2026 - 2027", teacher: str = "Thầy Đinh Văn Thành"):
    classes = _read_json(CLASSES_FILE, {})
    clean_name = class_name.strip()
    class_id = f"CLASS_{clean_name.upper().replace(' ', '_')}"
    
    classes[clean_name] = {
        "id": class_id,
        "name": f"Lớp {clean_name}" if not clean_name.lower().startswith("lớp") else clean_name,
        "grade": str(grade),
        "school_year": school_year,
        "teacher": teacher
    }
    _write_json(CLASSES_FILE, classes)
    return classes[clean_name]

# =========================================================================
# 2. TẠO TÀI KHOẢN HỌC SINH THEO DANH SÁCH ĐƯA LÊN (BULK IMPORT)
# =========================================================================
def import_students_from_text(raw_text: str, class_name: str, default_password: str = "123456"):
    """
    Xử lý danh sách học sinh từ văn bản (Word, Excel copy sang):
    Hỗ trợ các định dạng:
    1. STT \t Họ và tên \t Lớp
    2. STT, Họ và tên
    3. Mỗi dòng 1 học sinh
    """
    students_db = _read_json(STUDENTS_FILE, {})
    lines = raw_text.strip().split("\n")
    
    created_students = []
    idx_counter = len([s for s in students_db.values() if s.get("class_name") == class_name]) + 1

    clean_class = class_name.replace("Lớp", "").strip().upper()

    for line in lines:
        line_str = line.strip()
        if not line_str:
            continue
            
        # Tách dòng bằng tab hoặc phẩy hoặc gạch đứng
        parts = re.split(r"[\t|,]", line_str)
        parts = [p.strip() for p in parts if p.strip()]
        
        if not parts:
            continue

        # Lấy tên học sinh
        student_name = ""
        if len(parts) == 1:
            # Chỉ có tên hoặc "1. Nguyễn Văn An"
            match = re.match(r"^(\d+)[\.\s\-]+(.*)$", parts[0])
            if match:
                student_name = match.group(2).strip()
            else:
                student_name = parts[0]
        elif len(parts) >= 2:
            # Nếu cột đầu là số thứ tự
            if parts[0].isdigit():
                student_name = parts[1]
            else:
                student_name = parts[0]

        if not student_name:
            continue

        # Sinh mã học sinh & Tên đăng nhập
        student_id = f"HS_{clean_class}_{idx_counter:02d}"
        
        # Tạo username không dấu: ví dụ 6a_an.nguyen hoặc hs6a01
        name_no_accents = _remove_vietnamese_accents(student_name).lower()
        words = name_no_accents.split()
        if words:
            short_tag = words[-1] + "".join([w[0] for w in words[:-1]])
            username = f"{clean_class.lower()}_{short_tag}"
        else:
            username = f"{clean_class.lower()}_hs{idx_counter:02d}"

        # Kiểm tra trùng username
        existing_usernames = {s.get("username") for s in students_db.values()}
        final_username = username
        bump = 1
        while final_username in existing_usernames:
            final_username = f"{username}{bump}"
            bump += 1

        student_record = {
            "id": student_id,
            "student_id": student_id,
            "full_name": student_name,
            "class_name": class_name,
            "username": final_username,
            "password": default_password,
            "role": "student",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "active"
        }

        students_db[student_id] = student_record
        created_students.append(student_record)
        idx_counter += 1

    _write_json(STUDENTS_FILE, students_db)
    return created_students

def get_students_by_class(class_name: str):
    students_db = _read_json(STUDENTS_FILE, None)
    if students_db is None:
        # Tự động khởi tạo học sinh mẫu cho Lớp 6A
        sample_list = (
            "1\tNguyễn Văn An\t6A\n"
            "2\tTrần Thị Bình\t6A\n"
            "3\tLê Hoàng Cường\t6A\n"
            "4\tPhạm Thu Dung\t6A\n"
            "5\tHoàng Minh Đức\t6A"
        )
        import_students_from_text(sample_list, "6A")
        students_db = _read_json(STUDENTS_FILE, {})
    result = [s for s in students_db.values() if s.get("class_name") == class_name]
    result.sort(key=lambda x: x.get("student_id", ""))
    return result

def authenticate_student(username: str, password: str):
    """Xác thực đăng nhập học sinh"""
    students_db = _read_json(STUDENTS_FILE, {})
    u_clean = username.strip().lower()
    p_clean = password.strip()

    for s in students_db.values():
        if s.get("username", "").lower() == u_clean and s.get("password") == p_clean:
            s_copy = dict(s)
            s_copy.pop("password", None)
            return s_copy
    return None

# =========================================================================
# 3. XUẤT DANH SÁCH TÀI KHOẢN HỌC SINH RA EXCEL (.XLSX)
# =========================================================================
def export_student_accounts_to_excel(class_name: str, output_path: str = None) -> str:
    students = get_students_by_class(class_name)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = f"Tài Khoản {class_name}"

    font_title = Font(name="Times New Roman", size=14, bold=True, color="1E3A8A")
    font_sub = Font(name="Times New Roman", size=11, italic=True)
    font_th = Font(name="Times New Roman", size=11, bold=True, color="FFFFFF")
    font_data = Font(name="Times New Roman", size=11)
    font_user = Font(name="Times New Roman", size=11, bold=True, color="2563EB")
    font_pass = Font(name="Times New Roman", size=11, bold=True, color="DC2626")

    fill_header = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
    fill_alt = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")

    align_center = Alignment(horizontal="center", vertical="center")
    align_left = Alignment(horizontal="left", vertical="center")

    thin_border = Side(border_style="thin", color="CBD5E1")
    border_cell = Border(left=thin_border, right=thin_border, top=thin_border, bottom=thin_border)

    ws.merge_cells("A1:F1")
    ws["A1"] = "TRƯỜNG THCS ĐỒNG YÊN - CỔNG HỌC TIẾNG ANH TRỰC TUYẾN"
    ws["A1"].font = font_sub
    ws["A1"].alignment = align_center

    ws.merge_cells("A2:F2")
    ws["A2"] = f"DANH SÁCH CẤP TÀI KHOẢN & MẬT KHẨU HỌC SINH: {class_name.upper()}"
    ws["A2"].font = font_title
    ws["A2"].alignment = align_center

    ws.merge_cells("A3:F3")
    ws["A3"] = f"Giáo viên chủ nhiệm/phụ trách: Thầy Đinh Văn Thành (0915.213717) - Ngày cấp: {datetime.now().strftime('%d/%m/%Y')}"
    ws["A3"].font = font_sub
    ws["A3"].alignment = align_center

    headers = ["STT", "Mã Học Sinh", "Họ và Tên Học Sinh", "Lớp", "Tên Đăng Nhập", "Mật Khẩu Ban Đầu"]
    row_num = 5
    for c_idx, h in enumerate(headers, 1):
        cell = ws.cell(row=row_num, column=c_idx, value=h)
        cell.font = font_th
        cell.fill = fill_header
        cell.alignment = align_center
        cell.border = border_cell

    for idx, s in enumerate(students, 1):
        row_num += 1
        r_fill = fill_alt if idx % 2 == 0 else PatternFill(fill_type=None)

        c1 = ws.cell(row=row_num, column=1, value=idx)
        c2 = ws.cell(row=row_num, column=2, value=s.get("student_id", ""))
        c3 = ws.cell(row=row_num, column=3, value=s.get("full_name", ""))
        c4 = ws.cell(row=row_num, column=4, value=s.get("class_name", ""))
        c5 = ws.cell(row=row_num, column=5, value=s.get("username", ""))
        c6 = ws.cell(row=row_num, column=6, value=s.get("password", "123456"))

        c1.alignment = align_center
        c2.alignment = align_center
        c3.alignment = align_left
        c4.alignment = align_center
        c5.alignment = align_center
        c6.alignment = align_center

        for cell in [c1, c2, c3, c4, c5, c6]:
            cell.font = font_data
            cell.border = border_cell
            if r_fill.fill_type:
                cell.fill = r_fill

        c5.font = font_user
        c6.font = font_pass

    col_widths = {1: 8, 2: 16, 3: 28, 4: 12, 5: 22, 6: 20}
    for col_idx, width in col_widths.items():
        ws.column_dimensions[openpyxl.utils.get_column_letter(col_idx)].width = width

    if not output_path:
        out_dir = os.path.join(DATA_DIR, "Tai_Khoan_Hoc_Sinh_Xuat_Ra")
        os.makedirs(out_dir, exist_ok=True)
        safe_class = "".join([c if c.isalnum() else "_" for c in class_name])
        output_path = os.path.join(out_dir, f"Tai_Khoan_{safe_class}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx")

    wb.save(output_path)
    return output_path

# =========================================================================
# 4. SỔ ĐIỂM ĐIỆN TỬ VÀ THỐNG KÊ LỚP HỌC (PROFESSIONAL CLASS GRADEBOOK)
# =========================================================================
def get_class_gradebook_analytics(class_name: str):
    """Thống kê chi tiết điểm số, tỷ lệ nộp bài, xếp loại của cả lớp"""
    from .submission_store import _load_submissions
    from .exam_store import list_all_exams

    students = get_students_by_class(class_name)
    all_subs = _load_submissions()
    exams = list_all_exams()

    # Thu thập kết quả theo học sinh
    gradebook_rows = []
    class_scores = []
    total_assigned = len(exams)

    for idx, s in enumerate(students, 1):
        s_name = s.get("full_name", "").strip().lower()
        s_class = s.get("class_name", "").strip().lower()

        student_submissions = []
        for eid, sub_list in all_subs.items():
            for sub in sub_list:
                # Đối chiếu tên và lớp
                if sub.get("student_name", "").strip().lower() == s_name:
                    student_submissions.append(sub)

        scores = [sub.get("score", 0.0) for sub in student_submissions]
        avg_score = round(sum(scores) / len(scores), 1) if scores else 0.0
        if scores:
            class_scores.append(avg_score)

        # Xếp loại học lực
        if avg_score >= 9.0:
            rank = "Xuất Sắc 🏆"
        elif avg_score >= 8.0:
            rank = "Giỏi 🌟"
        elif avg_score >= 6.5:
            rank = "Khá 👍"
        elif avg_score >= 5.0:
            rank = "Đạt / Trung Bình 📚"
        else:
            rank = "Chưa Đạt / Cần Cố Gắng 💪" if scores else "Chưa Làm Bài"

        gradebook_rows.append({
            "stt": idx,
            "student_id": s.get("student_id", ""),
            "full_name": s.get("full_name", ""),
            "class_name": s.get("class_name", ""),
            "username": s.get("username", ""),
            "completed_exams_count": len(student_submissions),
            "total_assigned_count": total_assigned,
            "average_score": avg_score,
            "rank": rank,
            "recent_scores": scores[-4:] if scores else [],
            "status": "Đã nộp bài" if student_submissions else "Chưa nộp bài"
        })

    # Thống kê tổng hợp lớp
    total_students = len(students)
    submitted_students = len([r for r in gradebook_rows if r["completed_exams_count"] > 0])
    unsubmitted_students = [r["full_name"] for r in gradebook_rows if r["completed_exams_count"] == 0]
    
    submission_rate = round((submitted_students / total_students) * 100, 1) if total_students > 0 else 0.0
    class_avg = round(sum(class_scores) / len(class_scores), 1) if class_scores else 0.0
    class_max = max(class_scores) if class_scores else 0.0
    class_min = min(class_scores) if class_scores else 0.0

    excellent_count = len([s for s in class_scores if s >= 8.0])
    good_count = len([s for s in class_scores if 6.5 <= s < 8.0])
    avg_count = len([s for s in class_scores if 5.0 <= s < 6.5])
    low_count = len([s for s in class_scores if s < 5.0])

    # Mẫu tin nhắn Zalo nhắc nhở học sinh chưa nộp bài
    zalo_reminder = ""
    if unsubmitted_students:
        names_str = "\n- ".join(unsubmitted_students)
        zalo_reminder = (
            f"📢 [THÔNG BÁO TỪ THẦY ĐINH VĂN THÀNH - LỚP {class_name}]\n"
            f"Kính gửi Quý phụ huynh và các em học sinh lớp {class_name}.\n"
            f"Hiện tại hệ thống kiểm tra Tiếng Anh trực tuyến ghi nhận các em sau đây CHƯA NỘP BÀI:\n"
            f"- {names_str}\n"
            f"👉 Các em hãy đăng nhập vào hệ thống để hoàn thành bài tập đúng hạn nhé!"
        )

    return {
        "class_name": class_name,
        "total_students": total_students,
        "submitted_students": submitted_students,
        "unsubmitted_count": len(unsubmitted_students),
        "submission_rate_percent": submission_rate,
        "class_average_score": class_avg,
        "class_max_score": class_max,
        "class_min_score": class_min,
        "distribution": {
            "excellent": excellent_count,
            "good": good_count,
            "average": avg_count,
            "needs_improvement": low_count
        },
        "gradebook": gradebook_rows,
        "zalo_reminder_message": zalo_reminder
    }
