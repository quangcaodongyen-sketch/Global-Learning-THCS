/**
 * GLOBAL LEARNING THCS - DỮ LIỆU LUYỆN NÓI & PHÁT ÂM TIẾNG ANH (LỚP 6 - 9)
 * Thầy giáo Đinh Văn Thành - Hotline / Zalo: 0915.213717
 * Trường THCS Đồng Yên
 */

const SPEAKING_TOPICS = {
  "6": [
    {
      unit: "Unit 1: My New School",
      title: "Giới thiệu trường học & Đồ dùng học tập",
      icon: "🏫",
      sentences: [
        {
          id: "s_g6_u1_1",
          text: "I go to a new secondary school in the town.",
          ipa: "/aɪ ɡəʊ tuː ə njuː ˈsekəndri skuːl ɪn ðə taʊn/",
          meaning: "Tôi học tại một trường trung học cơ sở mới ở thị trấn.",
          tips: "Chú ý nối âm 'go to a' và âm /s/ trong 'school'."
        },
        {
          id: "s_g6_u1_2",
          text: "My favourite subject at school is English.",
          ipa: "/maɪ ˈfeɪvərɪt ˈsʌbdʒɪkt æt skuːl ɪz ˈɪŋɡlɪʃ/",
          meaning: "Môn học yêu thích của tôi ở trường là môn Tiếng Anh.",
          tips: "Bật rõ âm đuôi /ʃ/ trong từ 'English'."
        },
        {
          id: "s_g6_u1_3",
          text: "I always put my calculator and pencil sharpener in my bag.",
          ipa: "/aɪ ˈɔːlweɪz pʊt maɪ ˈkælkjuleɪtər ænd ˈpensl ˈʃɑːpnər ɪn maɪ bæɡ/",
          meaning: "Tôi luôn để máy tính và gọt bút chì vào trong cặp sách.",
          tips: "Trọng âm của 'calculator' rơi vào âm tiết đầu tiên."
        }
      ]
    },
    {
      unit: "Unit 2: My House",
      title: "Miêu tả ngôi nhà & Phòng ốc",
      icon: "🏡",
      sentences: [
        {
          id: "s_g6_u2_1",
          text: "There is a cosy living room and a modern kitchen in my house.",
          ipa: "/ðeər ɪz ə ˈkəʊzi ˈlɪvɪŋ ruːm ænd ə ˈmɒdn ˈkɪtʃɪn ɪn maɪ haʊs/",
          meaning: "Có một phòng khách ấm cúng và một căn bếp hiện đại trong nhà tôi.",
          tips: "Âm /ð/ trong 'There' đặt lưỡi giữa hai hàm răng."
        },
        {
          id: "s_g6_u2_2",
          text: "My bedroom has a big window overlooking a beautiful garden.",
          ipa: "/maɪ ˈbedruːm hæz ə bɪɡ ˈwɪndəʊ ˌəʊvəˈlʊkɪŋ ə ˈbjuːtɪfl ˈɡɑːdn/",
          meaning: "Phòng ngủ của tôi có một cửa sổ lớn nhìn ra khu vườn tuyệt đẹp.",
          tips: "Nhấn trọng âm từ 'beautiful' và 'bedroom'."
        }
      ]
    },
    {
      unit: "Unit 5: Natural Wonders of Viet Nam",
      title: "Kỳ quan thiên nhiên Việt Nam",
      icon: "🏞️",
      sentences: [
        {
          id: "s_g6_u5_1",
          text: "Ha Long Bay is one of the most famous natural wonders in the world.",
          ipa: "/hɑː lɒŋ beɪ ɪz wʌn əv ðə məʊst ˈfeɪməs ˈnætʃrəl ˈwʌndəz ɪn ðə wɜːld/",
          meaning: "Vịnh Hạ Long là một trong những kỳ quan thiên nhiên nổi tiếng nhất thế giới.",
          tips: "Phát âm chuẩn từ 'natural' /ˈnætʃrəl/ và 'wonders' /ˈwʌndəz/."
        },
        {
          id: "s_g6_u5_2",
          text: "You must bring suncream and a waterproof jacket when travelling.",
          ipa: "/juː mʌst brɪŋ ˈsʌnkriːm ænd ə ˈwɔːtəpruːf ˈdʒækɪt wen ˈtrævlɪŋ/",
          meaning: "Bạn phải mang theo kem chống nắng và áo khoác chống nước khi đi du lịch.",
          tips: "Âm /ʌ/ trong 'must' và 'suncream'."
        }
      ]
    }
  ],
  "7": [
    {
      unit: "Unit 1: Hobbies",
      title: "Sở thích & Lối sống lành mạnh",
      icon: "🎨",
      sentences: [
        {
          id: "s_g7_u1_1",
          text: "My hobby is making models and collecting unique stamps.",
          ipa: "/maɪ ˈhɒbi ɪz ˈmeɪkɪŋ ˈmɒdlz ænd kəˈlektɪŋ juˈniːk stæmps/",
          meaning: "Sở thích của tôi là làm mô hình và sưu tập những con tem độc đáo.",
          tips: "Trọng âm từ 'unique' rơi vào âm tiết thứ hai /juˈniːk/."
        },
        {
          id: "s_g7_u1_2",
          text: "Doing regular exercise helps you stay in good shape and keep fit.",
          ipa: "/ˈduːɪŋ ˈreɡjələr ˈeksəsaɪz helps juː steɪ ɪn ɡʊd ʃeɪp ænd kiːp fɪt/",
          meaning: "Tập thể dục thường xuyên giúp bạn giữ được vóc dáng và khỏe mạnh.",
          tips: "Âm /ʃ/ trong 'shape' và âm /fɪt/ dứt khoát."
        }
      ]
    },
    {
      unit: "Unit 10: Energy Sources",
      title: "Nguồn năng lượng tương lai",
      icon: "⚡",
      sentences: [
        {
          id: "s_g7_u10_1",
          text: "Solar energy and wind power are renewable and clean sources of energy.",
          ipa: "/ˈsəʊlər ˈenədʒi ænd wɪnd ˈpaʊər ɑː rɪˈnjuːəbl ænd kliːn ˈsɔːsɪz əv ˈenədʒi/",
          meaning: "Năng lượng mặt trời và năng lượng gió là những nguồn năng lượng tái tạo và sạch.",
          tips: "Lưu ý từ 'renewable' /rɪˈnjuːəbl/."
        }
      ]
    }
  ],
  "8": [
    {
      unit: "Unit 1: Leisure Time",
      title: "Thời gian rảnh rỗi & Giải trí",
      icon: "⚽",
      sentences: [
        {
          id: "s_g8_u1_1",
          text: "I am really keen on skateboarding and hanging out with my close friends.",
          ipa: "/aɪ æm ˈrɪəli kiːn ɒn ˈskeɪtbɔːdɪŋ ænd ˈhæŋɪŋ aʊt wɪð maɪ kləʊs frendz/",
          meaning: "Tôi rất thích trượt ván và đi chơi cùng những người bạn thân.",
          tips: "Cụm 'keen on' mang nghĩa say mê, hào hứng."
        },
        {
          id: "s_g8_u1_2",
          text: "Spending too much screen time may cause eye problems and laziness.",
          ipa: "/ˈspendɪŋ tuː mʌtʃ skriːn taɪm meɪ kɔːz aɪ ˈprɒbləmz ænd ˈleɪzinəs/",
          meaning: "Dành quá nhiều thời gian trước màn hình có thể gây hại cho mắt và lười biếng.",
          tips: "Trọng âm 'laziness' rơi vào âm 1."
        }
      ]
    },
    {
      unit: "Unit 7: Environmental Protection",
      title: "Bảo vệ môi trường sinh thái",
      icon: "🌱",
      sentences: [
        {
          id: "s_g8_u7_1",
          text: "We should reduce single-use plastic bags to protect marine life.",
          ipa: "/wiː ʃʊd rɪˈdjuːs ˈsɪŋɡl juːs ˈplæstɪk bæɡz tuː prəˈtekt məˈriːn laɪf/",
          meaning: "Chúng ta nên giảm túi nilon dùng một lần để bảo vệ sinh vật biển.",
          tips: "Âm /iː/ trong 'marine' /məˈriːn/."
        }
      ]
    }
  ],
  "9": [
    {
      unit: "Unit 1: Local Community",
      title: "Cộng đồng địa phương & Làng nghề truyền thống",
      icon: "🏘️",
      sentences: [
        {
          id: "s_g9_u1_1",
          text: "Skilled artisans in the pottery village pass their craft down from generation to generation.",
          ipa: "/skɪld ˈɑːtɪzænz ɪn ðə ˈpɒtəri ˈvɪlɪdʒ pɑːs ðeər krɑːft daʊn frəm ˌdʒenəˈreɪʃn tuː ˌdʒenəˈreɪʃn/",
          meaning: "Các nghệ nhân lành nghề trong làng gốm truyền nghề từ thế hệ này sang thế hệ khác.",
          tips: "Cụm 'pass down' nghĩa là truyền lại cho đời sau."
        },
        {
          id: "s_g9_u1_2",
          text: "Community helpers like firefighters and doctors play an important role in our daily lives.",
          ipa: "/kəˈmjuːnəti ˈhelpəz laɪk ˈfaɪəfaɪtəz ænd ˈdɒktəz pleɪ ən ɪmˈpɔːtnt rəʊl ɪn ˈaʊər ˈdeɪli laɪvz/",
          meaning: "Những người giúp đỡ cộng đồng như lính cứu hỏa và bác sĩ đóng vai trò rất quan trọng.",
          tips: "Lưu ý nối âm 'play an important role in'."
        }
      ]
    },
    {
      unit: "Unit 9: English in the World",
      title: "Tiếng Anh là ngôn ngữ toàn cầu",
      icon: "🌐",
      sentences: [
        {
          id: "s_g9_u9_1",
          text: "English has become the global lingua franca for international trade, science, and education.",
          ipa: "/ˈɪŋɡlɪʃ hæz bɪˈkʌm ðə ˈɡləʊbl ˌlɪŋɡwə ˈfræŋkə fɔːr ˌɪntəˈnæʃnəl treɪd ˈsaɪəns ænd ˌedʒuˈkeɪʃn/",
          meaning: "Tiếng Anh đã trở thành ngôn ngữ chung toàn cầu trong thương mại quốc tế, khoa học và giáo dục.",
          tips: "Thuật ngữ 'lingua franca' nghĩa là ngôn ngữ giao tiếp chung."
        }
      ]
    }
  ]
};

