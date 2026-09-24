# -*- coding: utf-8 -*-
"""
Tiện ích phát hiện mạng nội bộ & tạo liên kết giao bài
Thầy giáo Đinh Văn Thành - Hotline / Zalo: 0915.213717
"""

import socket
import urllib.parse

def get_local_ip():
    """Lấy địa chỉ IPv4 nội bộ (LAN / WiFi) của máy tính đang chạy server"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Không cần kết nối thật, chỉ cần socket định tuyến ra ngoài
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        try:
            return socket.gethostbyname(socket.gethostname())
        except Exception:
            return "127.0.0.1"

def build_student_assignment_link(exam_id: str, host: str = None, port: int = 8080) -> dict:
    """Tạo các đường dẫn giao bài cho học sinh (Localhost & LAN IP)"""
    lan_ip = host or get_local_ip()
    local_url = f"http://localhost:{port}/lam-bai?id={urllib.parse.quote(exam_id)}"
    lan_url = f"http://{lan_ip}:{port}/lam-bai?id={urllib.parse.quote(exam_id)}"
    
    zalo_msg = (
        f"📢 [BÀI TẬP TIẾNG ANH THCS - THẦY ĐINH VĂN THÀNH]\n"
        f"👉 Các em bấm vào link dưới đây để làm bài kiểm tra trực tuyến:\n"
        f"🔗 Link làm bài: {lan_url}\n"
        f"📌 Mã bài thi: {exam_id}\n"
        f"⚠️ Chú ý: Điền đúng Họ tên và Lớp trước khi bắt đầu. Chúc các em đạt điểm cao! 🌟"
    )
    
    return {
        "exam_id": exam_id,
        "local_url": local_url,
        "lan_url": lan_url,
        "lan_ip": lan_ip,
        "port": port,
        "zalo_message": zalo_msg
    }

def build_teacher_review_link(exam_id: str = "", host: str = None, port: int = 8080) -> dict:
    """Tạo đường dẫn nhận bài & bảng điểm cho giáo viên"""
    lan_ip = host or get_local_ip()
    base = f"http://localhost:{port}/giao-vien"
    review_url = f"{base}?view=submissions&id={urllib.parse.quote(exam_id)}" if exam_id else f"{base}?view=submissions"
    lan_review_url = f"http://{lan_ip}:{port}/giao-vien?view=submissions&id={urllib.parse.quote(exam_id)}" if exam_id else f"http://{lan_ip}:{port}/giao-vien?view=submissions"
    
    return {
        "local_url": review_url,
        "lan_url": lan_review_url,
        "lan_ip": lan_ip,
        "port": port
    }
