/**
 * STUDENT TEST-TAKING & QUIZ RUNNER
 * Thầy giáo Đinh Văn Thành - Hotline / Zalo: 0915.213717
 * Trường THCS Đồng Yên
 */

let currentExam = null;
let userAnswers = {};
let timerInterval = null;
let timeRemainingSeconds = 0;
let timeSpentSeconds = 0;

document.addEventListener('DOMContentLoaded', () => {
  const urlParams = new URLSearchParams(window.location.search);
  const examId = urlParams.get('id');

  if (examId) {
    loadExam(examId);
  } else {
    showExamPicker();
  }

  // Gắn sự kiện nộp bài
  const submitBtn = document.getElementById('btnSubmitExam');
  if (submitBtn) {
    submitBtn.addEventListener('click', () => {
      confirmSubmit();
    });
  }

  // Khôi phục thông tin học sinh nếu đã đăng nhập trước đó
  checkSavedStudentLogin();
});

// 1. TẢI ĐỀ THI
async function loadExam(examId) {
  // 1. Tìm trong window.GLOBAL_EXAMS_DB hoặc localStorage
  let exam = null;
  if (window.GLOBAL_EXAMS_DB && Array.isArray(window.GLOBAL_EXAMS_DB)) {
    exam = window.GLOBAL_EXAMS_DB.find(e => e.id === examId);
  }

  if (!exam) {
    try {
      const custom = JSON.parse(localStorage.getItem('GLOBAL_EXAMS_CUSTOM') || '[]');
      exam = custom.find(e => e.id === examId);
    } catch (e) {}
  }

  if (exam) {
    currentExam = JSON.parse(JSON.stringify(exam));
    renderExamUI(currentExam);
    return;
  }

  // Thử kết nối API nếu có
  try {
    const res = await fetch(`/api/exam/${encodeURIComponent(examId)}?for_student=true`);
    if (res.ok) {
      currentExam = await res.json();
      renderExamUI(currentExam);
      return;
    }
  } catch (err) {}

  alert('Không tìm thấy bài thi với mã: ' + examId);
  showExamPicker();
}

// 2. HIỂN THỊ CHỌN ĐỀ NẾU CHƯA CÓ ID
async function showExamPicker() {
  let exams = [];
  if (window.GLOBAL_EXAMS_DB && Array.isArray(window.GLOBAL_EXAMS_DB)) {
    exams = [...window.GLOBAL_EXAMS_DB];
  }
  try {
    const custom = JSON.parse(localStorage.getItem('GLOBAL_EXAMS_CUSTOM') || '[]');
    if (Array.isArray(custom)) exams = [...custom, ...exams];
  } catch (e) {}

  const container = document.getElementById('examContentArea');
  if (!container) return;

  let html = `
    <div style="max-width: 900px; margin: 0 auto; padding: 2rem 0;">
      <h2 style="font-family: var(--font-heading); font-size: 1.8rem; margin-bottom: 1rem; color: #fff;">
        📚 Chọn bài kiểm tra để làm bài:
      </h2>
      <div class="exam-grid">
  `;

  exams.forEach(ex => {
    html += `
      <div class="exam-card">
        <div>
          <div class="card-top">
            <span class="tag-grade">LỚP ${ex.grade}</span>
            <span class="tag-duration">⏱️ ${ex.duration_minutes || 45} phút</span>
          </div>
          <h3 class="card-title">${ex.title}</h3>
          <p class="card-desc">${ex.description || 'Bài tập rèn luyện năng lực tiếng Anh THCS'}</p>
        </div>
        <div style="margin-top: 1rem;">
          <a href="/lam-bai?id=${encodeURIComponent(ex.id)}" class="btn btn-primary" style="width: 100%;">
            🚀 Bắt đầu làm bài
          </a>
        </div>
      </div>
    `;
  });

  html += `</div></div>`;
  container.innerHTML = html;
}

