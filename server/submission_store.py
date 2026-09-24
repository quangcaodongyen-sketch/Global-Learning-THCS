# -*- coding: utf-8 -*-
"""
QUẢN LÝ BÀI NỘP, CHẤM ĐIỂM TỰ ĐỘNG VÀ XUẤT BẢNG ĐIỂM EXCEL (SUBMISSION STORE)
Tác giả: Thầy giáo Đinh Văn Thành - Hotline / Zalo: 0915.213717
Đơn vị: Trường THCS Đồng Yên
"""

import os
import json
import uuid
from datetime import datetime
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from .exam_store import get_exam_by_id

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
SUBMISSIONS_FILE = os.path.join(DATA_DIR, "submissions.json")

os.makedirs(DATA_DIR, exist_ok=True)

def _load_submissions():
    if os.path.exists(SUBMISSIONS_FILE):
        try:
            with open(SUBMISSIONS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def _save_submissions(data):
    with open(SUBMISSIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def grade_submission(exam_id: str, student_info: dict, student_answers: dict) -> dict:
    """Chấm điểm bài làm của học sinh theo từng loại câu hỏi"""
    exam = get_exam_by_id(exam_id, for_student=False)
    if not exam:
        raise ValueError(f"Không tìm thấy bài thi với mã {exam_id}")

    questions = exam.get("questions", [])
    total_evaluable_items = 0
    correct_items = 0
    details = []

    for q in questions:
        q_id = q.get("id")
        q_type = q.get("type")
        item_detail = {
            "question_id": q_id,
            "type": q_type,
            "instruction": q.get("instruction", ""),
            "question_text": q.get("question", q.get("passage", "")),
            "explanation": q.get("explanation", "")
        }

        # 1. Trắc nghiệm / Phát âm / Odd-one-out / Listening
        if q_type in ["multiple_choice", "phonetics", "odd_one_out", "listening"]:
            total_evaluable_items += 1
            correct_ans = str(q.get("answer", "")).strip()
            user_ans = str(student_answers.get(q_id, "")).strip()
            is_correct = (user_ans.lower() == correct_ans.lower())
            if is_correct:
                correct_items += 1
            item_detail.update({
                "student_answer": user_ans,
                "correct_answer": correct_ans,
                "is_correct": is_correct
            })

        # 2. Cloze test
        elif q_type == "cloze":
            sub_results = []
            for sub in q.get("questions", []):
                total_evaluable_items += 1
                sub_num = str(sub.get("number"))
                sub_key = f"{q_id}_{sub_num}"
                correct_ans = str(sub.get("answer", "")).strip()
                user_ans = str(student_answers.get(sub_key, "")).strip()
                is_correct = (user_ans.lower() == correct_ans.lower())
                if is_correct:
                    correct_items += 1
                sub_results.append({
                    "number": sub_num,
                    "student_answer": user_ans,
                    "correct_answer": correct_ans,
                    "is_correct": is_correct,
                    "explanation": sub.get("explanation", "")
                })
            item_detail["sub_results"] = sub_results

        # 3. Matching
        elif q_type == "matching":
            sub_results = []
            for idx, pair in enumerate(q.get("pairs", [])):
                total_evaluable_items += 1
                pair_key = f"{q_id}_{idx}"
                correct_right = str(pair.get("right", "")).strip()
                user_right = str(student_answers.get(pair_key, "")).strip()
                is_correct = (user_right.lower() == correct_right.lower())
                if is_correct:
                    correct_items += 1
                sub_results.append({
                    "left": pair.get("left"),
                    "student_answer": user_right,
                    "correct_answer": correct_right,
                    "is_correct": is_correct
                })
            item_detail["sub_results"] = sub_results

        # 4. Sentence Unscramble
        elif q_type == "sentence_unscramble":
            total_evaluable_items += 1
            correct_sent = str(q.get("correct_sentence", "")).strip().rstrip(".")
            user_sent = str(student_answers.get(q_id, "")).strip().rstrip(".")
            is_correct = (user_sent.lower() == correct_sent.lower())
            if is_correct:
                correct_items += 1
            item_detail.update({
                "student_answer": user_sent,
                "correct_answer": q.get("correct_sentence"),
                "is_correct": is_correct
            })

        # 5. Sentence Transformation
        elif q_type == "transformation":
            total_evaluable_items += 1
            correct_trans = str(q.get("correct_answer", "")).strip().rstrip(".")
            user_trans = str(student_answers.get(q_id, "")).strip().rstrip(".")
            is_correct = (user_trans.lower() == correct_trans.lower())
            if is_correct:
                correct_items += 1
            item_detail.update({
                "student_answer": user_trans,
                "correct_answer": q.get("correct_answer"),
                "is_correct": is_correct
            })

        # 6. Reading comprehension
        elif q_type == "reading":
            sub_results = []
            for sub in q.get("questions", []):
                total_evaluable_items += 1
                sub_num = str(sub.get("number"))
                sub_key = f"{q_id}_{sub_num}"
                correct_ans = str(sub.get("answer", "")).strip()
                user_ans = str(student_answers.get(sub_key, "")).strip()
                is_correct = (user_ans.lower() == correct_ans.lower())
                if is_correct:
                    correct_items += 1
                sub_results.append({
                    "number": sub_num,
                    "question": sub.get("question"),
                    "student_answer": user_ans,
                    "correct_answer": correct_ans,
                    "is_correct": is_correct,
                    "explanation": sub.get("explanation", "")
                })
            item_detail["sub_results"] = sub_results

        details.append(item_detail)

    # Tính điểm trên thang điểm 10.0
    if total_evaluable_items > 0:
        score_10 = round((correct_items / total_evaluable_items) * 10.0, 1)
    else:
        score_10 = 0.0

    # Lời nhận xét sư phạm
    if score_10 >= 9.0:
        feedback = "Xuất sắc! Em nắm rất vững kiến thức và kỹ năng làm bài Tiếng Anh. Tiếp tục phát huy nhé!"
        badge = "Xuất Sắc 🏆"
    elif score_10 >= 8.0:
        feedback = "Rất tốt! Em đạt kết quả Giỏi, chỉ cần chú ý thêm một số bẫy ngữ pháp nhỏ để đạt điểm tuyệt đối."
        badge = "Học Sinh Giỏi 🌟"
    elif score_10 >= 6.5:
        feedback = "Khá tốt! Em đã nắm được kiến thức trọng tâm, hãy tích cực đọc thêm và làm thêm bài tập nâng cao."
        badge = "Học Sinh Khá 👍"
    elif score_10 >= 5.0:
        feedback = "Đạt yêu cầu! Em hãy đọc kỹ phần giải thích chi tiết từng câu ở bên dưới để khắc phục các lỗi sai nhé."
        badge = "Trung Bình 📚"
    else:
        feedback = "Cần cố gắng hơn nữa! Em hãy ôn lại từ vựng, cấu trúc câu và làm lại bài để cải thiện điểm số nhé."
        badge = "Cố Gắng Lên 💪"

    submission_id = f"SUB_{uuid.uuid4().hex[:8].upper()}"
    record = {
        "id": submission_id,
        "exam_id": exam_id,
        "exam_title": exam.get("title", ""),
        "grade": exam.get("grade", "6"),
        "student_name": student_info.get("name", "Học sinh"),
        "student_class": student_info.get("class", "6A"),
        "school": student_info.get("school", "THCS Đồng Yên"),
        "score": score_10,
        "correct_items": correct_items,
        "total_items": total_evaluable_items,
        "badge": badge,
        "feedback": feedback,
        "submitted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "time_spent_seconds": student_info.get("time_spent", 0),
        "details": details
    }

    # Lưu vào database
    all_subs = _load_submissions()
    if exam_id not in all_subs:
        all_subs[exam_id] = []
    all_subs[exam_id].append(record)
    _save_submissions(all_subs)

    return record

def get_submissions_by_exam(exam_id: str):
    """Lấy danh sách các bài đã nộp của một đề kiểm tra"""
    all_subs = _load_submissions()
    subs = all_subs.get(exam_id, [])
    # Sắp xếp mới nhất lên đầu
    subs_sorted = sorted(subs, key=lambda x: x.get("submitted_at", ""), reverse=True)
    
    # Thống kê tổng quan
    total_count = len(subs_sorted)
    if total_count > 0:
        scores = [s.get("score", 0) for s in subs_sorted]
        avg_score = round(sum(scores) / total_count, 1)
        max_score = max(scores)
        min_score = min(scores)
        excellent_count = sum(1 for sc in scores if sc >= 8.0)
        good_count = sum(1 for sc in scores if 6.5 <= sc < 8.0)
        avg_count = sum(1 for sc in scores if 5.0 <= sc < 6.5)
        need_improve_count = sum(1 for sc in scores if sc < 5.0)
    else:
        avg_score = max_score = min_score = 0
        excellent_count = good_count = avg_count = need_improve_count = 0

    return {
        "exam_id": exam_id,
        "total_submissions": total_count,
        "stats": {
            "average_score": avg_score,
            "max_score": max_score,
            "min_score": min_score,
            "excellent_count": excellent_count,
            "good_count": good_count,
            "average_count": avg_count,
            "need_improve_count": need_improve_count
        },
        "submissions": subs_sorted
    }

def get_submission_detail(submission_id: str):
    """Lấy chi tiết một bài nộp cụ thể"""
    all_subs = _load_submissions()
    for eid, sub_list in all_subs.items():
        for sub in sub_list:
            if sub.get("id") == submission_id:
                return sub
    return None

def export_exam_submissions_to_excel(exam_id: str, output_path: str = None) -> str:
    """Xuất bảng điểm bài kiểm tra ra file Excel (.xlsx) chuẩn hoá đẹp mắt"""
    sub_data = get_submissions_by_exam(exam_id)
    exam = get_exam_by_id(exam_id)
    exam_title = exam.get("title", f"Bài Kiểm Tra {exam_id}") if exam else f"Bài Kiểm Tra {exam_id}"

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Bảng Điểm Học Sinh"

    # Định dạng font & màu sắc chuyên nghiệp
    font_header_title = Font(name="Times New Roman", size=14, bold=True, color="1E3A8A")
    font_sub_title = Font(name="Times New Roman", size=12, italic=True)
    font_col_header = Font(name="Times New Roman", size=11, bold=True, color="FFFFFF")
    font_data = Font(name="Times New Roman", size=11)
    font_score = Font(name="Times New Roman", size=12, bold=True, color="DC2626")

    fill_header = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
    fill_row_alt = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")

    align_center = Alignment(horizontal="center", vertical="center", wrap_text=True)
    align_left = Alignment(horizontal="left", vertical="center")
    align_right = Alignment(horizontal="right", vertical="center")

    thin_border_side = Side(border_style="thin", color="CBD5E1")
    border_cell = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)

    # Dòng 1 & 2: Tiêu đề cơ quan & trường
    ws.merge_cells("A1:G1")
    ws["A1"] = "TRƯỜNG THCS ĐỒNG YÊN - HỌC & KIỂM TRA TIẾNG ANH TRỰC TUYẾN"
    ws["A1"].font = font_sub_title
    ws["A1"].alignment = align_center

    ws.merge_cells("A2:G2")
    ws["A2"] = f"BẢNG TỔNG HỢP ĐIỂM BÀI LÀM: {exam_title.upper()}"
    ws["A2"].font = font_header_title
    ws["A2"].alignment = align_center

    ws.merge_cells("A3:G3")
    ws["A3"] = f"Giáo viên phụ trách: Thầy giáo Đinh Văn Thành (0915.213717) - Xuất ngày: {datetime.now().strftime('%d/%m/%Y %H:%M')}"
    ws["A3"].font = font_sub_title
    ws["A3"].alignment = align_center

    # Dòng tiêu đề cột
    headers = [
        "STT",
        "Họ và tên học sinh",
        "Lớp",
        "Điểm (Thang 10)",
        "Xếp loại",
        "Số câu đúng",
        "Thời gian nộp"
    ]

    row_num = 5
    for col_idx, header in enumerate(headers, 1):
        cell = ws.cell(row=row_num, column=col_idx, value=header)
        cell.font = font_col_header
        cell.fill = fill_header
        cell.alignment = align_center
        cell.border = border_cell

    # Ghi dữ liệu học sinh
    subs = sub_data.get("submissions", [])
    for idx, sub in enumerate(subs, 1):
        row_num += 1
        r_fill = fill_row_alt if idx % 2 == 0 else PatternFill(fill_type=None)

        c1 = ws.cell(row=row_num, column=1, value=idx)
        c2 = ws.cell(row=row_num, column=2, value=sub.get("student_name", ""))
        c3 = ws.cell(row=row_num, column=3, value=sub.get("student_class", ""))
        c4 = ws.cell(row=row_num, column=4, value=sub.get("score", 0.0))
        c5 = ws.cell(row=row_num, column=5, value=sub.get("badge", ""))
        c6 = ws.cell(row=row_num, column=6, value=f"{sub.get('correct_items', 0)}/{sub.get('total_items', 0)}")
        c7 = ws.cell(row=row_num, column=7, value=sub.get("submitted_at", ""))

        c1.alignment = align_center
        c2.alignment = align_left
        c3.alignment = align_center
        c4.alignment = align_center
        c5.alignment = align_center
        c6.alignment = align_center
        c7.alignment = align_center

        for cell in [c1, c2, c3, c4, c5, c6, c7]:
            cell.font = font_data
            cell.border = border_cell
            if r_fill.fill_type:
                cell.fill = r_fill

        c4.font = font_score

    # Thống kê tổng hợp ở dưới
    row_num += 2
    ws.merge_cells(f"A{row_num}:G{row_num}")
    stats = sub_data.get("stats", {})
    ws[f"A{row_num}"] = (
        f"📊 TỔNG HỢP: Tổng số học sinh nộp: {sub_data.get('total_submissions', 0)} em | "
        f"Điểm TB: {stats.get('average_score', 0)}đ | "
        f"Cao nhất: {stats.get('max_score', 0)}đ | "
        f"Giỏi: {stats.get('excellent_count', 0)} | "
        f"Khá: {stats.get('good_count', 0)} | "
        f"TB: {stats.get('average_count', 0)} | "
        f"Cần cố gắng: {stats.get('need_improve_count', 0)}"
    )
    ws[f"A{row_num}"].font = Font(name="Times New Roman", size=11, bold=True, color="047857")
    ws[f"A{row_num}"].alignment = align_left

    # Đặt độ rộng cột tự động
    column_widths = {1: 8, 2: 28, 3: 12, 4: 16, 5: 20, 6: 16, 7: 22}
    for col_idx, width in column_widths.items():
        ws.column_dimensions[openpyxl.utils.get_column_letter(col_idx)].width = width

    # Đường dẫn xuất
    if not output_path:
        out_dir = os.path.join(DATA_DIR, "Bang_Diem_Xuat_Ra")
        os.makedirs(out_dir, exist_ok=True)
        safe_id = "".join([c if c.isalnum() or c in "_-" else "_" for c in exam_id])
        output_path = os.path.join(out_dir, f"Bang_Diem_{safe_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx")

    wb.save(output_path)
    return output_path
