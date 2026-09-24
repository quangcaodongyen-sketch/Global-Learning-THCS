/**
 * TEACHER DASHBOARD, EXAM CREATOR, SHARE LINK & SUBMISSIONS HUB
 * Thầy giáo Đinh Văn Thành - Hotline / Zalo: 0915.213717
 * Trường THCS Đồng Yên
 */

let allExams = [];
let selectedExamId = null;

document.addEventListener('DOMContentLoaded', () => {
  loadTeacherExams();

  const urlParams = new URLSearchParams(window.location.search);
  const initialView = urlParams.get('view');
  const targetId = urlParams.get('id');

  if (initialView === 'submissions') {
    switchTeacherTab('tabSubmissions');
    if (targetId) {
      setTimeout(() => {
        const sel = document.getElementById('selectExamForSubmissions');
        if (sel) {
          sel.value = targetId;
          loadSubmissionsForExam(targetId);
        }
      }, 500);
    }
  }

  // Khởi tạo tab ra đề
  initExamCreatorEvents();
});

// 1. CHUYỂN ĐỔI TAB QUẢN TRỊ
function switchTeacherTab(tabId) {
  document.querySelectorAll('.teacher-tab-content').forEach(el => el.style.display = 'none');
  document.querySelectorAll('.teacher-nav-btn').forEach(btn => btn.classList.remove('active'));

  const target = document.getElementById(tabId);
  if (target) target.style.display = 'block';

  const activeBtn = document.querySelector(`[data-target="${tabId}"]`);
  if (activeBtn) activeBtn.classList.add('active');

  if (tabId === 'tabSubmissions') {
    refreshSubmissionsSelect();
  }
}

// 2. TẢI DANH SÁCH BỘ ĐỀ
async function loadTeacherExams() {
  try {
    const res = await fetch('/api/exams');
    allExams = await res.json();
    renderExamsList(allExams);
    populateExamSelects(allExams);
  } catch (err) {
    console.error('Lỗi tải danh sách đề:', err);
  }
}

function renderExamsList(exams) {
  const container = document.getElementById('teacherExamsList');
  if (!container) return;

  if (exams.length === 0) {
    container.innerHTML = `<div style="color: var(--text-muted); padding: 2rem;">Chưa có đề kiểm tra nào. Hãy bấm 'Tạo đề mới'.</div>`;
    return;
  }

  let html = '';
  exams.forEach(ex => {
    html += `
      <div class="exam-card">
        <div class="card-top">
          <span class="tag-grade">LỚP ${ex.grade}</span>
          <span class="tag-duration">⏱️ ${ex.duration_minutes} phút</span>
        </div>
        <h3 class="card-title">${ex.title}</h3>
        <p class="card-desc">${ex.description || 'Bài tập rèn luyện năng lực tiếng Anh'}</p>
        <div class="card-meta">
          <span>📝 ${ex.question_count} câu</span>
          <span>📅 ${ex.created_at || 'Mới tạo'}</span>
        </div>
        <div class="card-actions">
          <button type="button" class="btn btn-primary btn-sm" onclick="openShareLinkModal('${ex.id}')">
            🔗 Lấy Link Giao
          </button>
          <button type="button" class="btn btn-emerald btn-sm" onclick="viewSubmissions('${ex.id}')">
            📊 Xem Bảng Điểm
          </button>
        </div>
      </div>
    `;
  });
  container.innerHTML = html;
}

function populateExamSelects(exams) {
  const selectSub = document.getElementById('selectExamForSubmissions');
  if (!selectSub) return;

  selectSub.innerHTML = '<option value="">-- Chọn bài kiểm tra để xem điểm --</option>';
  exams.forEach(ex => {
    selectSub.innerHTML += `<option value="${ex.id}">[Lớp ${ex.grade}] ${ex.title} (${ex.id})</option>`;
  });
}

function refreshSubmissionsSelect() {
  const selectSub = document.getElementById('selectExamForSubmissions');
  if (selectSub && selectSub.value) {
    loadSubmissionsForExam(selectSub.value);
  }
}