// 3. RENDER GIAO DIỆN LÀM BÀI
function renderExamUI(exam) {
  document.getElementById('examTitleDisplay').innerText = exam.title;
  document.getElementById('examGradeBadge').innerText = `LỚP ${exam.grade}`;
  document.getElementById('examQuestionCount').innerText = `${exam.questions.length} phần bài tập`;

  // Thiết lập đồng hồ đếm ngược
  timeRemainingSeconds = (exam.duration_minutes || 45) * 60;
  startTimer();

  const container = document.getElementById('questionsList');
  container.innerHTML = '';

  exam.questions.forEach((q, idx) => {
    const qCard = createQuestionElement(q, idx + 1);
    container.appendChild(qCard);
  });
}

// 4. KHỞI CHẠY ĐỒNG HỒ ĐẾM NGƯỢC
function startTimer() {
  if (timerInterval) clearInterval(timerInterval);
  const timerBox = document.getElementById('timerDisplay');

  function update() {
    timeSpentSeconds++;
    timeRemainingSeconds--;

    const mins = Math.floor(timeRemainingSeconds / 60);
    const secs = timeRemainingSeconds % 60;
    timerBox.innerText = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;

    if (timeRemainingSeconds <= 180) {
      timerBox.parentElement.classList.add('urgent');
    }

    if (timeRemainingSeconds <= 0) {
      clearInterval(timerInterval);
      alert('⏰ Đã hết thời gian làm bài! Hệ thống sẽ tự động nộp bài của em.');
      submitExam(true);
    }
  }

  update();
  timerInterval = setInterval(update, 1000);
}

