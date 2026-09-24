/**
 * GLOBAL LEARNING AI - SPEECH RECOGNITION & PRONUNCIATION TRAINER
 * Thầy giáo Đinh Văn Thành - Hotline / Zalo: 0915.213717
 * Trường THCS Đồng Yên
 */

let recognition = null;
let isRecording = false;
let currentTargetSentence = null;
let activeSpeakerCardId = null;

// Khởi tạo Speech Recognition
function initSpeechEngine() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    console.warn("Trình duyệt không hỗ trợ Web Speech Recognition API");
    return null;
  }

  const rec = new SpeechRecognition();
  rec.continuous = false;
  rec.interimResults = false;
  rec.lang = 'en-US';

  rec.onstart = () => {
    isRecording = true;
    updateMicUI(true);
  };

  rec.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    const confidence = event.results[0][0].confidence;
    handleStudentSpeechResult(transcript, confidence);
  };

  rec.onerror = (event) => {
    console.error("Speech Recognition Error:", event.error);
    isRecording = false;
    updateMicUI(false);
    if (event.error === 'not-allowed') {
      alert("⚠️ Vui lòng cấp quyền truy cập Microphone trong trình duyệt để luyện nói Tiếng Anh!");
    } else if (event.error === 'no-speech') {
      alert("⚠️ Hệ thống chưa nghe rõ giọng của em. Hãy bấm lại nút Micro và nói to rõ hơn nhé!");
    }
  };

  rec.onend = () => {
    isRecording = false;
    updateMicUI(false);
  };

  return rec;
}

// 1. PHÁT ÂM MẪU BẢN XỨ (TTS) VỚI ĐIỀU CHỈNH TỐC ĐỘ
function speakNativeModel(text, rate = 1.0) {
  if (!('speechSynthesis' in window)) {
    alert("Trình duyệt không hỗ trợ tổng hợp giọng nói.");
    return;
  }
  window.speechSynthesis.cancel();

  const utter = new SpeechSynthesisUtterance(text);
  utter.rate = rate;
  utter.pitch = 1.0;
  utter.lang = 'en-US';

  // Tìm voice chuẩn tiếng Anh US hoặc UK
  const voices = window.speechSynthesis.getVoices();
  const enVoice = voices.find(v => (v.lang === 'en-US' || v.lang === 'en-GB') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Samantha') || v.name.includes('David')));
  if (enVoice) utter.voice = enVoice;

  window.speechSynthesis.speak(utter);
}

// 2. BẮT ĐẦU THU ÂM VÀ CHẤM ĐIỂM
function startSpeakingChallenge(sentenceId, targetText) {
  if (!recognition) {
    recognition = initSpeechEngine();
  }

  if (!recognition) {
    alert("Trình duyệt của bạn hiện chưa bật Web Speech API. Hãy sử dụng Google Chrome, Edge hoặc Cốc Cốc để trải nghiệm tính năng này!");
    return;
  }

  if (isRecording) {
    recognition.stop();
    return;
  }

  currentTargetSentence = {
    id: sentenceId,
    targetText: targetText
  };
  activeSpeakerCardId = sentenceId;

  try {
    recognition.start();
  } catch (e) {
    console.error(e);
  }
}

function updateMicUI(recording) {
  if (!activeSpeakerCardId) return;
  const card = document.getElementById(`speak_card_${activeSpeakerCardId}`);
  if (!card) return;

  const btnMic = card.querySelector('.btn-mic-record');
  if (btnMic) {
    if (recording) {
      btnMic.classList.add('recording-pulse');
      btnMic.innerHTML = `🛑 Đang nghe em nói...`;
    } else {
      btnMic.classList.remove('recording-pulse');
      btnMic.innerHTML = `🎙️ Bấm Để Luyện Nói`;
    }
  }
}

// 3. SO KHỚP VÀ TÍNH ĐỘ CHÍNH XÁC PHÁT ÂM (%)
function handleStudentSpeechResult(transcript, confidence) {
  if (!currentTargetSentence) return;

  const target = currentTargetSentence.targetText.toLowerCase().replace(/[^a-z0-9 ]/g, '').trim();
  const spoken = transcript.toLowerCase().replace(/[^a-z0-9 ]/g, '').trim();

  const score = calculateSentenceAccuracy(target, spoken);
  const resultCard = document.getElementById(`result_box_${currentTargetSentence.id}`);

  // Cập nhật XP và Streak
  updateStudentStats(score);

  if (resultCard) {
    resultCard.style.display = 'block';
    let feedbackBadge = '';
    let badgeClass = '';

    if (score >= 90) {
      feedbackBadge = '🌟 XUẤT SẮC! PHÁT ÂM CHUẨN BẢN XỨ (NATIVE ACCENT)';
      badgeClass = 'score-badge-perfect';
      if (window.sounds) sounds.playVictory();
      if (window.launchConfetti) launchConfetti(3000);
    } else if (score >= 70) {
      feedbackBadge = '👏 RẤT TỐT! NGỮ ĐIỆU RẤT TỰ NHIÊN';
      badgeClass = 'score-badge-good';
      if (window.sounds) sounds.playCorrect();
    } else {
      feedbackBadge = '💪 CỐ GẮNG LÊN! HÃY NGHE LẠI MẪU VÀ NÓI CHẬM HƠN NHÉ';
      badgeClass = 'score-badge-try';
      if (window.sounds) sounds.playWrong();
    }

    resultCard.innerHTML = `
      <div class="accuracy-score-banner ${badgeClass}">
        <div style="font-size: 1.5rem; font-weight: 900;">${score}% CHÍNH XÁC</div>
        <div style="font-size: 0.9rem; font-weight: 700; margin-top: 0.25rem;">${feedbackBadge}</div>
      </div>
      <div style="margin-top: 0.75rem; font-size: 0.95rem; line-height: 1.6;">
        <span style="color: var(--text-muted);">AI ghi nhận em đã nói:</span><br>
        <span style="color: #38bdf8; font-weight: 800; font-size: 1.05rem;">"${transcript}"</span>
      </div>
      <div style="margin-top: 0.5rem; font-size: 0.85rem; color: #a5b4fc;">
        ${renderWordComparison(target, spoken)}
      </div>
    `;
  }
}

// Thuật toán so sánh từng từ
function calculateSentenceAccuracy(target, spoken) {
  const targetWords = target.split(/\s+/);
  const spokenWords = spoken.split(/\s+/);

  if (targetWords.length === 0) return 0;

  let matched = 0;
  targetWords.forEach(tw => {
    if (spokenWords.includes(tw)) {
      matched++;
    }
  });

  let rawPercent = Math.round((matched / targetWords.length) * 100);
  // Nếu có từ tương tự gần đúng
  if (rawPercent < 100 && target.length > 0) {
    const editDist = levenshteinDistance(target, spoken);
    const maxLen = Math.max(target.length, spoken.length);
    const simPercent = Math.round((1 - editDist / maxLen) * 100);
    rawPercent = Math.max(rawPercent, simPercent);
  }

  return Math.min(100, Math.max(0, rawPercent));
}

function levenshteinDistance(a, b) {
  const m = a.length, n = b.length;
  const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));
  for (let i = 0; i <= m; i++) dp[i][0] = i;
  for (let j = 0; j <= n; j++) dp[0][j] = j;

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (a[i - 1] === b[j - 1]) dp[i][j] = dp[i - 1][j - 1];
      else dp[i][j] = 1 + Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]);
    }
  }
  return dp[m][n];
}