// 3. MỞ MODAL LẤY LINK GIAO BÀI & MÃ QR
async function openShareLinkModal(examId) {
  sounds.playClick();
  selectedExamId = examId;

  try {
    const res = await fetch(`/api/assignment-link/${encodeURIComponent(examId)}`);
    const data = await res.json();

    document.getElementById('modalExamIdDisplay').innerText = examId;
    document.getElementById('shareLocalUrl').value = data.student.local_url;
    document.getElementById('shareLanUrl').value = data.student.lan_url;
    document.getElementById('shareZaloText').value = data.student.zalo_message;

    // Vẽ mã QR Code cho link LAN (để học sinh quét trên điện thoại)
    const qrCanvas = document.getElementById('qrCanvas');
    if (qrCanvas && window.QRCodeLib) {
      QRCodeLib.render(qrCanvas, data.student.lan_url, 220);
    }

    document.getElementById('shareLinkModal').classList.add('active');
  } catch (err) {
    alert('Lỗi lấy link giao bài: ' + err.message);
  }
}

function copyToClipboard(elementId, successMsg = 'Đã sao chép link!') {
  sounds.playClick();
  const input = document.getElementById(elementId);
  if (!input) return;

  input.select();
  navigator.clipboard.writeText(input.value).then(() => {
    alert(`✅ ${successMsg}`);
  }).catch(() => {
    document.execCommand('copy');
    alert(`✅ ${successMsg}`);
  });
}

// 4. XEM BẢNG ĐIỂM (LINK NHẬN BÀI)
function viewSubmissions(examId) {
  switchTeacherTab('tabSubmissions');
  const sel = document.getElementById('selectExamForSubmissions');
  if (sel) {
    sel.value = examId;
    loadSubmissionsForExam(examId);
  }
}

async function loadSubmissionsForExam(examId) {
  if (!examId) return;
  selectedExamId = examId;

  const container = document.getElementById('submissionsTableBody');
  container.innerHTML = `<tr><td colspan="7" style="text-align: center; padding: 2rem;">Đang tải danh sách bài làm...</td></tr>`;

  try {
    const res = await fetch(`/api/submissions/${encodeURIComponent(examId)}`);
    const data = await res.json();

    // Cập nhật thẻ thống kê
    document.getElementById('statTotalSubs').innerText = data.total_submissions;
    document.getElementById('statAvgScore').innerText = `${data.stats.average_score}đ`;
    document.getElementById('statMaxScore').innerText = `${data.stats.max_score}đ`;
    document.getElementById('statExcellent').innerText = `${data.stats.excellent_count} em`;

    if (data.submissions.length === 0) {
      container.innerHTML = `<tr><td colspan="7" style="text-align: center; color: var(--text-muted); padding: 2rem;">Chưa có học sinh nào nộp bài cho đề kiểm tra này.</td></tr>`;
      return;
    }

    let rows = '';
    data.submissions.forEach((sub, idx) => {
      rows += `
        <tr>
          <td style="text-align: center; font-weight: 700;">${idx + 1}</td>
          <td><b>${sub.student_name}</b></td>
          <td style="text-align: center;">${sub.student_class}</td>
          <td style="text-align: center; font-weight: 800; font-size: 1.15rem; color: #ef4444;">${sub.score.toFixed(1)}</td>
          <td style="text-align: center;"><span class="q-badge" style="background: rgba(16, 185, 129, 0.2); color: #34d399;">${sub.badge}</span></td>
          <td style="text-align: center;">${sub.correct_items} / ${sub.total_items}</td>
          <td style="font-size: 0.82rem; color: var(--text-dim);">${sub.submitted_at}</td>
        </tr>
      `;
    });
    container.innerHTML = rows;
  } catch (err) {
    container.innerHTML = `<tr><td colspan="7" style="color: #ef4444; padding: 2rem;">Lỗi tải bảng điểm: ${err.message}</td></tr>`;
  }
}

// 5. XUẤT FILE BẢNG ĐIỂM EXCEL
function exportExcelScores() {
  sounds.playClick();
  const examId = selectedExamId || document.getElementById('selectExamForSubmissions').value;
  if (!examId) {
    alert('Vui lòng chọn bài kiểm tra trước khi xuất Excel!');
    return;
  }
  window.open(`/api/submissions/${encodeURIComponent(examId)}/export-excel`, '_blank');
}

