# -*- coding: utf-8 -*-
"""
FASTAPI SERVER - CỔNG HỌC & KIỂM TRA TIẾNG ANH THCS
Tác giả: Thầy giáo Đinh Văn Thành - Hotline / Zalo: 0915.213717
Đơn vị: Trường THCS Đồng Yên
"""

import os
import sys
from typing import Optional, List, Dict, Any
from fastapi import FastAPI, HTTPException, Query, Body, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .network_utils import get_local_ip, build_student_assignment_link, build_teacher_review_link
from .question_bank import get_grade_questions, get_all_grades_summary
from .exam_store import (
    list_all_exams,
    get_exam_by_id,
    create_custom_exam,
    delete_exam,
    generate_default_suite
)
from .submission_store import (
    grade_submission,
    get_submissions_by_exam,
    get_submission_detail,
    export_exam_submissions_to_excel
)
from .fun_games_data import get_game_data
from .classroom_store import (
    get_all_classes,
    create_class,
    import_students_from_text,
    get_students_by_class,
    authenticate_student,
    export_student_accounts_to_excel,
    get_class_gradebook_analytics
)
from .kien_curriculum import get_curriculum

# Khởi tạo FastAPI App
app = FastAPI(
    title="Hệ Thống Học & Kiểm Tra Tiếng Anh THCS - Thầy Đinh Văn Thành",
    description="Cổng giao bài, nhận bài và kho bài tập tương tác chuẩn GDPT Global Success Lớp 6 - 9",
    version="2.0.0"
)

# Kích hoạt CORS để hỗ trợ mọi thiết bị
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Đường dẫn thư mục
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB_DIR = os.path.join(BASE_DIR, "web")
STATIC_DIR = os.path.join(WEB_DIR, "static")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

