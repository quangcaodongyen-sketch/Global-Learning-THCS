/**
 * FUN INTERACTIVE GAMES ARENA FOR SECONDARY STUDENTS (GRADES 6 - 9)
 * Thầy giáo Đinh Văn Thành - Hotline / Zalo: 0915.213717
 * 1. Lucky Vocab Wheel (Vòng quay may mắn)
 * 2. English Millionaire (Ai là triệu phú Tiếng Anh)
 * 3. Speed Word Match (Đua ghép cặp từ vựng)
 * 4. Sentence Builder Puzzle (Xếp câu thông minh)
 */

let currentGameGrade = '6';
let currentActiveGame = 'wheel';

document.addEventListener('DOMContentLoaded', () => {
  const urlParams = new URLSearchParams(window.location.search);
  const grade = urlParams.get('grade') || '6';
  const game = urlParams.get('game') || 'wheel';

  currentGameGrade = grade;
  currentActiveGame = game;

  initGameTabs();
  launchGame(game, grade);
});

function initGameTabs() {
  document.querySelectorAll('.game-nav-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.game-nav-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const gameType = btn.getAttribute('data-game');
      currentActiveGame = gameType;
      launchGame(gameType, currentGameGrade);
    });
  });

  document.querySelectorAll('.game-grade-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.game-grade-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const g = btn.getAttribute('data-grade');
      currentGameGrade = g;
      launchGame(currentActiveGame, g);
    });
  });
}

function launchGame(gameType, grade) {
  document.querySelectorAll('.game-view-panel').forEach(p => p.style.display = 'none');
  const panel = document.getElementById(`panel_${gameType}`);
  if (panel) panel.style.display = 'block';

  if (gameType === 'wheel') initLuckyWheel(grade);
  else if (gameType === 'millionaire') initMillionaire(grade);
  else if (gameType === 'speed_match') initSpeedMatch(grade);
  else if (gameType === 'puzzle') initSentencePuzzle(grade);
}

/* =========================================================================
   1. LUCKY VOCAB WHEEL (VÒNG QUAY MAY MẮN)
   ========================================================================= */
let wheelItems = [];
let wheelAngle = 0;
let isSpinning = false;
let wheelScoreXP = 0;

async function initLuckyWheel(grade) {
  try {
    const res = await fetch(`/api/games/lucky_wheel/${grade}`);
    const resData = await res.json();
    wheelItems = resData.data || [];
    drawWheel();
  } catch (err) {
    console.error(err);
  }
}

function drawWheel() {
  const canvas = document.getElementById('wheelCanvas');
  if (!canvas || wheelItems.length === 0) return;

  const ctx = canvas.getContext('2d');
  const size = canvas.width;
  const center = size / 2;
  const radius = center - 15;
  const sliceAngle = (2 * Math.PI) / wheelItems.length;

  ctx.clearRect(0, 0, size, size);

  const colors = ['#6366f1', '#06b6d4', '#10b981', '#f59e0b', '#ec4899', '#8b5cf6', '#3b82f6', '#14b8a6'];

  ctx.save();
  ctx.translate(center, center);
  ctx.rotate(wheelAngle);

  for (let i = 0; i < wheelItems.length; i++) {
    const angleStart = i * sliceAngle;
    const angleEnd = angleStart + sliceAngle;

    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.arc(0, 0, radius, angleStart, angleEnd);
    ctx.fillStyle = colors[i % colors.length];
    ctx.fill();
    ctx.strokeStyle = '#ffffff';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Vẽ chữ
    ctx.save();
    ctx.rotate(angleStart + sliceAngle / 2);
    ctx.textAlign = 'right';
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 15px Plus Jakarta Sans, sans-serif';
    ctx.shadowColor = 'rgba(0,0,0,0.6)';
    ctx.shadowBlur = 4;
    ctx.fillText(wheelItems[i].word, radius - 20, 6);
    ctx.restore();
  }

  // Vẽ tâm tròn
  ctx.beginPath();
  ctx.arc(0, 0, 28, 0, 2 * Math.PI);
  ctx.fillStyle = '#0f172a';
  ctx.fill();
  ctx.strokeStyle = '#38bdf8';
  ctx.lineWidth = 4;
  ctx.stroke();

  ctx.restore();
}

