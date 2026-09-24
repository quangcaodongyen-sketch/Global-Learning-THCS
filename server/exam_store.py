# -*- coding: utf-8 -*-
"""
HỆ THỐNG LƯU TRỮ VÀ TẠO BỘ ĐỀ / BÀI TẬP (EXAM STORE)
Tác giả: Thầy giáo Đinh Văn Thành - Hotline / Zalo: 0915.213717
Hỗ trợ tạo đề tự động từ ngân hàng và tạo đề tùy chỉnh cho giáo viên
"""

import os
import json
import uuid
import copy
import tempfile
from datetime import datetime
from .question_bank import QUESTION_BANK

BASE_WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if os.environ.get("VERCEL") or not os.access(BASE_WORKSPACE, os.W_OK):
    DATA_DIR = os.path.join(tempfile.gettempdir(), "global_learning_data")
else:
    DATA_DIR = os.path.join(BASE_WORKSPACE, "data")

ASSIGNMENTS_FILE = os.path.join(DATA_DIR, "assignments.json")

try:
    os.makedirs(DATA_DIR, exist_ok=True)
except Exception:
    pass

def _load_assignments():
    if os.path.exists(ASSIGNMENTS_FILE):
        try:
            with open(ASSIGNMENTS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def _save_assignments(data):
    try:
        with open(ASSIGNMENTS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Warning: could not save assignments to disk: {e}")

def generate_default_suite():
    """Tạo sẵn các bộ đề mẫu chuẩn THCS Lớp 6 - 9 nếu chưa có"""
    existing = _load_assignments()
    if existing:
        return existing

    defaults = {}
    terms_info = [
        ("15P-U1", "Bài Kiểm Tra 15 Phút - Unit 1 & 2", 15, "15 phút khởi động kiến thức đầu năm"),
        ("GK1", "Đề Kiểm Tra Giữa Học Kỳ I (Chuẩn CV 7991)", 45, "Đánh giá năng lực giữa kỳ 1"),
        ("CK1", "Đề Kiểm Tra Cuối Học Kỳ I (Toàn Diện 4 Kỹ Năng)", 60, "Đánh giá chất lượng cuối học kỳ 1"),
        ("GK2", "Đề Kiểm Tra Giữa Học Kỳ II (Chuẩn CV 7991)", 45, "Đánh giá năng lực giữa kỳ 2"),
        ("CK2", "Đề Kiểm Tra Cuối Học Kỳ II (Toàn Diện 4 Kỹ Năng)", 60, "Đánh giá chất lượng cuối học kỳ 2")
    ]

    for grade in ["6", "7", "8", "9"]:
        bank = QUESTION_BANK.get(grade, QUESTION_BANK["6"])
        for code, name, duration, desc in terms_info:
            exam_id = f"ENG{grade}_{code}"
            
            # Tuyển chọn câu hỏi mẫu phong phú
            questions = []
            
            # 1. Phát âm (2 câu)
            ph = bank.get("phonetics", [])
            for q in ph[:2]:
                q_copy = copy.deepcopy(q)
                questions.append(q_copy)
                
            # 2. Odd one out (1 câu)
            odd = bank.get("odd_one_out", [])
            for q in odd[:1]:
                q_copy = copy.deepcopy(q)
                questions.append(q_copy)
                
            # 3. Trắc nghiệm (4 câu)
            mc = bank.get("multiple_choice", [])
            for q in mc[:4]:
                q_copy = copy.deepcopy(q)
                questions.append(q_copy)
                
            # 4. Cloze test (1 bài)
            cl = bank.get("cloze", [])
            if cl:
                questions.append(copy.deepcopy(cl[0]))
                
            # 5. Matching (1 bài)
            ma = bank.get("matching", [])
            if ma:
                questions.append(copy.deepcopy(ma[0]))
                
            # 6. Sentence Unscramble (1 bài)
            uns = bank.get("sentence_unscramble", [])
            if uns:
                questions.append(copy.deepcopy(uns[0]))
                
            # 7. Sentence Transformation (1 bài)
            tr = bank.get("transformation", [])
            if tr:
                questions.append(copy.deepcopy(tr[0]))
                
            # 8. Reading (1 bài)
            re = bank.get("reading", [])
            if re:
                questions.append(copy.deepcopy(re[0]))
                
            # 9. Listening (1 bài)
            li = bank.get("listening", [])
            if li:
                questions.append(copy.deepcopy(li[0]))

            defaults[exam_id] = {
                "id": exam_id,
                "title": f"Tiếng Anh {grade} - {name}",
                "grade": grade,
                "duration_minutes": duration,
                "description": desc,
                "created_by": "Thầy giáo Đinh Văn Thành",
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "is_active": True,
                "questions": questions
            }

    _save_assignments(defaults)
    return defaults

def list_all_exams():
    """Liệt kê toàn bộ đề kiểm tra / bài tập hiện có"""
    data = _load_assignments()
    if not data:
        data = generate_default_suite()
    
    result = []
    for eid, item in data.items():
        result.append({
            "id": eid,
            "title": item.get("title", ""),
            "grade": item.get("grade", "6"),
            "duration_minutes": item.get("duration_minutes", 45),
            "description": item.get("description", ""),
            "created_by": item.get("created_by", ""),
            "created_at": item.get("created_at", ""),
            "question_count": len(item.get("questions", [])),
            "is_active": item.get("is_active", True)
        })
    # Sắp xếp theo khối lớp và mã đề
    result.sort(key=lambda x: (x["grade"], x["id"]))
    return result

def get_exam_by_id(exam_id: str, for_student: bool = False):
    """Lấy chi tiết một bài thi. Nếu for_student=True thì ẩn đáp án và giải thích"""
    data = _load_assignments()
    if exam_id not in data:
        data = generate_default_suite()
    
    exam = data.get(exam_id)
    if not exam:
        return None

    exam_copy = copy.deepcopy(exam)
    if for_student:
        for q in exam_copy.get("questions", []):
            q.pop("answer", None)
            q.pop("explanation", None)
            q.pop("correct_sentence", None)
            q.pop("correct_answer", None)
            if q.get("type") == "cloze":
                for sub in q.get("questions", []):
                    sub.pop("answer", None)
                    sub.pop("explanation", None)
            if q.get("type") == "reading":
                for sub in q.get("questions", []):
                    sub.pop("answer", None)
                    sub.pop("explanation", None)
    return exam_copy

def create_custom_exam(exam_payload: dict):
    """Giáo viên tự tạo bài kiểm tra hoặc bài tập mới"""
    data = _load_assignments()
    
    exam_id = exam_payload.get("id")
    if not exam_id:
        raw_id = f"EXAM_{exam_payload.get('grade', '6')}_{uuid.uuid4().hex[:6].upper()}"
        exam_id = raw_id
    
    exam_item = {
        "id": exam_id,
        "title": exam_payload.get("title", "Bài tập Tiếng Anh THCS"),
        "grade": str(exam_payload.get("grade", "6")),
        "duration_minutes": int(exam_payload.get("duration_minutes", 45)),
        "description": exam_payload.get("description", "Bài tập giao về nhà / kiểm tra trực tuyến"),
        "created_by": exam_payload.get("created_by", "Thầy giáo Đinh Văn Thành"),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "is_active": True,
        "questions": exam_payload.get("questions", [])
    }
    
    data[exam_id] = exam_item
    _save_assignments(data)
    return exam_item

def delete_exam(exam_id: str):
    """Xóa đề kiểm tra"""
    data = _load_assignments()
    if exam_id in data:
        del data[exam_id]
        _save_assignments(data)
        return True
    return False