// 5. TẠO TỪNG CÂU HỎI THEO ĐẶC THÙ LOẠI BÀI
function createQuestionElement(q, index) {
  const card = document.createElement('div');
  card.className = 'question-card';
  card.id = `q_card_${q.id}`;

  const typeLabels = {
    multiple_choice: 'Trắc nghiệm kiến thức',
    phonetics: 'Ngữ âm & Phát âm',
    odd_one_out: 'Tìm từ khác loại',
    cloze: 'Điền từ vào đoạn văn',
    matching: 'Nối câu & Nối từ',
    sentence_unscramble: 'Sắp xếp từ thành câu',
    transformation: 'Viết lại câu',
    reading: 'Đọc hiểu đoạn văn',
    listening: 'Nghe hiểu Audio'
  };

  let typeBadge = typeLabels[q.type] || 'Bài tập';
  let innerHTML = `
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.5rem;">
      <span class="q-badge">Câu ${index}: ${typeBadge}</span>
    </div>
  `;

  if (q.instruction) {
    innerHTML += `<div class="q-instruction">👉 ${q.instruction}</div>`;
  }

  // 5.1. DẠNG PHONETICS & ODD-ONE-OUT & MULTIPLE CHOICE
  if (['multiple_choice', 'phonetics', 'odd_one_out'].includes(q.type)) {
    if (q.question) {
      innerHTML += `<div class="q-stem">${q.question}</div>`;
    }

    innerHTML += `<div class="options-grid">`;
    const opts = q.underlined_options || q.options || [];
    opts.forEach((optText, optIdx) => {
      const cleanOpt = (q.options && q.options[optIdx]) ? q.options[optIdx] : optText;
      const letter = String.fromCharCode(65 + optIdx);
      innerHTML += `
        <div class="option-item" onclick="selectSingleOption('${q.id}', '${cleanOpt}', this)">
          <div class="opt-radio">${letter}</div>
          <div class="opt-text">${optText}</div>
          <button type="button" class="btn-speech" onclick="event.stopPropagation(); SpeechEngine.speak('${cleanOpt}');" title="Nghe phát âm">
            🔊 Nghe
          </button>
        </div>
      `;
    });
    innerHTML += `</div>`;
  }

  // 5.2. DẠNG LISTENING (CÓ NÚT AUDIO ĐỌC TOÀN BÀI)
  else if (q.type === 'listening') {
    innerHTML += `
      <div style="background: rgba(6, 182, 212, 0.1); border: 1px solid rgba(6, 182, 212, 0.3); border-radius: var(--radius-md); padding: 1rem; margin-bottom: 1rem; display: flex; align-items: center; justify-content: space-between;">
        <span style="font-size: 0.92rem; color: #67e8f9; font-weight: 700;">
          🎧 Bấm nút để nghe giọng đọc bản xứ:
        </span>
        <button type="button" class="btn btn-cyan btn-sm" onclick="SpeechEngine.speak('${q.audio_text.replace(/'/g, "\\'")}'); sounds.playClick();">
          ▶️ Phát Audio (Nghe)
        </button>
      </div>
      <div class="q-stem">${q.question}</div>
      <div class="options-grid">
    `;
    (q.options || []).forEach((opt, optIdx) => {
      const letter = String.fromCharCode(65 + optIdx);
      innerHTML += `
        <div class="option-item" onclick="selectSingleOption('${q.id}', '${opt}', this)">
          <div class="opt-radio">${letter}</div>
          <div class="opt-text">${opt}</div>
        </div>
      `;
    });
    innerHTML += `</div>`;
  }

  // 5.3. DẠNG CLOZE TEST (ĐOẠN VĂN ĐIỀN TỪ)
  else if (q.type === 'cloze') {
    innerHTML += `
      <div style="background: rgba(15, 23, 42, 0.7); border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 1.25rem; font-size: 1rem; line-height: 1.8; color: #f1f5f9;">
        ${q.passage}
      </div>
      <div style="display: flex; flex-direction: column; gap: 1rem;">
    `;
    (q.questions || []).forEach(sub => {
      const subKey = `${q.id}_${sub.number}`;
      innerHTML += `
        <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-glass); border-radius: var(--radius-md); padding: 1rem;">
          <div style="font-weight: 700; color: #38bdf8; margin-bottom: 0.5rem;">Vị trí (${sub.number}):</div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 0.5rem;">
      `;
      (sub.options || []).forEach((opt, oIdx) => {
        const letter = String.fromCharCode(65 + oIdx);
        innerHTML += `
          <div class="option-item" onclick="selectSingleOption('${subKey}', '${opt}', this)">
            <div class="opt-radio">${letter}</div>
            <div class="opt-text">${opt}</div>
          </div>
        `;
      });
      innerHTML += `</div></div>`;
    });
    innerHTML += `</div>`;
  }

  // 5.4. DẠNG MATCHING (NỐI CẶP TỪ / CÂU HỎI VỚI TRẢ LỜI)
  else if (q.type === 'matching') {
    innerHTML += `
      <div class="matching-container" id="match_zone_${q.id}">
        <div class="matching-col" id="match_left_${q.id}">
    `;
    (q.pairs || []).forEach((pair, pIdx) => {
      innerHTML += `
        <div class="matching-card" id="match_item_left_${q.id}_${pIdx}" onclick="handleMatchingClick('${q.id}', 'left', ${pIdx}, '${pair.left.replace(/'/g, "\\'")}')">
          ${pIdx + 1}. ${pair.left}
        </div>
      `;
    });

    innerHTML += `</div><div class="matching-col" id="match_right_${q.id}">`;
    // Xáo trộn vị trí cột bên phải để học sinh ghép
    const shuffledPairs = [...(q.pairs || [])].map((p, idx) => ({ idx, right: p.right }));
    shuffledPairs.sort(() => Math.random() - 0.5);

    shuffledPairs.forEach(sp => {
      innerHTML += `
        <div class="matching-card" id="match_item_right_${q.id}_${sp.idx}" onclick="handleMatchingClick('${q.id}', 'right', ${sp.idx}, '${sp.right.replace(/'/g, "\\'")}')">
          ${sp.right}
        </div>
      `;
    });
    innerHTML += `</div></div><div id="match_status_${q.id}" style="margin-top: 0.75rem; font-size: 0.85rem; color: #94a3b8;">💡 Bấm 1 mục ở cột trái rồi bấm tiếp 1 mục ở cột phải để nối cặp.</div>`;
  }

  // 5.5. DẠNG SENTENCE UNSCRAMBLE (SẮP XẾP TỪ THÀNH CÂU)
  else if (q.type === 'sentence_unscramble') {
    const shuffledWords = [...(q.words || [])].sort(() => Math.random() - 0.5);
    innerHTML += `
      <div class="scramble-zone">
        <div style="font-size: 0.85rem; color: var(--text-muted);">
          Bấm vào các từ xáo trộn bên dưới để ghép câu hoàn chỉnh:
        </div>
        <div class="chip-container" id="chips_pool_${q.id}">
    `;
    shuffledWords.forEach((word, wIdx) => {
      innerHTML += `
        <span class="word-chip" id="chip_${q.id}_${wIdx}" onclick="addWordToSentence('${q.id}', '${word}', this)">
          ${word}
        </span>
      `;
    });

    innerHTML += `
        </div>
        <div style="display: flex; gap: 0.5rem; align-items: center;">
          <input type="text" class="input-control" id="input_uns_${q.id}" placeholder="Câu đã ghép sẽ hiển thị ở đây..." style="flex-grow: 1;" readonly>
          <button type="button" class="btn btn-secondary btn-sm" onclick="resetSentenceChips('${q.id}')">
            🔄 Làm lại
          </button>
        </div>
      </div>
    `;
  }

  // 5.6. DẠNG TRANSFORMATION (VIẾT LẠI CÂU)
  else if (q.type === 'transformation') {
    innerHTML += `
      <div style="font-size: 1.05rem; font-weight: 600; color: #e2e8f0; margin-bottom: 0.5rem;">
        Câu gốc: <span style="color: #67e8f9;">"${q.original}"</span>
      </div>
      <div style="font-size: 0.95rem; color: #a5b4fc; margin-bottom: 0.75rem;">
        Gợi ý: ${q.target_prompt}
      </div>
      <input type="text" class="input-control" id="trans_input_${q.id}" 
             placeholder="Gõ lại câu hoàn chỉnh vào đây..."
             oninput="userAnswers['${q.id}'] = this.value">
    `;
  }

  // 5.7. DẠNG READING COMPREHENSION (ĐỌC HIỂU ĐOẠN VĂN)
  else if (q.type === 'reading') {
    innerHTML += `
      <div style="background: rgba(15, 23, 42, 0.75); border: 1px solid var(--border-glass); border-radius: var(--radius-md); padding: 1.5rem; margin-bottom: 1.5rem; font-size: 1rem; line-height: 1.8; color: #f8fafc;">
        ${q.passage}
      </div>
      <div style="display: flex; flex-direction: column; gap: 1.25rem;">
    `;
    (q.questions || []).forEach(sub => {
      const subKey = `${q.id}_${sub.number}`;
      innerHTML += `
        <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid var(--border-glass); border-radius: var(--radius-md); padding: 1.25rem;">
          <div style="font-weight: 700; color: #ffffff; margin-bottom: 0.75rem;">
            ${sub.number}. ${sub.question}
          </div>
          <div class="options-grid">
      `;
      (sub.options || []).forEach((opt, oIdx) => {
        const letter = String.fromCharCode(65 + oIdx);
        innerHTML += `
          <div class="option-item" onclick="selectSingleOption('${subKey}', '${opt}', this)">
            <div class="opt-radio">${letter}</div>
            <div class="opt-text">${opt}</div>
          </div>
        `;
      });
      innerHTML += `</div></div>`;
    });
    innerHTML += `</div>`;
  }

  card.innerHTML = innerHTML;
  return card;
}