function spinWheel() {
  if (isSpinning || wheelItems.length === 0) return;
  isSpinning = true;
  sounds.playClick();

  const extraSpins = 5 + Math.random() * 4;
  const totalRotation = extraSpins * 2 * Math.PI + Math.random() * 2 * Math.PI;
  const duration = 4000;
  const start = performance.now();
  const initialAngle = wheelAngle;

  let lastTickAngle = 0;

  function animate(now) {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);
    // Easing cubic out
    const easeOut = 1 - Math.pow(1 - progress, 3);
    wheelAngle = initialAngle + totalRotation * easeOut;

    // Phát âm thanh tiếng bánh xe lách cách
    if (Math.abs(wheelAngle - lastTickAngle) > 0.4) {
      sounds.playTick();
      lastTickAngle = wheelAngle;
    }

    drawWheel();

    if (progress < 1) {
      requestAnimationFrame(animate);
    } else {
      isSpinning = false;
      determineWheelResult();
    }
  }

  requestAnimationFrame(animate);
}

function determineWheelResult() {
  const sliceAngle = (2 * Math.PI) / wheelItems.length;
  // Con trỏ ở đỉnh (270 độ / 3PI/2)
  let normalized = (3 * Math.PI / 2 - (wheelAngle % (2 * Math.PI))) % (2 * Math.PI);
  if (normalized < 0) normalized += 2 * Math.PI;

  const winningIndex = Math.floor(normalized / sliceAngle) % wheelItems.length;
  const winner = wheelItems[winningIndex];

  sounds.playCorrect();
  SpeechEngine.speak(winner.word);

  showWheelChallengeModal(winner);
}

function showWheelChallengeModal(item) {
  const modal = document.getElementById('wheelChallengeModal');
  if (!modal) return;

  document.getElementById('wheelWordTitle').innerText = `${item.word} ${item.phonetic}`;
  document.getElementById('wheelWordMeaning').innerText = `Nghĩa: ${item.meaning}`;
  document.getElementById('wheelChallengeQuestion').innerText = item.challenge;

  const optsContainer = document.getElementById('wheelChallengeOptions');
  optsContainer.innerHTML = '';

  item.options.forEach(opt => {
    const btn = document.createElement('div');
    btn.className = 'option-item';
    btn.style.marginBottom = '0.5rem';
    btn.innerHTML = `<span style="font-weight: 700;">${opt}</span>`;
    btn.onclick = () => {
      if (opt === item.answer) {
        sounds.playCorrect();
        launchConfetti(2000);
        wheelScoreXP += item.points || 100;
        document.getElementById('wheelScoreDisplay').innerText = `${wheelScoreXP} XP`;
        alert(`🎉 CHÍNH XÁC! Em được cộng +${item.points} XP!`);
      } else {
        sounds.playWrong();
        alert(`❌ Rất tiếc! Đáp án đúng là: ${item.answer}`);
      }
      modal.classList.remove('active');
    };
    optsContainer.appendChild(btn);
  });

  modal.classList.add('active');
}

/* =========================================================================
   2. ENGLISH MILLIONAIRE (AI LÀ TRIỆU PHÚ TIẾNG ANH)
   ========================================================================= */
let millionaireQuestions = [];
let currentMillionaireIdx = 0;
let used5050 = false;
let usedAudience = false;

async function initMillionaire(grade) {
  try {
    const res = await fetch(`/api/games/millionaire/${grade}`);
    const resData = await res.json();
    millionaireQuestions = resData.data || [];
    currentMillionaireIdx = 0;
    used5050 = false;
    usedAudience = false;
    renderMillionaireQuestion();
  } catch (err) {
    console.error(err);
  }
}

function renderMillionaireQuestion() {
  if (currentMillionaireIdx >= millionaireQuestions.length) {
    sounds.playVictory();
    launchConfetti(5000);
    alert('🏆 XUẤT SẮC! Em đã chinh phục đỉnh cao Ai Là Triệu Phú Tiếng Anh THCS!');
    return;
  }

  const q = millionaireQuestions[currentMillionaireIdx];
  document.getElementById('milLevelDisplay').innerText = `Câu ${q.level} / ${millionaireQuestions.length}`;
  document.getElementById('milRewardDisplay').innerText = `$${q.reward} Điểm`;
  document.getElementById('milQuestionText').innerText = q.question;

  const optsContainer = document.getElementById('milOptionsContainer');
  optsContainer.innerHTML = '';

  q.options.forEach((opt, idx) => {
    const letter = String.fromCharCode(65 + idx);
    const item = document.createElement('div');
    item.className = 'option-item';
    item.id = `mil_opt_${idx}`;
    item.innerHTML = `
      <div class="opt-radio">${letter}</div>
      <div class="opt-text" style="font-weight: 700;">${opt}</div>
    `;
    item.onclick = () => handleMillionaireAnswer(opt, q.answer, item);
    optsContainer.appendChild(item);
  });
}