function renderWordComparison(target, spoken) {
  const targetWords = target.split(/\s+/);
  const spokenWords = spoken.split(/\s+/);

  let html = `<div style="display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.4rem;">`;
  targetWords.forEach(word => {
    const isMatched = spokenWords.includes(word);
    html += `
      <span style="padding: 0.2rem 0.5rem; border-radius: 6px; font-weight: 700; font-size: 0.85rem; 
        background: ${isMatched ? 'rgba(16, 185, 129, 0.2)' : 'rgba(244, 63, 94, 0.2)'}; 
        color: ${isMatched ? '#34d399' : '#fb7185'}; 
        border: 1px solid ${isMatched ? 'rgba(16, 185, 129, 0.4)' : 'rgba(244, 63, 94, 0.4)'};">
        ${isMatched ? '✓' : '✗'} ${word}
      </span>
    `;
  });
  html += `</div>`;
  return html;
}

// 4. QUẢN LÝ XP VÀ STREAK NGÀY HỌC
function updateStudentStats(score) {
  try {
    let xp = parseInt(localStorage.getItem('gs_xp') || '0', 10);
    let streak = parseInt(localStorage.getItem('gs_streak') || '1', 10);

    let earnedXp = Math.round(score / 5);
    xp += earnedXp;

    localStorage.setItem('gs_xp', xp.toString());
    localStorage.setItem('gs_streak', streak.toString());

    renderGlobalStatsHeader();
  } catch (e) {
    console.error(e);
  }
}

function renderGlobalStatsHeader() {
  const xpEl = document.getElementById('userTotalXp');
  const streakEl = document.getElementById('userStreakDays');
  if (xpEl) {
    const xp = localStorage.getItem('gs_xp') || '120';
    xpEl.innerText = `${xp} XP`;
  }
  if (streakEl) {
    const streak = localStorage.getItem('gs_streak') || '3';
    streakEl.innerText = `${streak} Ngày 🔥`;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  renderGlobalStatsHeader();
});