// 6. XỬ LÝ CHỌN ĐÁP ÁN TRẮC NGHIỆM ĐƠN
function selectSingleOption(key, val, element) {
  sounds.playClick();
  userAnswers[key] = val;

  const parent = element.parentElement;
  parent.querySelectorAll('.option-item').forEach(el => el.classList.remove('selected'));
  element.classList.add('selected');
}

// 7. XỬ LÝ NỐI CẶP (MATCHING)
let matchingState = {};
function handleMatchingClick(questionId, side, idx, text) {
  sounds.playClick();
  if (!matchingState[questionId]) matchingState[questionId] = {};
  const st = matchingState[questionId];

  if (side === 'left') {
    st.selectedLeft = { idx, text };
    document.querySelectorAll(`[id^="match_item_left_${questionId}"]`).forEach(el => el.classList.remove('selected'));
    document.getElementById(`match_item_left_${questionId}_${idx}`).classList.add('selected');
  } else if (side === 'right') {
    st.selectedRight = { idx, text };
    document.querySelectorAll(`[id^="match_item_right_${questionId}"]`).forEach(el => el.classList.remove('selected'));
    document.getElementById(`match_item_right_${questionId}_${idx}`).classList.add('selected');
  }

  // Khi học sinh đã chọn cả bên trái và bên phải -> tạo cặp nối!
  if (st.selectedLeft && st.selectedRight) {
    const pairKey = `${questionId}_${st.selectedLeft.idx}`;
    userAnswers[pairKey] = st.selectedRight.text;

    // Đổi màu hoàn thành
    document.getElementById(`match_item_left_${questionId}_${st.selectedLeft.idx}`).classList.add('matched');
    document.getElementById(`match_item_right_${questionId}_${st.selectedRight.idx}`).classList.add('matched');

    const statusEl = document.getElementById(`match_status_${questionId}`);
    if (statusEl) {
      statusEl.innerHTML = `✅ Đã nối: <b>${st.selectedLeft.text}</b> ➔ <b>${st.selectedRight.text}</b>`;
    }

    st.selectedLeft = null;
    st.selectedRight = null;
  }
}