function handleMillionaireAnswer(selected, correct, el) {
  sounds.playClick();
  el.classList.add('selected');

  setTimeout(() => {
    if (selected === correct) {
      sounds.playCorrect();
      el.style.background = 'rgba(16, 185, 129, 0.4)';
      el.style.borderColor = '#10b981';
      setTimeout(() => {
        currentMillionaireIdx++;
        renderMillionaireQuestion();
      }, 1000);
    } else {
      sounds.playWrong();
      el.style.background = 'rgba(239, 68, 68, 0.4)';
      el.style.borderColor = '#ef4444';
      alert(`❌ Sai rồi! Đáp án đúng là: ${correct}. Em hãy thử sức lại nhé!`);
      currentMillionaireIdx = 0;
      renderMillionaireQuestion();
    }
  }, 700);
}

function useLifeline5050() {
  if (used5050) return;
  sounds.playClick();
  used5050 = true;
  document.getElementById('btn5050').style.opacity = '0.3';
  document.getElementById('btn5050').style.pointerEvents = 'none';

  const q = millionaireQuestions[currentMillionaireIdx];
  const wrongIndices = [];
  q.options.forEach((opt, idx) => {
    if (opt !== q.answer) wrongIndices.push(idx);
  });

  // Ẩn 2 phương án sai ngẫu nhiên
  wrongIndices.sort(() => Math.random() - 0.5);
  wrongIndices.slice(0, 2).forEach(idx => {
    const el = document.getElementById(`mil_opt_${idx}`);
    if (el) el.style.visibility = 'hidden';
  });
}

function useLifelineAudience() {
  if (usedAudience) return;
  sounds.playClick();
  usedAudience = true;
  document.getElementById('btnAudience').style.opacity = '0.3';
  document.getElementById('btnAudience').style.pointerEvents = 'none';

  const q = millionaireQuestions[currentMillionaireIdx];
  alert(`📊 Ý kiến 100 khán giả trong trường quay:\nCó tới 85% khán giả bình chọn phương án: "${q.answer}"!`);
}

/* =========================================================================
   3. SPEED WORD MATCH (ĐUA GHÉP CẶP TỪ VỰNG TỐC ĐỘ)
   ========================================================================= */
let matchPairsData = [];
let matchSelectedLeft = null;
let matchSelectedRight = null;
let matchScore = 0;
let matchStreak = 0;

async function initSpeedMatch(grade) {
  try {
    const res = await fetch(`/api/games/speed_match/${grade}`);
    const resData = await res.json();
    matchPairsData = resData.data || [];
    renderSpeedMatchUI();
  } catch (err) {
    console.error(err);
  }
}

function renderSpeedMatchUI() {
  const leftCol = document.getElementById('speedMatchLeft');
  const rightCol = document.getElementById('speedMatchRight');
  if (!leftCol || !rightCol) return;

  leftCol.innerHTML = '';
  rightCol.innerHTML = '';
  matchScore = 0;
  matchStreak = 0;
  document.getElementById('speedMatchScore').innerText = `${matchScore} đ`;

  matchPairsData.forEach((p, idx) => {
    const elLeft = document.createElement('div');
    elLeft.className = 'matching-card';
    elLeft.id = `sm_l_${idx}`;
    elLeft.innerText = p.en;
    elLeft.onclick = () => {
      sounds.playClick();
      SpeechEngine.speak(p.en);
      leftCol.querySelectorAll('.matching-card').forEach(c => c.classList.remove('selected'));
      elLeft.classList.add('selected');
      matchSelectedLeft = { idx, en: p.en };
      checkSpeedMatch();
    };
    leftCol.appendChild(elLeft);
  });

  const shuffledRight = [...matchPairsData].map((p, idx) => ({ idx, vi: p.vi }));
  shuffledRight.sort(() => Math.random() - 0.5);

  shuffledRight.forEach(sp => {
    const elRight = document.createElement('div');
    elRight.className = 'matching-card';
    elRight.id = `sm_r_${sp.idx}`;
    elRight.innerText = sp.vi;
    elRight.onclick = () => {
      sounds.playClick();
      rightCol.querySelectorAll('.matching-card').forEach(c => c.classList.remove('selected'));
      elRight.classList.add('selected');
      matchSelectedRight = { idx: sp.idx, vi: sp.vi };
      checkSpeedMatch();
    };
    rightCol.appendChild(elRight);
  });
}