os.makedirs(STATIC_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
if os.path.exists(ASSETS_DIR):
    app.mount("/assets", StaticFiles(directory=ASSETS_DIR), name="assets")

# Đảm bảo có sẵn các bộ đề mặc định
generate_default_suite()

# =========================================================================
# WEB PAGES SERVING
# =========================================================================
@app.get("/", response_class=HTMLResponse)
async def serve_index():
    index_path = os.path.join(WEB_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return HTMLResponse("<h1>Học Tiếng Anh THCS - Thầy Đinh Văn Thành</h1>")

@app.get("/lam-bai", response_class=HTMLResponse)
async def serve_student_page(id: Optional[str] = None):
    student_path = os.path.join(WEB_DIR, "student.html")
    if os.path.exists(student_path):
        return FileResponse(student_path)
    return FileResponse(os.path.join(WEB_DIR, "index.html"))

@app.get("/giao-vien", response_class=HTMLResponse)
async def serve_teacher_page(view: Optional[str] = None, id: Optional[str] = None):
    teacher_path = os.path.join(WEB_DIR, "teacher.html")
    if os.path.exists(teacher_path):
        return FileResponse(teacher_path)
    return FileResponse(os.path.join(WEB_DIR, "index.html"))

@app.get("/tro-choi", response_class=HTMLResponse)
async def serve_games_page(grade: Optional[str] = "6", game: Optional[str] = "wheel"):
    games_path = os.path.join(WEB_DIR, "fun_games.html")
    if os.path.exists(games_path):
        return FileResponse(games_path)
    return FileResponse(os.path.join(WEB_DIR, "index.html"))

@app.get("/luyen-noi", response_class=HTMLResponse)
async def serve_speaking_page():
    speaking_path = os.path.join(WEB_DIR, "speaking.html")
    if os.path.exists(speaking_path):
        return FileResponse(speaking_path)
    return FileResponse(os.path.join(WEB_DIR, "index.html"))

@app.get("/the-tu-vung", response_class=HTMLResponse)
async def serve_flashcards_page():
    flashcards_path = os.path.join(WEB_DIR, "flashcards.html")
    if os.path.exists(flashcards_path):
        return FileResponse(flashcards_path)
    return FileResponse(os.path.join(WEB_DIR, "index.html"))

@app.get("/phong-hoc", response_class=HTMLResponse)
@app.get("/classroom", response_class=HTMLResponse)
async def serve_classroom_page():
    classroom_path = os.path.join(WEB_DIR, "classroom.html")
    if os.path.exists(classroom_path):
        return FileResponse(classroom_path)
    return FileResponse(os.path.join(WEB_DIR, "index.html"))


# =========================================================================
# API ROUTES
# =========================================================================
@app.get("/api/status")
async def get_system_status():
    local_ip = get_local_ip()
    return {
        "status": "online",
        "app_name": "Hệ Thống Học & Kiểm Tra Tiếng Anh THCS (Lớp 6 - 9)",
        "author": "Thầy giáo Đinh Văn Thành",
        "hotline": "0915.213717",
        "school": "Trường THCS Đồng Yên",
        "local_ip": local_ip,
        "port": 8080
    }

@app.get("/api/grades")
async def get_grades():
    """Lấy danh sách các khối lớp và thông tin tóm tắt"""
    return get_all_grades_summary()

@app.get("/api/question-bank/{grade}")
async def get_questions_by_grade(grade: str):
    """Lấy toàn bộ ngân hàng câu hỏi của một khối lớp"""
    return get_grade_questions(grade)

@app.get("/api/exams")
async def get_all_exams():
    """Liệt kê toàn bộ đề kiểm tra / bài tập hiện có"""
    return list_all_exams()

@app.get("/api/exam/{exam_id}")
async def get_exam(exam_id: str, for_student: bool = False):
    """Lấy nội dung đề thi (cho học sinh hoặc giáo viên)"""
    exam = get_exam_by_id(exam_id, for_student=for_student)
    if not exam:
        raise HTTPException(status_code=404, detail="Không tìm thấy bài thi")
    return exam

class CreateExamRequest(BaseModel):
    id: Optional[str] = None
    title: str
    grade: str
    duration_minutes: int = 45
    description: Optional[str] = ""
    created_by: Optional[str] = "Thầy giáo Đinh Văn Thành"
    questions: List[Dict[str, Any]]

@app.post("/api/exam/create")
async def create_exam_endpoint(payload: CreateExamRequest):
    """Giáo viên tạo bài tập / đề kiểm tra mới"""
    new_exam = create_custom_exam(payload.dict())
    return {
        "success": True,
        "message": "Đã tạo đề kiểm tra thành công!",
        "exam": new_exam,
        "assignment_links": build_student_assignment_link(new_exam["id"])
    }

@app.delete("/api/exam/{exam_id}")
async def delete_exam_endpoint(exam_id: str):
    success = delete_exam(exam_id)
    if not success:
        raise HTTPException(status_code=404, detail="Không tìm thấy bài thi để xóa")
    return {"success": True, "message": "Đã xóa bài thi thành công"}

@app.get("/api/assignment-link/{exam_id}")
async def get_assignment_link(exam_id: str, host: Optional[str] = None, port: int = 8080):
    """Sinh link giao bài cho học sinh và link nhận bài cho giáo viên"""
    student_links = build_student_assignment_link(exam_id, host=host, port=port)
    teacher_links = build_teacher_review_link(exam_id, host=host, port=port)
    return {
        "exam_id": exam_id,
        "student": student_links,
        "teacher": teacher_links
    }

class SubmitExamRequest(BaseModel):
    exam_id: str
    student: Dict[str, Any]
    answers: Dict[str, Any]

@app.post("/api/exam/submit")
async def submit_exam_endpoint(payload: SubmitExamRequest):
    """Học sinh nộp bài và nhận điểm số, đánh giá ngay lập tức"""
    try:
        result = grade_submission(
            exam_id=payload.exam_id,
            student_info=payload.student,
            student_answers=payload.answers
        )
        return {
            "success": True,
            "message": "Nộp bài thành công!",
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/submissions/{exam_id}")
async def get_exam_submissions(exam_id: str):
    """Giáo viên lấy danh sách bài đã nộp và bảng điểm của đề thi"""
    return get_submissions_by_exam(exam_id)

@app.get("/api/submission/{submission_id}")
async def get_single_submission(submission_id: str):
    """Xem chi tiết bài làm của một học sinh cụ thể"""
    sub = get_submission_detail(submission_id)
    if not sub:
        raise HTTPException(status_code=404, detail="Không tìm thấy bài nộp")
    return sub

@app.get("/api/submissions/{exam_id}/export-excel")
async def export_excel_endpoint(exam_id: str):
    """Xuất file Excel bảng điểm học sinh để giáo viên tải về"""
    try:
        excel_path = export_exam_submissions_to_excel(exam_id)
        filename = os.path.basename(excel_path)
        return FileResponse(
            excel_path,
            filename=filename,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi xuất Excel: {str(e)}")

@app.get("/api/games/{game_name}/{grade}")
async def get_games_endpoint(game_name: str, grade: str):
    """Lấy dữ liệu mini-games theo khối lớp (lucky_wheel, millionaire, speed_match, sentence_puzzle)"""
    data = get_game_data(game_name, grade)
    return {
        "game": game_name,
        "grade": grade,
        "data": data
    }

# =========================================================================
# CLASSROOM & STUDENT ACCOUNT MANAGEMENT APIS
# =========================================================================
@app.get("/api/classes")
async def get_classes_endpoint():
    """Lấy danh sách các lớp học"""
    return get_all_classes()

class CreateClassPayload(BaseModel):
    name: str
    grade: str
    school_year: Optional[str] = "2026 - 2027"
    teacher: Optional[str] = "Thầy Đinh Văn Thành"

@app.post("/api/classes/create")
async def create_class_endpoint(payload: CreateClassPayload):
    """Tạo lớp học mới"""
    cls = create_class(payload.name, payload.grade, payload.school_year, payload.teacher)
    return {"success": True, "class": cls}

@app.get("/api/students/{class_name}")
async def get_students_endpoint(class_name: str):
    """Lấy danh sách học sinh theo lớp"""
    return get_students_by_class(class_name)

class ImportStudentsPayload(BaseModel):
    class_name: str
    raw_text: str
    default_password: Optional[str] = "123456"

@app.post("/api/students/import")
async def import_students_endpoint(payload: ImportStudentsPayload):
    """Tạo tài khoản học sinh hàng loạt từ danh sách dán vào"""
    students = import_students_from_text(payload.raw_text, payload.class_name, payload.default_password)
    return {
        "success": True,
        "count": len(students),
        "students": students,
        "message": f"Đã tạo thành công {len(students)} tài khoản học sinh cho lớp {payload.class_name}!"
    }

@app.get("/api/students/{class_name}/export-excel")
async def export_students_excel(class_name: str):
    """Xuất file Excel danh sách tài khoản học sinh kèm mật khẩu để in hoặc gửi phụ huynh"""
    try:
        path = export_student_accounts_to_excel(class_name)
        filename = os.path.basename(path)
        return FileResponse(
            path,
            filename=filename,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi xuất Excel tài khoản: {str(e)}")

class StudentLoginPayload(BaseModel):
    username: str
    password: str

@app.post("/api/students/login")
async def student_login_endpoint(payload: StudentLoginPayload):
    """Đăng nhập học sinh"""
    student = authenticate_student(payload.username, payload.password)
    if not student:
        raise HTTPException(status_code=401, detail="Tên đăng nhập hoặc mật khẩu không chính xác!")
    return {
        "success": True,
        "student": student,
        "message": f"Chào mừng em {student.get('full_name')} ({student.get('class_name')}) đã đăng nhập thành công!"
    }

@app.get("/api/gradebook/{class_name}")
async def get_gradebook_endpoint(class_name: str):
    """Bảng điểm tổng hợp và phân tích lớp học như lớp online chuyên nghiệp"""
    return get_class_gradebook_analytics(class_name)

@app.get("/api/curriculum/{grade}")
async def get_curriculum_endpoint(grade: str):
    """Lấy kiến thức và phân phối chương trình 105 tiết từ Kien"""
    return get_curriculum(grade)