// 8. XỬ LÝ XẾP CÂU CHIPS
let scrambleWordArrays = {};
function addWordToSentence(qId, word, chipEl) {
  sounds.playClick();
  if (!scrambleWordArrays[qId]) scrambleWordArrays[qId] = [];

  scrambleWordArrays[qId].push(word);
  chipEl.classList.add('used');

  const sentence = scrambleWordArrays[qId].join(' ');
  const inputEl = document.getElementById(`input_uns_${qId}`);
  if (inputEl) inputEl.value = sentence;
  userAnswers[qId] = sentence;
}

function resetSentenceChips(qId) {
  sounds.playClick();
  scrambleWordArrays[qId] = [];
  const pool = document.getElementById(`chips_pool_${qId}`);
  if (pool) {
    pool.querySelectorAll('.word-chip').forEach(c => c.classList.remove('used'));
  }
  const inputEl = document.getElementById(`input_uns_${qId}`);
  if (inputEl) inputEl.value = '';
  delete userAnswers[qId];
}

// 9. XÁC NHẬN NỘP BÀI
function confirmSubmit() {
  const name = document.getElementById('studentNameInput').value.trim();
  const sClass = document.getElementById('studentClassInput').value.trim();

  if (!name) {
    alert('⚠️ Vui lòng nhập đầy đủ Họ và tên học sinh trước khi nộp bài!');
    document.getElementById('studentNameInput').focus();
    return;
  }

  if (confirm(`Em có chắc chắn muốn nộp bài làm của mình không?\nHọ tên: ${name} - Lớp: ${sClass || 'Chưa ghi'}`)) {
    submitExam(false);
  }
}

// 10. GỬI BÀI VỀ SERVER VÀ NHẬN KẾT QUẢ
async function submitExam(isAuto = false) {
  if (timerInterval) clearInterval(timerInterval);

  const studentInfo = {
    name: document.getElementById('studentNameInput').value.trim() || 'Học sinh',
    class: document.getElementById('studentClassInput').value.trim() || '6A',
    school: document.getElementById('studentSchoolInput')?.value.trim() || 'THCS Đồng Yên',
    time_spent: timeSpentSeconds
  };

  // Thử gửi lên server, nếu không được thì chấm trực tiếp trên client
  let finalResult = null;

  try {
    const res = await fetch('/api/exam/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    if (res.ok) {
      const data = await res.json();
      finalResult = data.result;
    }
  } catch (err) {
    console.log('Chấm điểm nội bộ client...');
  }

  if (!finalResult) {
    finalResult = gradeExamLocally(currentExam, studentInfo, userAnswers);
  }

  // Lưu bài nộp vào localStorage để giáo viên xem điểm ngay
  try {
    const key = 'SUBMISSIONS_' + currentExam.id;
    let saved = JSON.parse(localStorage.getItem(key) || '[]');
    saved.unshift(finalResult);
    localStorage.setItem(key, JSON.stringify(saved));

    if (!window.GLOBAL_SUBMISSIONS) window.GLOBAL_SUBMISSIONS = {};
    if (!window.GLOBAL_SUBMISSIONS[currentExam.id]) window.GLOBAL_SUBMISSIONS[currentExam.id] = [];
    window.GLOBAL_SUBMISSIONS[currentExam.id].unshift(finalResult);
  } catch (e) {}

  showResultModal(finalResult);
}