function checkSpeedMatch() {
  if (matchSelectedLeft && matchSelectedRight) {
    if (matchSelectedLeft.idx === matchSelectedRight.idx) {
      sounds.playCorrect();
      matchStreak++;
      matchScore += 100 * matchStreak;
      document.getElementById('speedMatchScore').innerText = `${matchScore} đ (Combo x${matchStreak} 🔥)`;

      document.getElementById(`sm_l_${matchSelectedLeft.idx}`).classList.add('matched');
      document.getElementById(`sm_r_${matchSelectedRight.idx}`).classList.add('matched');

      matchSelectedLeft = null;
      matchSelectedRight = null;

      // Kiểm tra hoàn thành tất cả các cặp
      const unmatched = document.querySelectorAll('#speedMatchLeft .matching-card:not(.matched)');
      if (unmatched.length === 0) {
        sounds.playVictory();
        launchConfetti(3000);
        alert(`🎉 XUẤT SẮC! Em đã hoàn thành toàn bộ bảng ghép cặp với ${matchScore} điểm!`);
      }
    } else {
      sounds.playWrong();
      matchStreak = 0;
      document.getElementById('speedMatchScore').innerText = `${matchScore} đ`;
      matchSelectedLeft = null;
      matchSelectedRight = null;
      document.querySelectorAll('.matching-card.selected').forEach(c => c.classList.remove('selected'));
    }
  }
}

/* =========================================================================
   4. SENTENCE BUILDER PUZZLE (XẾP CÂU THÔNG MINH)
   ========================================================================= */
let puzzleSentences = [];
let puzzleCurrentIdx = 0;
let puzzleCurrentAssembled = [];

async function initSentencePuzzle(grade) {
  try {
    const res = await fetch(`/api/games/sentence_puzzle/${grade}`);
    const resData = await res.json();
    puzzleSentences = resData.data || [];
    puzzleCurrentIdx = 0;
    renderPuzzleSentence();
  } catch (err) {
    console.error(err);
  }
}

function renderPuzzleSentence() {
  if (puzzleCurrentIdx >= puzzleSentences.length) {
    sounds.playVictory();
    launchConfetti(4000);
    alert('🎉 XUẤT SẮC! Em đã hoàn thành tất cả các câu thử thách xếp câu!');
    return;
  }

  const item = puzzleSentences[puzzleCurrentIdx];
  puzzleCurrentAssembled = [];

  document.getElementById('puzzleVietnameseClue').innerText = `Dịch câu: "${item.vietnamese}"`;
  document.getElementById('puzzleAssembledSentence').value = '';

  const chipsContainer = document.getElementById('puzzleChipsPool');
  chipsContainer.innerHTML = '';

  const shuffled = [...item.words].sort(() => Math.random() - 0.5);
  shuffled.forEach((w, wIdx) => {
    const chip = document.createElement('span');
    chip.className = 'word-chip';
    chip.innerText = w;
    chip.onclick = () => {
      sounds.playClick();
      puzzleCurrentAssembled.push(w);
      chip.classList.add('used');
      document.getElementById('puzzleAssembledSentence').value = puzzleCurrentAssembled.join(' ');
    };
    chipsContainer.appendChild(chip);
  });
}

function verifySentencePuzzle() {
  const item = puzzleSentences[puzzleCurrentIdx];
  const target = item.words.join(' ').trim();
  const assembled = puzzleCurrentAssembled.join(' ').trim();

  if (assembled.toLowerCase() === target.toLowerCase()) {
    sounds.playCorrect();
    SpeechEngine.speak(target);
    launchConfetti(2000);
    alert('🎉 CHÍNH XÁC! Câu văn của em hoàn toàn đúng ngữ pháp!');
    puzzleCurrentIdx++;
    renderPuzzleSentence();
  } else {
    sounds.playWrong();
    alert(`❌ Chưa chính xác! Câu đúng là:\n"${target}"`);
    resetCurrentSentencePuzzle();
  }
}

function resetCurrentSentencePuzzle() {
  puzzleCurrentAssembled = [];
  document.getElementById('puzzleAssembledSentence').value = '';
  document.querySelectorAll('#puzzleChipsPool .word-chip').forEach(c => c.classList.remove('used'));
}