// 6. KHỞI TẠO TRÌNH TẠO ĐỀ THI ĐA DẠNG CÁC LOẠI
function initExamCreatorEvents() {
  const gradeSel = document.getElementById('creatorGradeSelect');
  if (gradeSel) {
    gradeSel.addEventListener('change', () => {
      updateCreatorPreviewQuestions();
    });
  }

  const btnCreate = document.getElementById('btnSubmitCreateExam');
  if (btnCreate) {
    btnCreate.addEventListener('click', handleCreateExamSubmit);
  }
}

async function handleCreateExamSubmit() {
  sounds.playClick();

  const title = document.getElementById('creatorTitleInput').value.trim();
  const grade = document.getElementById('creatorGradeSelect').value;
  const duration = parseInt(document.getElementById('creatorDurationInput').value, 10) || 45;
  const desc = document.getElementById('creatorDescInput').value.trim();

  if (!title) {
    alert('⚠️ Vui lòng nhập tiêu đề bài kiểm tra!');
    document.getElementById('creatorTitleInput').focus();
    return;
  }

  // Thu thập các dạng câu hỏi được chọn
  const checkedTypes = Array.from(document.querySelectorAll('.cb-qtype:checked')).map(el => el.value);
  if (checkedTypes.length === 0) {
    alert('⚠️ Vui lòng chọn ít nhất 1 dạng bài tập (Trắc nghiệm, Phát âm, Điền từ...)');
    return;
  }

  // Lấy câu hỏi tương ứng từ ngân hàng
  try {
    const res = await fetch(`/api/question-bank/${grade}`);
    const bank = await res.json();

    const selectedQuestions = [];
    checkedTypes.forEach(t => {
      const items = bank[t] || [];
      if (items.length > 0) {
        items.forEach(it => selectedQuestions.push(it));
      }
    });

    if (selectedQuestions.length === 0) {
      alert('Không tìm thấy câu hỏi phù hợp trong ngân hàng câu hỏi.');
      return;
    }

    const payload = {
      title: title,
      grade: grade,
      duration_minutes: duration,
      description: desc || `Bài tập rèn luyện Tiếng Anh Lớp ${grade}`,
      created_by: 'Thầy giáo Đinh Văn Thành',
      questions: selectedQuestions
    };

    const createRes = await fetch('/api/exam/create', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    if (!createRes.ok) throw new Error('Không thể tạo đề');
    const result = await createRes.json();

    alert(`🎉 Đã tạo bài kiểm tra thành công!\nMã đề: ${result.exam.id}\nSố phần bài tập: ${result.exam.questions.length}`);
    await loadTeacherExams();
    openShareLinkModal(result.exam.id);
  } catch (err) {
    alert('Lỗi tạo đề: ' + err.message);
  }
}

function updateCreatorPreviewQuestions() {
  // Cập nhật thông tin nhanh nếu cần
}

/* =========================================================================
   7. QUẢN LÝ LỚP HỌC & CẤP TÀI KHOẢN HỌC SINH HÀNG LOẠT
   ========================================================================= */
let currentAccountsClass = '6A';

async function loadClassStudentsList(className) {
  currentAccountsClass = className || '6A';
  const tbody = document.getElementById('studentAccountsTableBody');
  if (!tbody) return;

  tbody.innerHTML = `<tr><td colspan="7" style="text-align: center; padding: 2rem;">Đang tải danh sách học sinh lớp ${currentAccountsClass}...</td></tr>`;

  try {
    const res = await fetch(`/api/students/${encodeURIComponent(currentAccountsClass)}`);
    const students = await res.json();

    if (students.length === 0) {
      tbody.innerHTML = `<tr><td colspan="7" style="text-align: center; color: var(--text-muted); padding: 2.5rem;">Lớp ${currentAccountsClass} chưa có học sinh nào. Thầy hãy dán danh sách ở trên rồi bấm 'Tự động tạo tài khoản'!</td></tr>`;
      return;
    }

    let rows = '';
    students.forEach((s, idx) => {
      rows += `
        <tr>
          <td style="text-align: center; font-weight: 700;">${idx + 1}</td>
          <td style="text-align: center; font-family: monospace; font-weight: 700; color: #a5b4fc;">${s.student_id}</td>
          <td><b>${s.full_name}</b></td>
          <td style="text-align: center;">${s.class_name}</td>
          <td style="text-align: center; font-weight: 700; color: #38bdf8; font-family: monospace;">${s.username}</td>
          <td style="text-align: center; font-weight: 700; color: #f87171; font-family: monospace;">${s.password || '123456'}</td>
          <td style="text-align: center;"><span class="q-badge" style="background: rgba(16, 185, 129, 0.2); color: #34d399;">Hoạt động</span></td>
        </tr>
      `;
    });
    tbody.innerHTML = rows;
  } catch (err) {
    tbody.innerHTML = `<tr><td colspan="7" style="color: #ef4444; padding: 2rem;">Lỗi tải học sinh: ${err.message}</td></tr>`;
  }
}

async function handleImportStudents() {
  sounds.playClick();
  const className = document.getElementById('selectClassForAccounts').value;
  const rawText = document.getElementById('rawStudentsInput').value.trim();
  const defaultPass = document.getElementById('defaultStudentPassword').value.trim() || '123456';

  if (!rawText) {
    alert('⚠️ Vui lòng dán danh sách học sinh vào ô văn bản trước khi bấm tạo tài khoản!');
    document.getElementById('rawStudentsInput').focus();
    return;
  }

  try {
    const res = await fetch('/api/students/import', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        class_name: className,
        raw_text: rawText,
        default_password: defaultPass
      })
    });

    if (!res.ok) throw new Error('Không thể tạo tài khoản');
    const data = await res.json();

    alert(`🎉 ${data.message}`);
    document.getElementById('rawStudentsInput').value = '';
    await loadClassStudentsList(className);
    sounds.playVictory();
  } catch (err) {
    alert('Lỗi tạo tài khoản: ' + err.message);
  }
}