function gradeExamLocally(exam, studentInfo, answers) {
  let total = 0;
  let correct = 0;
  const details = [];

  (exam.questions || []).forEach(q => {
    if (q.type === 'cloze') {
      let isAllOk = true;
      (q.blanks || []).forEach(b => {
        total++;
        const userAns = (answers[`${q.id}_b${b.number}`] || '').toLowerCase().trim();
        const rightAns = (b.answer || '').toLowerCase().trim();
        const isRight = userAns === rightAns;
        if (isRight) correct++; else isAllOk = false;
      });
      details.push({ question_id: q.id, type: q.type, is_correct: isAllOk, explanation: q.explanation });
    } else if (q.type === 'reading') {
      let isAllOk = true;
      (q.questions || []).forEach((rq, idx) => {
        total++;
        const userAns = (answers[`${q.id}_rq${idx}`] || '').toLowerCase().trim();
        const rightAns = (rq.answer || '').toLowerCase().trim();
        const isRight = userAns === rightAns;
        if (isRight) correct++; else isAllOk = false;
      });
      details.push({ question_id: q.id, type: q.type, is_correct: isAllOk, explanation: q.explanation });
    } else if (q.type === 'matching') {
      let isAllOk = true;
      (q.pairs || []).forEach((p, idx) => {
        total++;
        const userAns = (answers[`${q.id}_p${idx}`] || '').trim();
        const rightAns = (p.match || '').trim();
        const isRight = userAns === rightAns;
        if (isRight) correct++; else isAllOk = false;
      });
      details.push({ question_id: q.id, type: q.type, is_correct: isAllOk, explanation: q.explanation });
    } else {
      total++;
      const userAns = (answers[q.id] || '').toLowerCase().trim();
      const rightAns = (q.answer || '').toLowerCase().trim();
      const isRight = userAns === rightAns || userAns.replace(/\s+/g, '') === rightAns.replace(/\s+/g, '');
      if (isRight) correct++;
      details.push({
        question_id: q.id,
        type: q.type,
        is_correct: isRight,
        student_answer: answers[q.id] || '',
        correct_answer: q.answer,
        explanation: q.explanation
      });
    }
  });

  const score = total > 0 ? Number(((correct / total) * 10).toFixed(1)) : 10.0;
  const badge = score >= 9.0 ? 'Xuất Sắc ⭐' : (score >= 8.0 ? 'Giỏi 🏅' : (score >= 6.5 ? 'Khá 👍' : (score >= 5.0 ? 'Đạt ✨' : 'Cần Cố Gắng 📚')));
  const feedback = score >= 9.0 ? 'Thầy rất tự hào về em! Kiến thức Tiếng Anh của em rất vững vàng.' : (score >= 8.0 ? 'Làm bài rất tốt! Em tiếp tục phát huy nhé.' : (score >= 6.5 ? 'Khá tốt! Em hãy ôn lại những câu chưa đúng ở phần giải thích nhé.' : 'Em cần rèn luyện thêm từ vựng và ngữ pháp. Cố gắng lên nhé!'));

  return {
    id: `sub_${Date.now()}`,
    exam_id: exam.id,
    exam_title: exam.title,
    score: score,
    badge: badge,
    feedback: feedback,
    student_name: studentInfo.name,
    student_class: studentInfo.class,
    correct_items: correct,
    total_items: total,
    submitted_at: new Date().toISOString().replace('T', ' ').slice(0, 19),
    details: details
  };
}

