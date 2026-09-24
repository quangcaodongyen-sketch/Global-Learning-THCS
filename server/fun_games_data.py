# -*- coding: utf-8 -*-
"""
DỮ LIỆU CÁC TRÒ CHƠI BÀI TẬP THÚ VỊ CHO HỌC SINH THCS (LỚP 6 - 9)
Tác giả: Thầy giáo Đinh Văn Thành - Hotline / Zalo: 0915.213717
Bao gồm:
1. Vòng quay từ vựng may mắn (Lucky Vocab Wheel)
2. Ai là triệu phú Tiếng Anh (English Millionaire)
3. Đua ghép cặp từ vựng tốc độ (Speed Word Match)
4. Xếp câu thông minh (Sentence Builder Puzzle)
"""

GAMES_DATA = {
    # 1. LUCKY VOCAB WHEEL
    "lucky_wheel": {
        "6": [
            {"word": "Compass", "phonetic": "/ˈkʌm.pəs/", "meaning": "Cái com-pa", "challenge": "What do you use a compass for?", "options": ["Drawing circles", "Cutting paper", "Erasing pencil marks"], "answer": "Drawing circles", "points": 100},
            {"word": "Neighbourhood", "phonetic": "/ˈneɪ.bə.hʊd/", "meaning": "Khu dân cư lân cận", "challenge": "A neighbourhood is...", "options": ["An area where people live near each other", "A school subject", "A kind of pet"], "answer": "An area where people live near each other", "points": 150},
            {"word": "Creative", "phonetic": "/kriˈeɪ.tɪv/", "meaning": "Sáng tạo", "challenge": "A creative person...", "options": ["Has lots of original ideas", "Sleeps all day", "Hates drawing"], "answer": "Has lots of original ideas", "points": 120},
            {"word": "Natural Wonder", "phonetic": "/ˈnætʃ.ər.əl ˈwʌn.dər/", "meaning": "Kỳ quan thiên nhiên", "challenge": "Which one is a natural wonder?", "options": ["Ha Long Bay", "Keangnam Tower", "Smart TV"], "answer": "Ha Long Bay", "points": 200},
            {"word": "Recycle", "phonetic": "/ˌriːˈsaɪ.kəl/", "meaning": "Tái chế", "challenge": "The 3Rs stand for Reduce, Reuse and...", "options": ["Recycle", "Remove", "Repeat"], "answer": "Recycle", "points": 180},
            {"word": "Solar Energy", "phonetic": "/ˈsəʊ.lər ˈen.ə.dʒi/", "meaning": "Năng lượng mặt trời", "challenge": "Solar energy comes from...", "options": ["The sun", "Underground oil", "River water"], "answer": "The sun", "points": 150}
        ],
        "7": [
            {"word": "Community Service", "phonetic": "/kəˈmjuː.nə.ti ˈsɜː.vɪs/", "meaning": "Hoạt động vì cộng đồng", "challenge": "An example of community service is...", "options": ["Cleaning up city parks", "Playing video games", "Staying up late"], "answer": "Cleaning up city parks", "points": 120},
            {"word": "Volunteer", "phonetic": "/ˌvɒl.ənˈtɪər/", "meaning": "Tình nguyện viên", "challenge": "Volunteers work...", "options": ["Without being paid to help others", "For high salaries only", "To sell products"], "answer": "Without being paid to help others", "points": 150},
            {"word": "Documentary", "phonetic": "/ˌdɒk.jəˈmen.tər.i/", "meaning": "Phim tài liệu", "challenge": "A documentary provides...", "options": ["Factual information about real events", "Magical fairy tales", "Cartoon jokes"], "answer": "Factual information about real events", "points": 160},
            {"word": "Renewable", "phonetic": "/rɪˈnjuː.ə.bəl/", "meaning": "Có thể tái tạo", "challenge": "Which energy source is renewable?", "options": ["Wind power", "Coal", "Natural gas"], "answer": "Wind power", "points": 180},
            {"word": "Traffic Jam", "phonetic": "/ˈtræf.ɪk dʒæm/", "meaning": "Tắc nghẽn giao thông", "challenge": "Traffic jams usually happen during...", "options": ["Rush hours", "Midnight", "Noon on Sundays"], "answer": "Rush hours", "points": 140},
            {"word": "Origami", "phonetic": "/ˌɒr.ɪˈɡɑː.mi/", "meaning": "Nghệ thuật gấp giấy", "challenge": "Origami is the traditional art of...", "options": ["Folding paper", "Making ceramics", "Painting walls"], "answer": "Folding paper", "points": 200}
        ],
        "8": [
            {"word": "Metropolis", "phonetic": "/məˈtrɒp.əl.ɪs/", "meaning": "Đô thị khổng lồ", "challenge": "A metropolis is...", "options": ["A very large and bustling city", "A tiny quiet village", "A farm animal"], "answer": "A very large and bustling city", "points": 150},
            {"word": "Terrace Fields", "phonetic": "/ˈter.əs fiːldz/", "meaning": "Ruộng bậc thang", "challenge": "Terrace fields are usually carved into...", "options": ["Steep mountainsides", "Deep ocean floors", "Sandy beaches"], "answer": "Steep mountainsides", "points": 180},
            {"word": "Earthquake", "phonetic": "/ˈɜːθ.kweɪk/", "meaning": "Trận động đất", "challenge": "During an earthquake, you should...", "options": ["Take cover under a sturdy desk", "Run near glass windows", "Use elevators"], "answer": "Take cover under a sturdy desk", "points": 200},
            {"word": "Habitable", "phonetic": "/ˈhæb.ɪ.tə.bəl/", "meaning": "Có thể sinh sống được", "challenge": "A habitable planet has...", "options": ["Water and breathable air", "Poisonous acid rivers", "No atmosphere"], "answer": "Water and breathable air", "points": 220},
            {"word": "Costume", "phonetic": "/ˈkɒs.tjuːm/", "meaning": "Trang phục truyền thống", "challenge": "Ethnic minorities wear traditional costumes during...", "options": ["Festivals and celebrations", "Sleeping time only", "Car washing"], "answer": "Festivals and celebrations", "points": 140}
        ],
        "9": [
            {"word": "Artisan", "phonetic": "/ˌɑː.tɪˈzæn/", "meaning": "Nghệ nhân", "challenge": "An artisan is a person who...", "options": ["Makes skilled crafts by hand", "Pilots an airplane", "Scores football goals"], "answer": "Makes skilled crafts by hand", "points": 160},
            {"word": "Preserve", "phonetic": "/prɪˈzɜːv/", "meaning": "Bảo tồn, gìn giữ", "challenge": "To preserve cultural heritage means to...", "options": ["Keep it safe from dying out", "Throw it away", "Sell it cheaply"], "answer": "Keep it safe from dying out", "points": 180},
            {"word": "Ecotourism", "phonetic": "/ˈiː.kəʊˌtʊə.rɪ.zəm/", "meaning": "Du lịch sinh thái", "challenge": "Ecotourism aims to...", "options": ["Protect natural habitats and help locals", "Build skyscrapers in jungles", "Hunt wild animals"], "answer": "Protect natural habitats and help locals", "points": 200},
            {"word": "Lingua Franca", "phonetic": "/ˌlɪŋ.ɡwə ˈfræŋ.kə/", "meaning": "Ngôn ngữ chung thế giới", "challenge": "English is widely used as a global...", "options": ["Lingua franca", "Secret code", "Ancient dead tongue"], "answer": "Lingua franca", "points": 250},
            {"word": "Hands-on", "phonetic": "/ˌhændzˈɒn/", "meaning": "Trải nghiệm thực tế", "challenge": "A hands-on workshop allows students to...", "options": ["Practice and create things themselves", "Listen quietly with no action", "Read magazines"], "answer": "Practice and create things themselves", "points": 170}
        ]
    },

    # 2. ENGLISH MILLIONAIRE (AI LÀ TRIỆU PHÚ)
    "millionaire": {
        "6": [
            {"level": 1, "reward": "100", "question": "What is the capital city of Viet Nam?", "options": ["Ha Noi", "Da Nang", "Ho Chi Minh City", "Can Tho"], "answer": "Ha Noi"},
            {"level": 2, "reward": "200", "question": "Which word is a school item?", "options": ["Ruler", "Elephant", "Television", "Sofa"], "answer": "Ruler"},
            {"level": 3, "reward": "300", "question": "How many days are there in a normal week?", "options": ["Seven", "Five", "Six", "Eight"], "answer": "Seven"},
            {"level": 4, "reward": "500", "question": "Students ________ uniform on school days.", "options": ["wear", "wears", "wearing", "to wear"], "answer": "wear"},
            {"level": 5, "reward": "1,000", "question": "Look! The cat ________ on the wall.", "options": ["is sleeping", "sleeps", "slept", "sleep"], "answer": "is sleeping"},
            {"level": 6, "reward": "2,000", "question": "Which one is the opposite of 'friendly'?", "options": ["Unfriendly", "Helpful", "Kind", "Active"], "answer": "Unfriendly"},
            {"level": 7, "reward": "4,000", "question": "Da Nang is ________ than Hai Phong.", "options": ["more modern", "modern", "most modern", "modernier"], "answer": "more modern"},
            {"level": 8, "reward": "8,000", "question": "There isn't ________ orange juice in the bottle.", "options": ["any", "some", "many", "a"], "answer": "any"},
            {"level": 9, "reward": "16,000", "question": "Ha Long Bay is in ________ Province.", "options": ["Quang Ninh", "Lao Cai", "Phu Tho", "Binh Dinh"], "answer": "Quang Ninh"},
            {"level": 10, "reward": "32,000", "question": "Which robot ability means 'có thể nâng vật nặng'?", "options": ["Lift heavy objects", "Make coffee", "Sing karaoke", "Draw pictures"], "answer": "Lift heavy objects"}
        ],
        "7": [
            {"level": 1, "reward": "100", "question": "Which of these is a healthy activity?", "options": ["Doing morning exercise", "Eating too much fast food", "Sleeping 2 hours a day", "Watching TV all night"], "answer": "Doing morning exercise"},
            {"level": 2, "reward": "200", "question": "He enjoys ________ stamps in his free time.", "options": ["collecting", "collect", "collected", "collects"], "answer": "collecting"},
            {"level": 3, "reward": "300", "question": "Classical music is not as ________ as rock music.", "options": ["loud", "louder", "loudest", "more loud"], "answer": "loud"},
            {"level": 4, "reward": "500", "question": "We ________ old warm clothes to poor children last month.", "options": ["donated", "donate", "will donate", "are donating"], "answer": "donated"},
            {"level": 5, "reward": "1,000", "question": "Lan ________ ride a bicycle to school when she was 7.", "options": ["used to", "uses to", "is used", "use"], "answer": "used to"},
            {"level": 6, "reward": "2,000", "question": "Solar energy is generated from ________.", "options": ["The sun", "Underground gas", "Coal mines", "Gasoline"], "answer": "The sun"},
            {"level": 7, "reward": "4,000", "question": "________ it was raining, the football match continued.", "options": ["Although", "Because", "Despite", "However"], "answer": "Although"},
            {"level": 8, "reward": "8,000", "question": "Which country is an English-speaking country?", "options": ["New Zealand", "Japan", "Brazil", "France"], "answer": "New Zealand"},
            {"level": 9, "reward": "16,000", "question": "What is the main purpose of community service?", "options": ["To help society and develop empathy", "To make big money", "To pass exams easily", "To skip classes"], "answer": "To help society and develop empathy"},
            {"level": 10, "reward": "32,000", "question": "Which festival features glowing pumpkins and trick-or-treating?", "options": ["Halloween", "Easter", "Thanksgiving", "Christmas"], "answer": "Halloween"}
        ],
        "8": [
            {"level": 1, "reward": "100", "question": "Life in the countryside is generally ________ than in city centers.", "options": ["more peaceful", "peaceful", "peacefuller", "most peaceful"], "answer": "more peaceful"},
            {"level": 2, "reward": "200", "question": "Students are keen ________ learning digital technology.", "options": ["on", "in", "at", "about"], "answer": "on"},
            {"level": 3, "reward": "300", "question": "While she was doing homework, the telephone ________.", "options": ["rang", "was ringing", "rings", "has rung"], "answer": "rang"},
            {"level": 4, "reward": "500", "question": "A giant sea wave triggered by an undersea earthquake is a ________.", "options": ["Tsunami", "Tornado", "Drought", "Wildfire"], "answer": "Tsunami"},
            {"level": 5, "reward": "1,000", "question": "If we protect forests, many endangered animals ________ survive.", "options": ["will", "would", "must", "can't"], "answer": "will"},
            {"level": 6, "reward": "2,000", "question": "Which minority ethnic group is famous for terrace fields in Sapa?", "options": ["H'mong", "Kinh", "Cham", "Hoa"], "answer": "H'mong"},
            {"level": 7, "reward": "4,000", "question": "Unless you hurry up, you ________ miss the school bus.", "options": ["will", "don't", "wouldn't", "won't"], "answer": "will"},
            {"level": 8, "reward": "8,000", "question": "Which planet is commonly called the 'Red Planet'?", "options": ["Mars", "Venus", "Jupiter", "Saturn"], "answer": "Mars"}
        ],
        "9": [
            {"level": 1, "reward": "100", "question": "Bat Trang is globally renowned for its traditional ________.", "options": ["pottery", "silk", "silverware", "bronze casting"], "answer": "pottery"},
            {"level": 2, "reward": "200", "question": "I don't know where ________ the bus to the airport.", "options": ["to catch", "catching", "caught", "catch"], "answer": "to catch"},
            {"level": 3, "reward": "300", "question": "I wish our class ________ visit the space center next month.", "options": ["could", "can", "will", "is able"], "answer": "could"},
            {"level": 4, "reward": "500", "question": "It is said that Phong Nha Cave has the longest underground ________.", "options": ["river", "road", "railway", "bridge"], "answer": "river"},
            {"level": 5, "reward": "1,000", "question": "The more books you read, the ________ your mind becomes.", "options": ["broader", "broad", "broadest", "more broad"], "answer": "broader"},
            {"level": 6, "reward": "2,000", "question": "Which phrasal verb means 'to transfer skills from generation to generation'?", "options": ["pass down", "turn down", "cut down", "close down"], "answer": "pass down"},
            {"level": 7, "reward": "4,000", "question": "The artisan ________ crafted these conical hats has 40 years of experience.", "options": ["who", "which", "whom", "whose"], "answer": "who"},
            {"level": 8, "reward": "8,000", "question": "A variety of English spoken in a specific region is termed a ________.", "options": ["World English", "Dead tongue", "Grammar error", "Slang only"], "answer": "World English"}
        ]
    },

    # 3. SPEED WORD MATCH (ĐUA GHÉP CẶP TỪ VỰNG TỐC ĐỘ)
    "speed_match": {
        "6": [
            {"en": "Boarding school", "vi": "Trường nội trú"},
            {"en": "Pencil sharpener", "vi": "Cái gọt bút chì"},
            {"en": "Living room", "vi": "Phòng khách"},
            {"en": "Dishwasher", "vi": "Máy rửa bát"},
            {"en": "Confident", "vi": "Tự tin"},
            {"en": "Historic", "vi": "Mang tính lịch sử"},
            {"en": "Waterfall", "vi": "Thác nước"},
            {"en": "Appliance", "vi": "Thiết bị điện gia dụng"}
        ],
        "7": [
            {"en": "Carving eggshells", "vi": "Điêu khắc vỏ trứng"},
            {"en": "Chapped lips", "vi": "Môi nứt nẻ"},
            {"en": "Community service", "vi": "Dịch vụ cộng đồng"},
            {"en": "Musical instrument", "vi": "Nhạc cụ"},
            {"en": "Recipe", "vi": "Công thức nấu ăn"},
            {"en": "Pedestrian", "vi": "Người đi bộ"},
            {"en": "Solar panel", "vi": "Tấm pin mặt trời"},
            {"en": "Carbon footprint", "vi": "Dấu chân carbon"}
        ],
        "8": [
            {"en": "Leisure time", "vi": "Thời gian rảnh rỗi"},
            {"en": "Terrace field", "vi": "Ruộng bậc thang"},
            {"en": "Folk dance", "vi": "Điệu múa dân gian"},
            {"en": "Natural disaster", "vi": "Thảm họa thiên nhiên"},
            {"en": "Tsunami", "vi": "Sóng thần"},
            {"en": "Extraterrestrial", "vi": "Ngoài Trái Đất"},
            {"en": "Space exploration", "vi": "Thám hiểm không gian"},
            {"en": "Bargain", "vi": "Mặc cả, món hời"}
        ],
        "9": [
            {"en": "Handicraft village", "vi": "Làng nghề thủ công"},
            {"en": "Artisan", "vi": "Nghệ nhân"},
            {"en": "Preserve heritage", "vi": "Bảo tồn di sản"},
            {"en": "Affordable", "vi": "Giá cả phải chăng"},
            {"en": "Impersonal passive", "vi": "Bị động khách quan"},
            {"en": "Lingua franca", "vi": "Ngôn ngữ giao tiếp chung"},
            {"en": "Ecotourism", "vi": "Du lịch sinh thái"},
            {"en": "Sustainable", "vi": "Bền vững"}
        ]
    },

    # 4. SENTENCE BUILDER PUZZLE (XẾP CÂU THÔNG MINH)
    "sentence_puzzle": {
        "6": [
            {
                "words": ["My", "sister", "is", "doing", "her", "English", "homework", "now."],
                "vietnamese": "Chị gái tôi đang làm bài tập Tiếng Anh ngay bây giờ."
            },
            {
                "words": ["There", "are", "twenty", "classrooms", "in", "our", "new", "school."],
                "vietnamese": "Có hai mươi phòng học trong ngôi trường mới của chúng tôi."
            },
            {
                "words": ["We", "must", "keep", "our", "classroom", "clean", "and", "tidy."],
                "vietnamese": "Chúng ta phải giữ lớp học sạch sẽ và ngăn nắp."
            }
        ],
        "7": [
            {
                "words": ["My", "brother", "loves", "collecting", "rare", "coins", "in", "his", "free", "time."],
                "vietnamese": "Anh trai tôi thích sưu tầm tiền xu hiếm trong thời gian rảnh."
            },
            {
                "words": ["Doing", "morning", "exercise", "helps", "us", "stay", "healthy", "and", "fit."],
                "vietnamese": "Tập thể dục buổi sáng giúp chúng ta khỏe mạnh và cân đối."
            },
            {
                "words": ["They", "volunteered", "to", "clean", "the", "dirty", "beach", "last", "weekend."],
                "vietnamese": "Họ đã tình nguyện dọn sạch bãi biển bẩn vào cuối tuần trước."
            }
        ],
        "8": [
            {
                "words": ["Living", "in", "the", "countryside", "gives", "people", "a", "peaceful", "feeling."],
                "vietnamese": "Sống ở nông thôn mang lại cho mọi người một cảm giác thanh bình."
            },
            {
                "words": ["Ethnic", "children", "often", "help", "their", "parents", "herd", "buffaloes."],
                "vietnamese": "Trẻ em dân tộc thiểu số thường giúp cha mẹ chăn trâu."
            },
            {
                "words": ["If", "we", "recycle", "plastic", "waste,", "we", "will", "save", "marine", "life."],
                "vietnamese": "Nếu chúng ta tái chế rác nhựa, chúng ta sẽ cứu sống các sinh vật biển."
            }
        ],
        "9": [
            {
                "words": ["The", "local", "artisans", "are", "trying", "to", "preserve", "their", "ancient", "crafts."],
                "vietnamese": "Các nghệ nhân địa phương đang nỗ lực gìn giữ các nghề thủ công cổ truyền."
            },
            {
                "words": ["She", "wishes", "she", "could", "communicate", "confidently", "with", "foreigners."],
                "vietnamese": "Cô ấy ước rằng mình có thể giao tiếp tự tin với người nước ngoài."
            },
            {
                "words": ["The", "more", "you", "practice", "listening,", "the", "better", "your", "pronunciation", "becomes."],
                "vietnamese": "Bạn càng luyện nghe nhiều thì khả năng phát âm của bạn càng trở nên tốt hơn."
            }
        ]
    }
}

def get_game_data(game_name: str, grade: str):
    """Lấy dữ liệu cho một trò chơi cụ thể theo khối lớp"""
    game = GAMES_DATA.get(game_name, {})
    return game.get(str(grade), game.get("6", []))