function exportStudentAccountsExcel() {
  sounds.playClick();
  const className = currentAccountsClass || document.getElementById('selectClassForAccounts').value || '6A';
  window.open(`/api/students/${encodeURIComponent(className)}/export-excel`, '_blank');
}

/* =========================================================================
   8. SỔ ĐIỂM ĐIỆN TỬ VÀ ĐÁNH GIÁ ĐIỂM ONLINE CHUYÊN NGHIỆP
   ========================================================================= */
let currentGradebookClass = '6A';
let currentZaloReminderText = '';

async function loadClassGradebook(className) {
  currentGradebookClass = className || '6A';
  const tbody = document.getElementById('classGradebookTableBody');
  if (!tbody) return;

  tbody.innerHTML = `<tr><td colspan="7" style="text-align: center; padding: 2rem;">Đang tổng hợp dữ liệu sổ điểm lớp ${currentGradebookClass}...</td></tr>`;

  try {
    const res = await fetch(`/api/gradebook/${encodeURIComponent(currentGradebookClass)}`);
    const data = await res.json();

    // Cập nhật các thẻ thống kê
    document.getElementById('gbTotalStudents').innerText = `${data.total_students} em`;
    document.getElementById('gbSubmissionRate').innerText = `${data.submission_rate_percent}%`;
    document.getElementById('gbClassAverage').innerText = `${data.class_average_score}đ`;
    document.getElementById('gbUnsubmittedCount').innerText = `${data.unsubmitted_count} em`;

    // Cập nhật khung nhắc nhở Zalo
    const reminderBox = document.getElementById('zaloReminderBox');
    if (data.zalo_reminder_message) {
      reminderBox.style.display = 'block';
      document.getElementById('zaloReminderContent').value = data.zalo_reminder_message;
      currentZaloReminderText = data.zalo_reminder_message;
    } else {
      reminderBox.style.display = 'none';
    }

    if (data.gradebook.length === 0) {
      tbody.innerHTML = `<tr><td colspan="7" style="text-align: center; color: var(--text-muted); padding: 2.5rem;">Lớp ${currentGradebookClass} chưa có danh sách học sinh. Vui lòng chuyển sang tab 'Tạo Tài Khoản Học Sinh' để thêm học sinh!</td></tr>`;
      return;
    }

    let rows = '';
    data.gradebook.forEach(row => {
      const isDone = row.completed_exams_count > 0;
      rows += `
        <tr>
          <td style="text-align: center; font-weight: 700;">${row.stt}</td>
          <td style="text-align: center; font-family: monospace; font-weight: 700; color: #a5b4fc;">${row.student_id}</td>
          <td><b>${row.full_name}</b></td>
          <td style="text-align: center;"><b>${row.completed_exams_count}</b> / ${row.total_assigned_count} bài</td>
          <td style="text-align: center; font-weight: 800; font-size: 1.15rem; color: ${isDone ? '#10b981' : '#94a3b8'};">${isDone ? row.average_score.toFixed(1) : '---'}</td>
          <td style="text-align: center;"><span class="q-badge" style="background: ${isDone ? 'rgba(16, 185, 129, 0.2)' : 'rgba(239, 68, 68, 0.2)'}; color: ${isDone ? '#34d399' : '#f87171'};">${row.rank}</span></td>
          <td style="text-align: center; font-weight: 700; color: ${isDone ? '#34d399' : '#f59e0b'};">${row.status}</td>
        </tr>
      `;
    });
    tbody.innerHTML = rows;
  } catch (err) {
    tbody.innerHTML = `<tr><td colspan="7" style="color: #ef4444; padding: 2rem;">Lỗi tải sổ điểm: ${err.message}</td></tr>`;
  }
}