// FLASHCARDS TỪ VỰNG ĐA GIÁC QUAN
const FLASHCARDS_DATA = {
  "6": [
    { word: "Compass", pos: "n", ipa: "/ˈkʌmpəs/", meaning: "Cái com-pa (dụng cụ vẽ hình tròn)", example: "You need a compass to draw a perfect circle." },
    { word: "Calculator", pos: "n", ipa: "/ˈkælkjuleɪtər/", meaning: "Máy tính cầm tay bỏ túi", example: "We use calculators during maths lessons." },
    { word: "Neighbourhood", pos: "n", ipa: "/ˈneɪbəhʊd/", meaning: "Khu vực lân cận, hàng xóm láng giềng", example: "There is a big supermarket in my neighbourhood." },
    { word: "Wonder", pos: "n", ipa: "/ˈwʌndər/", meaning: "Kỳ quan, điều kỳ diệu", example: "Ha Long Bay is a famous natural wonder." },
    { word: "Uniform", pos: "n", ipa: "/ˈjuːnɪfɔːm/", meaning: "Bộ đồng phục học sinh", example: "All students wear white uniforms on Mondays." },
    { word: "Confident", pos: "adj", ipa: "/ˈkɒnfɪdənt/", meaning: "Tự tin, quyết đoán", example: "She is confident when speaking English in public." }
  ],
  "7": [
    { word: "Community", pos: "n", ipa: "/kəˈmjuːnəti/", meaning: "Cộng đồng dân cư", example: "Volunteers do a lot of good deeds for the community." },
    { word: "Renewable", pos: "adj", ipa: "/rɪˈnjuːəbl/", meaning: "Có thể tái tạo (năng lượng)", example: "Wind and sunlight are renewable energy sources." },
    { word: "Volunteer", pos: "n, v", ipa: "/ˌvɒlənˈtɪər/", meaning: "Tình nguyện viên / Đi làm tình nguyện", example: "We volunteer to clean up the local river." },
    { word: "Nutritious", pos: "adj", ipa: "/njuːˈtrɪʃəs/", meaning: "Bổ dưỡng, giàu dinh dưỡng", example: "Fresh fruits and vegetables provide nutritious meals." }
  ],
  "8": [
    { word: "Leisure", pos: "n", ipa: "/ˈleʒər/", meaning: "Thì giờ rỗi rãi, giải trí", example: "Reading books is my favourite leisure activity." },
    { word: "Biodiversity", pos: "n", ipa: "/ˌbaɪəʊdaɪˈvɜːsəti/", meaning: "Đa dạng sinh học", example: "Deforestation threatens the local biodiversity." },
    { word: "Tradition", pos: "n", ipa: "/trəˈdɪʃn/", meaning: "Truyền thống, phong tục", example: "It is a tradition to visit grandparents on Tet holiday." },
    { word: "Technology", pos: "n", ipa: "/tekˈnɒlədʒi/", meaning: "Công nghệ hiện đại", example: "Modern technology helps students learn English faster." }
  ],
  "9": [
    { word: "Artisan", pos: "n", ipa: "/ˈɑːtɪzæn/", meaning: "Nghệ nhân, thợ thủ công lành nghề", example: "The artisan shaped the ceramic pot with his hands." },
    { word: "Lingua Franca", pos: "n", ipa: "/ˌlɪŋɡwə ˈfræŋkə/", meaning: "Ngôn ngữ chung toàn cầu", example: "English is used as the global lingua franca." },
    { word: "Preserve", pos: "v", ipa: "/prɪˈzɜːv/", meaning: "Bảo tồn, gìn giữ", example: "We must preserve our historical monuments." },
    { word: "Multilingual", pos: "adj", ipa: "/ˌmʌltiˈlɪŋɡwəl/", meaning: "Biết và nói được nhiều thứ tiếng", example: "She is multilingual and speaks four languages fluently." }
  ]
};
