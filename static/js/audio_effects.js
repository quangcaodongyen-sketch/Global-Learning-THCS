/**
 * AUDIO EFFECTS & WEB SPEECH SYNTHESIS ENGINE
 * Thầy giáo Đinh Văn Thành - Hotline / Zalo: 0915.213717
 * 100% Native Web Audio API - Hoạt động độc lập không cần file mp3 hay mạng internet
 */

class SoundEngine {
  constructor() {
    this.ctx = null;
  }

  _init() {
    if (!this.ctx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioContext();
    }
    if (this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  }

  // Âm thanh click phím bấm nhẹ nhàng
  playClick() {
    try {
      this._init();
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(600, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(800, this.ctx.currentTime + 0.04);
      gain.gain.setValueAtTime(0.08, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.04);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.04);
    } catch (e) {}
  }

  // Âm thanh trả lời đúng (Ding chimes)
  playCorrect() {
    try {
      this._init();
      const now = this.ctx.currentTime;
      [523.25, 659.25, 783.99, 1046.50].forEach((freq, i) => {
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(freq, now + i * 0.08);
        gain.gain.setValueAtTime(0.12, now + i * 0.08);
        gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.08 + 0.25);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now + i * 0.08);
        osc.stop(now + i * 0.08 + 0.25);
      });
    } catch (e) {}
  }

  // Âm thanh trả lời sai (Buzzer)
  playWrong() {
    try {
      this._init();
      const now = this.ctx.currentTime;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(180, now);
      osc.frequency.linearRampToValueAtTime(110, now + 0.2);
      gain.gain.setValueAtTime(0.12, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.2);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(now);
      osc.stop(now + 0.2);
    } catch (e) {}
  }

  // Âm thanh vinh quang nộp bài hoàn thành (Victory Fanfare)
  playVictory() {
    try {
      this._init();
      const now = this.ctx.currentTime;
      const notes = [
        { f: 523.25, t: 0.0, d: 0.15 },
        { f: 523.25, t: 0.15, d: 0.15 },
        { f: 523.25, t: 0.3, d: 0.15 },
        { f: 659.25, t: 0.45, d: 0.35 },
        { f: 783.99, t: 0.8, d: 0.2 },
        { f: 1046.50, t: 1.0, d: 0.6 }
      ];
      notes.forEach(n => {
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(n.f, now + n.t);
        gain.gain.setValueAtTime(0.18, now + n.t);
        gain.gain.exponentialRampToValueAtTime(0.001, now + n.t + n.d);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now + n.t);
        osc.stop(now + n.t + n.d);
      });
    } catch (e) {}
  }

  // Âm thanh quay bánh xe (Wheel tick)
  playTick() {
    try {
      this._init();
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'square';
      osc.frequency.setValueAtTime(800, this.ctx.currentTime);
      gain.gain.setValueAtTime(0.05, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.02);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.02);
    } catch (e) {}
  }
}

// BỘ ĐỌC PHÁT ÂM TIẾNG ANH CHUẨN NATIVE BẰNG WEB SPEECH API
class SpeechEngine {
  static speak(text, lang = 'en-US', rate = 0.9) {
    if (!('speechSynthesis' in window)) {
      alert("Trình duyệt không hỗ trợ phát âm tự động Web Speech!");
      return;
    }
    window.speechSynthesis.cancel();
    const cleanText = text.replace(/<[^>]*>/g, '').trim();
    const utterance = new SpeechSynthesisUtterance(cleanText);
    utterance.lang = lang;
    utterance.rate = rate; // Đọc với tốc độ vừa phải cho học sinh THCS dễ nghe
    
    // Tìm giọng đọc tiếng Anh hay nhất
    const voices = window.speechSynthesis.getVoices();
    const enVoice = voices.find(v => v.lang.includes('en-US') || v.lang.includes('en-GB'));
    if (enVoice) {
      utterance.voice = enVoice;
    }
    
    window.speechSynthesis.speak(utterance);
  }
}

const sounds = new SoundEngine();