function copyZaloReminderMessage() {
  sounds.playClick();
  const text = document.getElementById('zaloReminderContent').value;
  if (!text) return;
  navigator.clipboard.writeText(text).then(() => {
    alert('✅ Đã sao chép tin nhắn nhắc nhở Zalo gửi nhóm phụ huynh/học sinh!');
  });
}

function exportClassGradebookExcel() {
  sounds.playClick();
  alert('💡 Tính năng xuất sổ điểm tổng hợp: Đang chuẩn bị tệp Excel xuất dữ liệu cho lớp ' + currentGradebookClass);
}

/* =========================================================================
   9. LỘ TRÌNH KIẾN THỨC 105 TIẾT (CHUẨN KIEN)
   ========================================================================= */
async function loadCurriculumView(grade, btn) {
  sounds.playClick();
  if (btn) {
    btn.parentElement.querySelectorAll('.grade-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
  }

  const container = document.getElementById('curriculumUnitsGrid');
  if (!container) return;

  container.innerHTML = `<div style="grid-column: 1/-1; text-align: center; padding: 2rem;">Đang tải lộ trình 105 tiết khối ${grade}...</div>`;

  try {
    const res = await fetch(`/api/curriculum/${grade}`);
    const data = await res.json();

    let html = '';
    (data.units || []).forEach((u, idx) => {
      html += `
        <div class="exam-card">
          <div class="card-top">
            <span class="tag-grade">KHỐI ${grade}</span>
            <span class="tag-duration">📘 ${u.id}</span>
          </div>
          <h3 class="card-title" style="color: #38bdf8;">${u.title}</h3>
          <p class="card-desc" style="margin-top: 0.5rem; color: #cbd5e1; font-size: 0.88rem; line-height: 1.5;">
            <b>Kiến thức trọng tâm:</b><br>${u.topics}
          </p>
          <div style="margin-top: 1rem;">
            <button type="button" class="btn btn-secondary btn-sm" style="width: 100%;" onclick="openCreatorWithUnit('${u.title}')">
              📝 Tạo Đề Cho Bài Này ➔
            </button>
          </div>
        </div>
      `;
    });
    container.innerHTML = html;
  } catch (err) {
    container.innerHTML = `<div style="color: #ef4444; padding: 2rem;">Lỗi: ${err.message}</div>`;
  }
}

function openCreatorWithUnit(unitTitle) {
  switchTeacherTab('tabCreator');
  document.getElementById('creatorTitleInput').value = `Bài Kiểm Tra - ${unitTitle}`;
}

// Khởi chạy mặc định danh sách học sinh và sổ điểm
setTimeout(() => {
  loadClassStudentsList('6A');
  loadClassGradebook('6A');
  loadCurriculumView('6');
}, 600);