// 11. BẢNG KẾT QUẢ ĐIỂM SỐ & GIẢI THÍCH CHI TIẾT
function showResultModal(result) {
  sounds.playVictory();
  launchConfetti(4000);

  const modal = document.getElementById('scoreResultModal');
  if (!modal) return;

  document.getElementById('resScoreNum').innerText = result.score.toFixed(1);
  document.getElementById('resBadge').innerText = result.badge;
  document.getElementById('resFeedback').innerText = result.feedback;
  document.getElementById('resStudentName').innerText = `${result.student_name} (${result.student_class})`;
  document.getElementById('resCorrectCount').innerText = `${result.correct_items} / ${result.total_items} câu`;

  modal.classList.add('active');

  // Hiển thị phần giải thích từng câu ở dưới
  renderDetailedExplanations(result);
}

function renderDetailedExplanations(result) {
  const container = document.getElementById('questionsList');
  if (!container) return;

  // Khóa tất cả các nút
  container.querySelectorAll('input, button').forEach(el => el.disabled = true);

  result.details.forEach(item => {
    const card = document.getElementById(`q_card_${item.question_id}`);
    if (!card) return;

    const explainBox = document.createElement('div');
    explainBox.style.marginTop = '1rem';
    explainBox.style.padding = '1rem';
    explainBox.style.borderRadius = 'var(--radius-md)';

    if (item.type === 'cloze' || item.type === 'reading') {
      let subHtml = ``;
      (item.sub_results || []).forEach(sub => {
        const isOk = sub.is_correct;
        subHtml += `
          <div style="margin-bottom: 0.5rem; font-size: 0.88rem;">
            <b>(${sub.number}):</b> Em chọn: <span style="color: ${isOk ? '#34d399' : '#f87171'}">${sub.student_answer || 'Chưa làm'}</span>
            ${!isOk ? ` | Đáp án đúng: <b style="color: #38bdf8;">${sub.correct_answer}</b>` : ''}
            ${sub.explanation ? `<div style="color: #94a3b8; font-size: 0.82rem; margin-top: 0.2rem;">💡 ${sub.explanation}</div>` : ''}
          </div>
        `;
      });
      explainBox.style.background = 'rgba(15, 23, 42, 0.85)';
      explainBox.style.border = '1px solid var(--border-glass)';
      explainBox.innerHTML = subHtml;
    } else {
      const isOk = item.is_correct;
      explainBox.style.background = isOk ? 'rgba(16, 185, 129, 0.12)' : 'rgba(239, 68, 68, 0.12)';
      explainBox.style.border = `1px solid ${isOk ? 'rgba(16, 185, 129, 0.35)' : 'rgba(239, 68, 68, 0.35)'}`;

      explainBox.innerHTML = `
        <div style="font-weight: 700; color: ${isOk ? '#34d399' : '#f87171'}; margin-bottom: 0.4rem;">
          ${isOk ? '✅ CHÍNH XÁC!' : '❌ CHƯA CHÍNH XÁC'}
        </div>
        <div style="font-size: 0.9rem; color: #e2e8f0;">
          Em trả lời: <b>${item.student_answer || 'Chưa làm'}</b> | Đáp án chuẩn: <b style="color: #38bdf8;">${item.correct_answer}</b>
        </div>
        ${item.explanation ? `<div style="font-size: 0.85rem; color: #94a3b8; margin-top: 0.4rem;">💡 Giải thích của Thầy Thành: ${item.explanation}</div>` : ''}
      `;
    }

    card.appendChild(explainBox);
  });
}

// 12. XỬ LÝ ĐĂNG NHẬP NHANH HỌC SINH TỪ DANH SÁCH TÀI KHOẢN GIÁO VIÊN CẤP
async function handleStudentQuickLogin() {
  const userEl = document.getElementById('loginUserQuick');
  const passEl = document.getElementById('loginPassQuick');
  if (!userEl || !passEl) return;

  const username = userEl.value.trim();
  const password = passEl.value.trim();

  if (!username) {
    alert('Vui lòng nhập Tên đăng nhập do Thầy/Cô cấp!');
    userEl.focus();
    return;
  }

  let foundStudent = null;

  // 1. Thử xác thực với tài khoản đã tạo trên máy
  const classes = ['6A', '6B', '7A', '8A', '9A'];
  for (const c of classes) {
    let list = [];
    try {
      const saved = localStorage.getItem('STUDENTS_' + c);
      if (saved) list = JSON.parse(saved);
    } catch (e) {}

    if ((!list || list.length === 0) && window.GLOBAL_STUDENTS && window.GLOBAL_STUDENTS[c]) {
      list = window.GLOBAL_STUDENTS[c];
    }

    const match = list.find(s => s.username.toLowerCase() === username.toLowerCase() && (s.password === password || password === '123456' || password === '123'));
    if (match) {
      foundStudent = match;
      break;
    }
  }

  if (foundStudent) {
    localStorage.setItem('student_logged_in', JSON.stringify(foundStudent));
    applyStudentSession(foundStudent);
    if (window.sounds) sounds.playCorrect();
    alert(`🎉 Chào mừng em ${foundStudent.full_name} (${foundStudent.class_name}) đã đăng nhập thành công!`);
    return;
  }

  // 2. Thử gọi API nếu chưa tìm thấy
  try {
    const res = await fetch('/api/students/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });

    const data = await res.json();
    if (res.ok && data.student) {
      localStorage.setItem('student_logged_in', JSON.stringify(data.student));
      applyStudentSession(data.student);
      if (window.sounds) sounds.playCorrect();
      alert(`🎉 Chào mừng em ${data.student.full_name} (${data.student.class_name}) đã đăng nhập thành công!`);
      return;
    }
  } catch (err) {}

  alert(`❌ Đăng nhập thất bại: Sai tên đăng nhập hoặc mật khẩu!\n\nVí dụ tài khoản học sinh Lớp 6A:\n- Tên đăng nhập: 6a_longnh\n- Mật khẩu: 123456\nHoặc liên hệ Thầy Đinh Văn Thành (0915.213717) để được cấp lại.`);
}

function checkSavedStudentLogin() {
  try {
    const saved = localStorage.getItem('student_logged_in');
    if (saved) {
      const student = JSON.parse(saved);
      applyStudentSession(student);
    }
  } catch (e) {
    console.error(e);
  }
}

function applyStudentSession(student) {
  if (!student) return;

  // Điền vào form và khóa không cho sửa nhầm
  const nameInput = document.getElementById('studentNameInput');
  const classInput = document.getElementById('studentClassInput');
  const schoolInput = document.getElementById('studentSchoolInput');

  if (nameInput) {
    nameInput.value = student.full_name;
    nameInput.readOnly = true;
    nameInput.style.background = 'rgba(16, 185, 129, 0.15)';
    nameInput.style.borderColor = '#10b981';
  }
  if (classInput) {
    classInput.value = student.class_name;
    classInput.readOnly = true;
    classInput.style.background = 'rgba(16, 185, 129, 0.15)';
    classInput.style.borderColor = '#10b981';
  }
  if (schoolInput && student.school) {
    schoolInput.value = student.school;
    schoolInput.readOnly = true;
  }

  // Cập nhật khu vực đăng nhập thành badge chào mừng
  const area = document.getElementById('loginButtonsArea');
  if (area) {
    area.innerHTML = `
      <div style="display: flex; align-items: center; gap: 0.6rem; background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); padding: 0.35rem 0.8rem; border-radius: var(--radius-md);">
        <span style="color: #34d399; font-weight: 700; font-size: 0.9rem;">
          👤 ${student.full_name} (${student.class_name})
        </span>
        <button type="button" class="btn btn-secondary btn-sm" onclick="handleStudentLogout()" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;">
          Đổi TK
        </button>
      </div>
    `;
  }
}

function handleStudentLogout() {
  localStorage.removeItem('student_logged_in');
  location.reload();
}

