# -*- coding: utf-8 -*-
"""
NGÂN HÀNG CÂU HỎI TIẾNG ANH THCS (LỚP 6, 7, 8, 9)
Chương trình GDPT mới / Kết nối tri thức - Global Success
Tác giả: Thầy giáo Đinh Văn Thành - Hotline / Zalo: 0915.213717
Đầy đủ các dạng bài tập:
1. Phonetics & Stress (Ngữ âm & Trọng âm)
2. Odd-one-out (Từ khác loại)
3. Multiple Choice (Trắc nghiệm từ vựng & ngữ pháp)
4. Cloze Test (Điền từ vào chỗ trống)
5. Matching (Nối cặp từ/câu)
6. Sentence Unscramble (Sắp xếp từ thành câu)
7. Sentence Transformation (Viết lại câu)
8. Reading Comprehension (Đọc hiểu trả lời câu hỏi)
9. Listening (Nghe audio và chọn đáp án)
"""

# Ngân hàng câu hỏi chi tiết theo từng khối lớp
QUESTION_BANK = {
    "6": {
        "title": "Tiếng Anh Lớp 6 - Global Success",
        "units": [
            "Unit 1: My New School", "Unit 2: My House", "Unit 3: My Friends",
            "Unit 4: My Neighbourhood", "Unit 5: Natural Wonders of Viet Nam", "Unit 6: Our Tet Holiday",
            "Unit 7: Television", "Unit 8: Sports and Games", "Unit 9: Cities of the World",
            "Unit 10: Houses in the Future", "Unit 11: Our Greener World", "Unit 12: Robots"
        ],
        "phonetics": [
            {
                "id": "6_ph_1",
                "type": "phonetics",
                "instruction": "Choose the word whose underlined part is pronounced differently from the others.",
                "question": "Which underlined part is pronounced differently?",
                "options": ["played", "helped", "watched", "walked"],
                "underlined_options": ["play<u>ed</u>", "help<u>ed</u>", "watch<u>ed</u>", "walk<u>ed</u>"],
                "answer": "played",
                "explanation": "'played' phát âm là /d/, các từ còn lại phát âm là /t/ sau phụ âm vô thanh."
            },
            {
                "id": "6_ph_2",
                "type": "phonetics",
                "instruction": "Choose the word whose underlined part is pronounced differently from the others.",
                "question": "Which underlined part is pronounced differently?",
                "options": ["cats", "books", "dogs", "cups"],
                "underlined_options": ["cat<u>s</u>", "book<u>s</u>", "dog<u>s</u>", "cup<u>s</u>"],
                "answer": "dogs",
                "explanation": "'dogs' phát âm là /z/, các từ còn lại phát âm là /s/."
            },
            {
                "id": "6_ph_3",
                "type": "phonetics",
                "instruction": "Choose the word whose underlined part is pronounced differently from the others.",
                "question": "Which underlined part is pronounced differently?",
                "options": ["city", "bicycle", "rice", "live"],
                "underlined_options": ["c<u>i</u>ty", "b<u>i</u>cycle", "r<u>i</u>ce", "l<u>i</u>ve"],
                "answer": "city",
                "explanation": "'city' phát âm là /ɪ/, 'bicycle' và 'rice' phát âm là /aɪ/."
            },
            {
                "id": "6_ph_4",
                "type": "phonetics",
                "instruction": "Choose the word whose underlined part is pronounced differently from the others.",
                "question": "Which underlined part is pronounced differently?",
                "options": ["think", "thank", "there", "theatre"],
                "underlined_options": ["<u>th</u>ink", "<u>th</u>ank", "<u>th</u>ere", "<u>th</u>eatre"],
                "answer": "there",
                "explanation": "'there' phát âm là /ð/, các từ còn lại phát âm là /θ/."
            }
        ],
        "odd_one_out": [
            {
                "id": "6_odd_1",
                "type": "odd_one_out",
                "instruction": "Find the odd word out in each group.",
                "question": "Choose the odd one out:",
                "options": ["ruler", "compass", "pencil sharpener", "brother"],
                "answer": "brother",
                "explanation": "'brother' là thành viên gia đình, 3 từ còn lại là đồ dùng học tập (school things)."
            },
            {
                "id": "6_odd_2",
                "type": "odd_one_out",
                "instruction": "Find the odd word out in each group.",
                "question": "Choose the odd one out:",
                "options": ["kitchen", "living room", "bedroom", "teacher"],
                "answer": "teacher",
                "explanation": "'teacher' là nghề nghiệp (giáo viên), 3 từ còn lại là các phòng trong nhà."
            },
            {
                "id": "6_odd_3",
                "type": "odd_one_out",
                "instruction": "Find the odd word out in each group.",
                "question": "Choose the odd one out:",
                "options": ["confident", "friendly", "creative", "apartment"],
                "answer": "apartment",
                "explanation": "'apartment' (căn hộ) là danh từ nơi chốn, 3 từ còn lại là tính từ chỉ tính cách."
            }
        ],
        "multiple_choice": [
            {
                "id": "6_mc_1",
                "type": "multiple_choice",
                "question": "My new school ________ a large green library and an IT room.",
                "options": ["has", "have", "having", "is have"],
                "answer": "has",
                "explanation": "Chủ ngữ số ít 'My new school' chia động từ 'has' ở thì hiện tại đơn."
            },
            {
                "id": "6_mc_2",
                "type": "multiple_choice",
                "question": "Students ________ wear uniform on Mondays and Thursdays.",
                "options": ["must", "can't", "needn't", "shouldn't"],
                "answer": "must",
                "explanation": "'must' diễn tả nội quy trường học bắt buộc phải mặc đồng phục."
            },
            {
                "id": "6_mc_3",
                "type": "multiple_choice",
                "question": "Listen! The children ________ happily in the schoolyard.",
                "options": ["are singing", "sing", "sang", "will sing"],
                "answer": "are singing",
                "explanation": "Có dấu hiệu nhận biết 'Listen!' chỉ hành động đang diễn ra -> Thì hiện tại tiếp diễn (are singing)."
            },
            {
                "id": "6_mc_4",
                "type": "multiple_choice",
                "question": "Da Nang is ________ than my hometown.",
                "options": ["more modern", "modern", "most modern", "modernier"],
                "answer": "more modern",
                "explanation": "So sánh hơn của tính từ dài 'modern' là 'more modern than'."
            },
            {
                "id": "6_mc_5",
                "type": "multiple_choice",
                "question": "There ________ any milk left in the bottle.",
                "options": ["isn't", "aren't", "is", "are"],
                "answer": "isn't",
                "explanation": "'milk' là danh từ không đếm được, dùng 'any' trong câu phủ định số ít -> 'isn't'."
            },
            {
                "id": "6_mc_6",
                "type": "multiple_choice",
                "question": "Robots in the future ________ do all heavy housework for humans.",
                "options": ["will", "can", "must", "might"],
                "answer": "will",
                "explanation": "'will + V' diễn tả dự đoán về khả năng trong tương lai."
            },
            {
                "id": "6_mc_7",
                "type": "multiple_choice",
                "question": "Which city is the ________ in Viet Nam?",
                "options": ["biggest", "bigger", "big", "most big"],
                "answer": "biggest",
                "explanation": "So sánh nhất của tính từ ngắn 'big' gấp đôi phụ âm: 'the biggest'."
            },
            {
                "id": "6_mc_8",
                "type": "multiple_choice",
                "question": "We should ________ old plastic bottles to protect our environment.",
                "options": ["recycle", "pollute", "throw", "burn"],
                "answer": "recycle",
                "explanation": "'recycle' (tái chế) chai nhựa cũ để bảo vệ môi trường theo nguyên tắc 3Rs."
            }
        ],
        "cloze": [
            {
                "id": "6_cloze_1",
                "type": "cloze",
                "instruction": "Read the passage and choose the best word (A, B, C or D) for each space.",
                "passage": "Nam is twelve years old. He goes to a very nice (1) ________ in the center of the town. His school has three floors and twenty classrooms. In the morning, students study subjects like Math, English and Science. During break time, Nam often plays (2) ________ with his best friends in the playground. He likes his school very much because the teachers are (3) ________ and helpful. Nam wants to (4) ________ an architect in the future to design modern houses.",
                "questions": [
                    {
                        "number": "1",
                        "options": ["school", "hospital", "supermarket", "cinema"],
                        "answer": "school",
                        "explanation": "Dựa vào ngữ cảnh học tập: 'goes to a very nice school'."
                    },
                    {
                        "number": "2",
                        "options": ["badminton", "piano", "reading", "sleeping"],
                        "answer": "badminton",
                        "explanation": "'play badminton' (chơi cầu lông ở sân chơi)."
                    },
                    {
                        "number": "3",
                        "options": ["friendly", "angry", "strict", "lazy"],
                        "answer": "friendly",
                        "explanation": "Tính từ tích cực đi cùng 'helpful' là 'friendly' (thân thiện)."
                    },
                    {
                        "number": "4",
                        "options": ["become", "do", "make", "take"],
                        "answer": "become",
                        "explanation": "'become an architect' (trở thành kiến trúc sư)."
                    }
                ]
            }
        ],
        "matching": [
            {
                "id": "6_match_1",
                "type": "matching",
                "instruction": "Match each question in Column A with its suitable answer in Column B.",
                "pairs": [
                    {"left": "Where do you live?", "right": "In a quiet neighbourhood in Da Nang."},
                    {"left": "What does your best friend look like?", "right": "She has long black hair and big brown eyes."},
                    {"left": "How often do you play sports?", "right": "Twice a week, on Tuesday and Friday."},
                    {"left": "What will robots be able to do in the future?", "right": "They will be able to do all household chores."}
                ]
            }
        ],
        "sentence_unscramble": [
            {
                "id": "6_uns_1",
                "type": "sentence_unscramble",
                "instruction": "Reorder the words to make a meaningful sentence.",
                "words": ["My", "classmates", "are", "friendly", "and", "helpful."],
                "correct_sentence": "My classmates are friendly and helpful.",
                "explanation": "Cấu trúc: Chủ ngữ (My classmates) + to be (are) + Tính từ (friendly and helpful)."
            },
            {
                "id": "6_uns_2",
                "type": "sentence_unscramble",
                "instruction": "Reorder the words to make a meaningful sentence.",
                "words": ["We", "should", "plant", "more", "green", "trees", "at", "school."],
                "correct_sentence": "We should plant more green trees at school.",
                "explanation": "Cấu trúc: S + should + V (plant) + O (more green trees) + Địa điểm (at school)."
            }
        ],
        "transformation": [
            {
                "id": "6_trans_1",
                "type": "transformation",
                "instruction": "Rewrite the sentence so that it has the same meaning as the first one.",
                "original": "Because the weather was bad, we stayed at home.",
                "target_prompt": "The weather was bad, so...",
                "correct_answer": "The weather was bad, so we stayed at home.",
                "explanation": "Chuyển từ liên từ chỉ nguyên nhân 'Because' sang liên từ chỉ kết quả 'so'."
            },
            {
                "id": "6_trans_2",
                "type": "transformation",
                "instruction": "Rewrite the sentence so that it has the same meaning as the first one.",
                "original": "No student in our class is taller than Nam.",
                "target_prompt": "Nam is...",
                "correct_answer": "Nam is the tallest student in our class.",
                "explanation": "Chuyển từ so sánh hơn 'No student is taller than' sang so sánh nhất 'the tallest student'."
            }
        ],
        "reading": [
            {
                "id": "6_read_1",
                "type": "reading",
                "instruction": "Read the passage carefully and choose the correct answer for each question.",
                "passage": "Ha Long Bay is one of the most famous natural wonders of Viet Nam. It is located in Quang Ninh Province, about 170 kilometres from Ha Noi. There are thousands of limestone islands in different shapes and sizes rising from the emerald waters. Visitors can take a boat trip around the bay to explore magnificent caves such as Sung Sot Cave and Thien Cung Cave. You can also enjoy fresh seafood and kayaking. It is recognised as a UNESCO World Heritage Site.",
                "questions": [
                    {
                        "number": "1",
                        "question": "Where is Ha Long Bay located?",
                        "options": ["In Quang Ninh Province", "In Ha Noi", "In Da Nang", "In Hue"],
                        "answer": "In Quang Ninh Province",
                        "explanation": "Đoạn văn ghi rõ: 'It is located in Quang Ninh Province'."
                    },
                    {
                        "number": "2",
                        "question": "What can visitors do in Ha Long Bay?",
                        "options": ["Take a boat trip and explore caves", "Go skiing in the snow", "Drive a racing car", "Climb Everest"],
                        "answer": "Take a boat trip and explore caves",
                        "explanation": "Đoạn văn nêu: 'Visitors can take a boat trip around the bay to explore magnificent caves'."
                    },
                    {
                        "number": "3",
                        "question": "Why is Ha Long Bay famous internationally?",
                        "options": ["It is a UNESCO World Heritage Site", "It has the biggest zoo", "It is near Ha Noi", "It has no islands"],
                        "answer": "It is a UNESCO World Heritage Site",
                        "explanation": "Câu cuối khẳng định: 'It is recognised as a UNESCO World Heritage Site'."
                    }
                ]
            }
        ],
        "listening": [
            {
                "id": "6_lis_1",
                "type": "listening",
                "instruction": "Listen to the speaker and choose the correct answer.",
                "audio_text": "Hello, my name is Linda. I am in grade six at Green Field School. My favourite subject is English because I love reading English story books and singing English songs.",
                "question": "What is Linda's favourite subject at school?",
                "options": ["English", "Math", "History", "Science"],
                "answer": "English",
                "explanation": "Linda nói: 'My favourite subject is English'."
            },
            {
                "id": "6_lis_2",
                "type": "listening",
                "instruction": "Listen to the speaker and choose the correct answer.",
                "audio_text": "Every Sunday morning, Peter and his father ride bicycles to the riverside park. They stay there for two hours and play badminton together.",
                "question": "How often do Peter and his father ride bicycles to the park?",
                "options": ["Every Sunday morning", "Every Friday afternoon", "Twice a month", "Every day"],
                "answer": "Every Sunday morning",
                "explanation": "Người nói nói: 'Every Sunday morning, Peter and his father ride bicycles'."
            }
        ]
    },

    "7": {
        "title": "Tiếng Anh Lớp 7 - Global Success",
        "units": [
            "Unit 1: Hobbies", "Unit 2: Healthy Living", "Unit 3: Community Service",
            "Unit 4: Music and Arts", "Unit 5: Food and Drink", "Unit 6: A Visit to a School",
            "Unit 7: Traffic", "Unit 8: Films", "Unit 9: Festivals around the World",
            "Unit 10: Energy Sources", "Unit 11: Travelling in the Future", "Unit 12: English-Speaking Countries"
        ],
        "phonetics": [
            {
                "id": "7_ph_1",
                "type": "phonetics",
                "instruction": "Choose the word whose underlined part is pronounced differently.",
                "question": "Which underlined part is pronounced differently?",
                "options": ["donated", "started", "listened", "decided"],
                "underlined_options": ["donat<u>ed</u>", "start<u>ed</u>", "listen<u>ed</u>", "decid<u>ed</u>"],
                "answer": "listened",
                "explanation": "'listened' có đuôi -ed phát âm là /d/, 3 từ còn lại kết thúc bằng /t/, /d/ nên phát âm là /ɪd/."
            },
            {
                "id": "7_ph_2",
                "type": "phonetics",
                "instruction": "Choose the word whose underlined part is pronounced differently.",
                "question": "Which underlined part is pronounced differently?",
                "options": ["community", "music", "activity", "volunteer"],
                "underlined_options": ["commun<u>i</u>ty", "mus<u>i</u>c", "act<u>i</u>vity", "volunteer"],
                "answer": "music",
                "explanation": "'music' có chữ u phát âm là /juː/, các từ khác có i là /ɪ/."
            },
            {
                "id": "7_ph_3",
                "type": "phonetics",
                "instruction": "Choose the word whose underlined part is pronounced differently.",
                "question": "Which underlined part is pronounced differently?",
                "options": ["cat", "fast", "father", "car"],
                "underlined_options": ["c<u>a</u>t", "f<u>a</u>st", "f<u>a</u>ther", "c<u>a</u>r"],
                "answer": "cat",
                "explanation": "'cat' phát âm là /æ/, các từ còn lại phát âm là /ɑː/."
            }
        ],
        "odd_one_out": [
            {
                "id": "7_odd_1",
                "type": "odd_one_out",
                "instruction": "Find the odd word out in each group.",
                "question": "Choose the odd one out:",
                "options": ["solar energy", "wind energy", "coal", "hydro energy"],
                "answer": "coal",
                "explanation": "'coal' (than đá) là năng lượng hóa thạch không tái tạo; 3 từ còn lại là năng lượng tái tạo."
            },
            {
                "id": "7_odd_2",
                "type": "odd_one_out",
                "instruction": "Find the odd word out in each group.",
                "question": "Choose the odd one out:",
                "options": ["comedy", "documentary", "horror", "traffic jam"],
                "answer": "traffic jam",
                "explanation": "'traffic jam' là hiện tượng giao thông, 3 từ còn lại là thể loại phim."
            }
        ],
        "multiple_choice": [
            {
                "id": "7_mc_1",
                "type": "multiple_choice",
                "question": "My sister enjoys ________ origami paper flowers in her spare time.",
                "options": ["making", "make", "made", "makes"],
                "answer": "making",
                "explanation": "Sau động từ chỉ sự yêu thích 'enjoy' đi với V-ing: 'enjoy making'."
            },
            {
                "id": "7_mc_2",
                "type": "multiple_choice",
                "question": "You should eat more fresh vegetables ________ they provide essential vitamins.",
                "options": ["because", "so", "but", "although"],
                "answer": "because",
                "explanation": "'because' chỉ nguyên nhân: ăn rau vì chúng cung cấp vitamin."
            },
            {
                "id": "7_mc_3",
                "type": "multiple_choice",
                "question": "We ________ hundreds of warm coats to poor mountain children last winter.",
                "options": ["donated", "donate", "will donate", "are donating"],
                "answer": "donated",
                "explanation": "Có mốc thời gian trong quá khứ 'last winter' -> Chia thì quá khứ đơn 'donated'."
            },
            {
                "id": "7_mc_4",
                "type": "multiple_choice",
                "question": "Classical music is not as ________ as modern pop music for teenagers.",
                "options": ["exciting", "more exciting", "most exciting", "excited"],
                "answer": "exciting",
                "explanation": "Cấu trúc so sánh bằng/không bằng: 'as + adj (nguyên thể) + as' -> 'as exciting as'."
            },
            {
                "id": "7_mc_5",
                "type": "multiple_choice",
                "question": "Lan ________ to school on foot when she was in primary school.",
                "options": ["used to go", "uses to go", "is going", "has gone"],
                "answer": "used to go",
                "explanation": "'used to + V' diễn tả thói quen trong quá khứ nay không còn nữa."
            },
            {
                "id": "7_mc_6",
                "type": "multiple_choice",
                "question": "________ it was raining heavily, they still went to the music festival.",
                "options": ["Although", "Because", "Despite", "However"],
                "answer": "Although",
                "explanation": "'Although + S + V' (mặc dù trời mưa to, họ vẫn đi xem hội ca nhạc)."
            },
            {
                "id": "7_mc_7",
                "type": "multiple_choice",
                "question": "In the future, electric vehicles will help ________ carbon emissions.",
                "options": ["reduce", "increase", "damage", "destroy"],
                "answer": "reduce",
                "explanation": "'reduce' (giảm thiểu khí thải carbon)."
            }
        ],
        "cloze": [
            {
                "id": "7_cloze_1",
                "type": "cloze",
                "instruction": "Choose the best option to complete the passage.",
                "passage": "Volunteer work is a meaningful activity for students. Last summer, our class joined a community project. We (1) ________ dirty streets and planted flowers along the sidewalks. We also collected old books and notebooks to send to students in remote areas. Doing community service helps us become more (2) ________ and learn how to share with others. In addition, we made many new (3) ________ who share the same passion for helping society. Everyone felt proud and happy with the (4) ________ we achieved.",
                "questions": [
                    {
                        "number": "1",
                        "options": ["cleaned up", "messed up", "broke down", "cut off"],
                        "answer": "cleaned up",
                        "explanation": "'clean up dirty streets' (dọn dẹp đường phố sạch sẽ)."
                    },
                    {
                        "number": "2",
                        "options": ["responsible", "careless", "lazy", "selfish"],
                        "answer": "responsible",
                        "explanation": "'become more responsible' (trở nên có trách nhiệm hơn)."
                    },
                    {
                        "number": "3",
                        "options": ["friends", "enemies", "strangers", "teachers"],
                        "answer": "friends",
                        "explanation": "'make new friends' (kết bạn mới)."
                    },
                    {
                        "number": "4",
                        "options": ["results", "troubles", "mistakes", "accidents"],
                        "answer": "results",
                        "explanation": "'proud and happy with the results' (tự hào về kết quả đạt được)."
                    }
                ]
            }
        ],
        "matching": [
            {
                "id": "7_match_1",
                "type": "matching",
                "instruction": "Match the festival in Column A with its typical activity in Column B.",
                "pairs": [
                    {"left": "Mid-Autumn Festival", "right": "Carrying star lanterns and eating mooncakes."},
                    {"left": "Halloween", "right": "Wearing spooky costumes and trick-or-treating."},
                    {"left": "Tet Holiday", "right": "Making Chung cake and receiving lucky money."},
                    {"left": "Christmas", "right": "Decorating pine trees and giving presents."}
                ]
            }
        ],
        "sentence_unscramble": [
            {
                "id": "7_uns_1",
                "type": "sentence_unscramble",
                "instruction": "Reorder the words to make a meaningful sentence.",
                "words": ["Eating", "healthy", "food", "is", "very", "good", "for", "our", "health."],
                "correct_sentence": "Eating healthy food is very good for our health.",
                "explanation": "Chủ ngữ là V-ing (Eating healthy food) + to be (is) + good for our health."
            },
            {
                "id": "7_uns_2",
                "type": "sentence_unscramble",
                "instruction": "Reorder the words to make a meaningful sentence.",
                "words": ["They", "donated", "old", "books", "to", "poor", "students", "yesterday."],
                "correct_sentence": "They donated old books to poor students yesterday.",
                "explanation": "Cấu trúc donate something to somebody: S + donated + old books + to poor students + yesterday."
            }
        ],
        "transformation": [
            {
                "id": "7_trans_1",
                "type": "transformation",
                "instruction": "Rewrite the sentence using the given word without changing its meaning.",
                "original": "My brother likes collecting old stamps.",
                "target_prompt": "My brother is fond of...",
                "correct_answer": "My brother is fond of collecting old stamps.",
                "explanation": "'like + V-ing' tương đương với 'be fond of + V-ing'."
            },
            {
                "id": "7_trans_2",
                "type": "transformation",
                "instruction": "Rewrite the sentence using the given word without changing its meaning.",
                "original": "Because it was noisy, I couldn't concentrate on my homework.",
                "target_prompt": "It was noisy, so...",
                "correct_answer": "It was noisy, so I couldn't concentrate on my homework.",
                "explanation": "Đổi liên từ 'Because' thành 'so'."
            }
        ],
        "reading": [
            {
                "id": "7_read_1",
                "type": "reading",
                "instruction": "Read the text about Renewable Energy and answer the questions.",
                "passage": "Energy is essential for our modern life, but fossil fuels like coal and oil are running out and causing serious air pollution. Therefore, scientists around the world are developing renewable energy sources. Solar energy comes from the sun and can be turned into electricity using solar panels. Wind power is generated by huge wind turbines in coastal areas. These clean sources of energy are inexhaustible and do not produce harmful greenhouse gases.",
                "questions": [
                    {
                        "number": "1",
                        "question": "What is the problem with fossil fuels?",
                        "options": ["They are running out and cause pollution", "They are too clean", "They never run out", "They are free"],
                        "answer": "They are running out and cause pollution",
                        "explanation": "Đoạn văn ghi: 'fossil fuels like coal and oil are running out and causing serious air pollution'."
                    },
                    {
                        "number": "2",
                        "question": "How is solar energy captured?",
                        "options": ["Using solar panels", "By burning coal", "By digging oil", "Using gasoline"],
                        "answer": "Using solar panels",
                        "explanation": "Đoạn văn nêu: 'using solar panels'."
                    },
                    {
                        "number": "3",
                        "question": "Why are renewable energy sources considered clean?",
                        "options": ["They do not produce harmful greenhouse gases", "They are expensive", "They use coal", "They are smelly"],
                        "answer": "They do not produce harmful greenhouse gases",
                        "explanation": "Đoạn văn viết: 'do not produce harmful greenhouse gases'."
                    }
                ]
            }
        ],
        "listening": [
            {
                "id": "7_lis_1",
                "type": "listening",
                "instruction": "Listen to the announcement and answer the question.",
                "audio_text": "Good morning students! Our Green Club is organising a recycling day this Saturday from eight in the morning until noon. Please bring your used paper, cartons and plastic bottles to the central playground.",
                "question": "When does the recycling activity take place?",
                "options": ["This Saturday morning", "This Sunday afternoon", "Next Monday", "Tomorrow evening"],
                "answer": "This Saturday morning",
                "explanation": "Thông báo: 'this Saturday from eight in the morning until noon'."
            }
        ]
    },

    "8": {
        "title": "Tiếng Anh Lớp 8 - Global Success",
        "units": [
            "Unit 1: Leisure Time", "Unit 2: Life in the Countryside", "Unit 3: Teenagers",
            "Unit 4: Ethnic Groups of Viet Nam", "Unit 5: Our Customs and Traditions", "Unit 6: Lifestyles",
            "Unit 7: Environmental Protection", "Unit 8: Shopping", "Unit 9: Natural Disasters",
            "Unit 10: Communication in the Future", "Unit 11: Science and Technology", "Unit 12: Life on Other Planets"
        ],
        "phonetics": [
            {
                "id": "8_ph_1",
                "type": "phonetics",
                "instruction": "Choose the word whose underlined part is pronounced differently.",
                "question": "Which underlined part is pronounced differently?",
                "options": ["question", "pollution", "eruption", "tradition"],
                "underlined_options": ["ques<u>ti</u>on", "pollu<u>ti</u>on", "erup<u>ti</u>on", "tradi<u>ti</u>on"],
                "answer": "question",
                "explanation": "'question' phát âm là /tʃ/, 3 từ còn lại phát âm là /ʃ/."
            },
            {
                "id": "8_ph_2",
                "type": "phonetics",
                "instruction": "Choose the word whose underlined part is pronounced differently.",
                "question": "Which underlined part is pronounced differently?",
                "options": ["leisure", "neighbour", "weight", "eight"],
                "underlined_options": ["l<u>ei</u>sure", "n<u>ei</u>ghbour", "w<u>ei</u>ght", "<u>ei</u>ght"],
                "answer": "leisure",
                "explanation": "'leisure' phát âm là /e/, các từ còn lại phát âm là /eɪ/."
            }
        ],
        "odd_one_out": [
            {
                "id": "8_odd_1",
                "type": "odd_one_out",
                "instruction": "Find the odd word out in each group.",
                "question": "Choose the odd one out:",
                "options": ["tornado", "earthquake", "tsunami", "smartphone"],
                "answer": "smartphone",
                "explanation": "'smartphone' là thiết bị công nghệ, 3 từ còn lại là thảm họa thiên nhiên (natural disasters)."
            }
        ],
        "multiple_choice": [
            {
                "id": "8_mc_1",
                "type": "multiple_choice",
                "question": "Living in the countryside is ________ than living in a crowded metropolis.",
                "options": ["more peaceful", "peaceful", "peacefuller", "most peaceful"],
                "answer": "more peaceful",
                "explanation": "So sánh hơn của tính từ dài 'peaceful' là 'more peaceful than'."
            },
            {
                "id": "8_mc_2",
                "type": "multiple_choice",
                "question": "Students are keen on ________ new digital skills and AI tools.",
                "options": ["learning", "learn", "learned", "to learn"],
                "answer": "learning",
                "explanation": "Cấu trúc: 'be keen on + V-ing' -> 'keen on learning'."
            },
            {
                "id": "8_mc_3",
                "type": "multiple_choice",
                "question": "While my father was reading a book, my mother ________ dinner.",
                "options": ["was cooking", "cooked", "cooks", "is cooking"],
                "answer": "was cooking",
                "explanation": "Hai hành động song song cùng diễn ra trong quá khứ kết nối bằng 'While' đều chia thì quá khứ tiếp diễn."
            },
            {
                "id": "8_mc_4",
                "type": "multiple_choice",
                "question": "The ethnic minority people wear colourful ________ costumes during village festivals.",
                "options": ["traditional", "tradition", "traditionally", "traditionalist"],
                "answer": "traditional",
                "explanation": "Trước danh từ 'costumes' cần một tính từ bổ nghĩa: 'traditional costumes'."
            },
            {
                "id": "8_mc_5",
                "type": "multiple_choice",
                "question": "If we don't save clean water, we ________ face severe droughts in the dry season.",
                "options": ["will", "would", "must", "can't"],
                "answer": "will",
                "explanation": "Câu điều kiện loại 1 (First conditional): If + hiện tại đơn, S + will + V."
            }
        ],
        "cloze": [
            {
                "id": "8_cloze_1",
                "type": "cloze",
                "instruction": "Fill in the blank with the appropriate word.",
                "passage": "Natural disasters can strike at any time. When an earthquake happens, you should drop to your knees, take (1) ________ under a sturdy desk, and hold on until the shaking stops. If you are outdoors, stay away from tall buildings, power lines, and trees. Having an emergency (2) ________ with clean water, canned food, flashlight, and medical supplies is very important for every family.",
                "questions": [
                    {
                        "number": "1",
                        "options": ["cover", "shower", "photo", "medicine"],
                        "answer": "cover",
                        "explanation": "'take cover' là cụm từ chỉ việc tìm chỗ trú ẩn an toàn."
                    },
                    {
                        "number": "2",
                        "options": ["kit", "toy", "movie", "book"],
                        "answer": "kit",
                        "explanation": "'emergency kit' là bộ túi cứu hộ khẩn cấp."
                    }
                ]
            }
        ],
        "matching": [
            {
                "id": "8_match_1",
                "type": "matching",
                "instruction": "Match the disaster with its definition.",
                "pairs": [
                    {"left": "Tsunami", "right": "A giant sea wave caused by an underwater earthquake."},
                    {"left": "Tornado", "right": "A violent funnel of spinning air touching the ground."},
                    {"left": "Drought", "right": "A long period with little or no rainfall."},
                    {"left": "Landslide", "right": "A rapid downhill movement of rock, soil and debris."}
                ]
            }
        ],
        "sentence_unscramble": [
            {
                "id": "8_uns_1",
                "type": "sentence_unscramble",
                "instruction": "Reorder the words to make a meaningful sentence.",
                "words": ["Ethnic", "minority", "people", "wear", "beautiful", "traditional", "costumes."],
                "correct_sentence": "Ethnic minority people wear beautiful traditional costumes.",
                "explanation": "S (Ethnic minority people) + V (wear) + O (beautiful traditional costumes)."
            },
            {
                "id": "8_uns_2",
                "type": "sentence_unscramble",
                "instruction": "Reorder the words to make a meaningful sentence.",
                "words": ["Protecting", "the", "environment", "is", "the", "responsibility", "of", "everyone."],
                "correct_sentence": "Protecting the environment is the responsibility of everyone.",
                "explanation": "Chủ ngữ danh động từ: 'Protecting the environment is the responsibility of everyone.'"
            }
        ],
        "transformation": [
            {
                "id": "8_trans_1",
                "type": "transformation",
                "instruction": "Rewrite the sentence using conditional type 1.",
                "original": "Unless we protect wildlife, many rare animals will become extinct.",
                "target_prompt": "If we don't...",
                "correct_answer": "If we don't protect wildlife, many rare animals will become extinct.",
                "explanation": "'Unless + khẳng định' tương đương 'If + phủ định'."
            }
        ],
        "reading": [
            {
                "id": "8_read_1",
                "type": "reading",
                "instruction": "Read the text and answer the question.",
                "passage": "In the northern mountainous regions of Viet Nam, terrace fields (ruộng bậc thang) are not only a miraculous agricultural landscape but also an embodiment of ethnic ingenuity. For hundreds of years, the H'mong and Dao farmers have carved steps into steep mountain slopes to cultivate wet rice. When water fills the fields during the pouring season, the terraces look like giant shiny mirrors reflecting the sky. During the harvesting season in autumn, the valleys turn into breathtaking golden ribbons.",
                "questions": [
                    {
                        "number": "1",
                        "question": "Who created the terrace fields in northern Viet Nam?",
                        "options": ["The H'mong and Dao farmers", "Foreign tourists", "Modern machines", "City people"],
                        "answer": "The H'mong and Dao farmers",
                        "explanation": "Đoạn văn ghi: 'the H'mong and Dao farmers have carved steps into steep mountain slopes'."
                    },
                    {
                        "number": "2",
                        "question": "What do terrace fields look like during the pouring season?",
                        "options": ["Giant shiny mirrors", "Golden ribbons", "Dark caves", "Desert plains"],
                        "answer": "Giant shiny mirrors",
                        "explanation": "Đoạn văn miêu tả: 'the terraces look like giant shiny mirrors reflecting the sky'."
                    }
                ]
            }
        ],
        "listening": [
            {
                "id": "8_lis_1",
                "type": "listening",
                "instruction": "Listen to the report and answer.",
                "audio_text": "Scientists forecast that in the next twenty years, artificial intelligence and robotics will transform education, allowing students to learn with personalized digital tutors at their own pace.",
                "question": "What will transform education according to scientists?",
                "options": ["Artificial intelligence and robotics", "Old chalkboards", "Paper books only", "Television"],
                "answer": "Artificial intelligence and robotics",
                "explanation": "Người nói nêu rõ: 'artificial intelligence and robotics'."
            }
        ]
    },

    "9": {
        "title": "Tiếng Anh Lớp 9 - Global Success",
        "units": [
            "Unit 1: Local Community", "Unit 2: City Life", "Unit 3: Healthy Living for Teens",
            "Unit 4: Remembering the Past", "Unit 5: Wonders of Viet Nam", "Unit 6: English in the World",
            "Unit 7: Natural World", "Unit 8: Tourism", "Unit 9: World Englishes",
            "Unit 10: Space Exploration", "Unit 11: Changing Roles in Society", "Unit 12: My Future Career"
        ],
        "phonetics": [
            {
                "id": "9_ph_1",
                "type": "phonetics",
                "instruction": "Choose the word whose underlined part is pronounced differently.",
                "question": "Which underlined part is pronounced differently?",
                "options": ["craft", "center", "city", "cinema"],
                "underlined_options": ["<u>c</u>raft", "<u>c</u>enter", "<u>c</u>ity", "<u>c</u>inema"],
                "answer": "craft",
                "explanation": "'craft' phát âm chữ c là /k/, 3 từ còn lại phát âm là /s/."
            },
            {
                "id": "9_ph_2",
                "type": "phonetics",
                "instruction": "Choose the word with different main stress pattern.",
                "question": "Which word has a different main stress position?",
                "options": ["artisan", "community", "environment", "traditional"],
                "answer": "artisan",
                "explanation": "'artisan' nhấn trọng âm 1, các từ còn lại nhấn trọng âm 2."
            }
        ],
        "odd_one_out": [
            {
                "id": "9_odd_1",
                "type": "odd_one_out",
                "instruction": "Find the odd word out in each group.",
                "question": "Choose the odd one out:",
                "options": ["pottery", "conical hat", "silk scarf", "subway"],
                "answer": "subway",
                "explanation": "'subway' (tàu điện ngầm) là phương tiện giao thông, 3 từ còn lại là sản phẩm thủ công truyền thống (handicrafts)."
            }
        ],
        "multiple_choice": [
            {
                "id": "9_mc_1",
                "type": "multiple_choice",
                "question": "My grandparents ________ in this peaceful handicraft village for more than fifty years.",
                "options": ["have lived", "lived", "live", "are living"],
                "answer": "have lived",
                "explanation": "Có mốc thời gian kéo dài đến hiện tại 'for more than fifty years' -> Thì hiện tại hoàn thành (have lived)."
            },
            {
                "id": "9_mc_2",
                "type": "multiple_choice",
                "question": "I don't know where ________ the best authentic Bat Trang ceramic bowls.",
                "options": ["to buy", "buying", "bought", "buy"],
                "answer": "to buy",
                "explanation": "Cấu trúc từ để hỏi kết hợp to-V: 'where to buy'."
            },
            {
                "id": "9_mc_3",
                "type": "multiple_choice",
                "question": "She wishes she ________ speak fluent English like a native interpreter.",
                "options": ["could", "can", "will", "is able to"],
                "answer": "could",
                "explanation": "Câu ước không có thật ở hiện tại (Wish clause): S + wish + S + V quá khứ đơn / could + V."
            },
            {
                "id": "9_mc_4",
                "type": "multiple_choice",
                "question": "It is said that Ha Long Bay is one of the most magnificent ________ in the world.",
                "options": ["wonders", "wonder", "wonderful", "wondering"],
                "answer": "wonders",
                "explanation": "'one of the most magnificent + danh từ số nhiều' -> 'wonders'."
            },
            {
                "id": "9_mc_5",
                "type": "multiple_choice",
                "question": "The more English books and news you read, the ________ your vocabulary becomes.",
                "options": ["richer", "richest", "rich", "more richly"],
                "answer": "richer",
                "explanation": "Cấu trúc so sánh kép (Double comparative): 'The more... the richer...'."
            }
        ],
        "cloze": [
            {
                "id": "9_cloze_1",
                "type": "cloze",
                "instruction": "Complete the passage with the correct words.",
                "passage": "Many traditional handicraft villages in Viet Nam are facing challenges because young people prefer moving to big cities. However, some creative artisans are combining ancient techniques with modern (1) ________ to attract new customers. They promote their products on social media and welcome international tourists for hands-on (2) ________. By doing this, they can (3) ________ cultural heritage and create sustainable livelihoods.",
                "questions": [
                    {
                        "number": "1",
                        "options": ["designs", "garbage", "excuses", "accidents"],
                        "answer": "designs",
                        "explanation": "'modern designs' (mẫu mã thiết kế hiện đại)."
                    },
                    {
                        "number": "2",
                        "options": ["workshops", "wars", "troubles", "punishments"],
                        "answer": "workshops",
                        "explanation": "'hands-on workshops' (các buổi trải nghiệm thực tế)."
                    },
                    {
                        "number": "3",
                        "options": ["preserve", "destroy", "neglect", "forget"],
                        "answer": "preserve",
                        "explanation": "'preserve cultural heritage' (bảo tồn di sản văn hóa)."
                    }
                ]
            }
        ],
        "matching": [
            {
                "id": "9_match_1",
                "type": "matching",
                "instruction": "Match the phrasal verb in Column A with its definition in Column B.",
                "pairs": [
                    {"left": "pass down", "right": "Transfer traditional skills to the next generation."},
                    {"left": "look forward to", "right": "Feel excited and happy about something in the future."},
                    {"left": "die out", "right": "Disappear completely and no longer exist."},
                    {"left": "cut down on", "right": "Reduce the quantity or amount of something."}
                ]
            }
        ],
        "sentence_unscramble": [
            {
                "id": "9_uns_1",
                "type": "sentence_unscramble",
                "instruction": "Reorder the words to make a meaningful sentence.",
                "words": ["Artisans", "help", "preserve", "the", "traditional", "craft", "villages."],
                "correct_sentence": "Artisans help preserve the traditional craft villages.",
                "explanation": "S (Artisans) + help + V (preserve) + O (the traditional craft villages)."
            },
            {
                "id": "9_uns_2",
                "type": "sentence_unscramble",
                "instruction": "Reorder the words to make a meaningful sentence.",
                "words": ["Ecotourism", "protects", "valuable", "natural", "habitats", "effectively."],
                "correct_sentence": "Ecotourism protects valuable natural habitats effectively.",
                "explanation": "S (Ecotourism) + V (protects) + O (valuable natural habitats) + Adv (effectively)."
            }
        ],
        "transformation": [
            {
                "id": "9_trans_1",
                "type": "transformation",
                "instruction": "Rewrite using indirect speech or wish structure.",
                "original": "People say that Da Nang is a worth-living city.",
                "target_prompt": "It is said that...",
                "correct_answer": "It is said that Da Nang is a worth-living city.",
                "explanation": "Bị động khách quan: 'People say that...' -> 'It is said that...'."
            },
            {
                "id": "9_trans_2",
                "type": "transformation",
                "instruction": "Rewrite using wish structure.",
                "original": "I cannot speak English fluently.",
                "target_prompt": "I wish...",
                "correct_answer": "I wish I could speak English fluently.",
                "explanation": "Ước muốn ở hiện tại: 'I wish I could + V'."
            }
        ],
        "reading": [
            {
                "id": "9_read_1",
                "type": "reading",
                "instruction": "Read the passage and choose the best answer.",
                "passage": "English is no longer the sole property of native speakers in Britain or America. Today, non-native English speakers vastly outnumber native speakers worldwide. English has become the primary global lingua franca used in international business, academic research, diplomacy, and aviation. As a result, varieties known as 'World Englishes' have emerged, each influenced by regional accents, vocabularies, and cultural contexts. The ultimate goal of learning English today is effective international communication, rather than sounding like an exact replica of a London or New York resident.",
                "questions": [
                    {
                        "number": "1",
                        "question": "Who outnumbers whom among English speakers today?",
                        "options": ["Non-native speakers outnumber native speakers", "Native speakers outnumber non-native speakers", "They are equal", "Nobody speaks English"],
                        "answer": "Non-native speakers outnumber native speakers",
                        "explanation": "Đoạn văn nêu: 'non-native English speakers vastly outnumber native speakers worldwide'."
                    },
                    {
                        "number": "2",
                        "question": "What is the primary goal of learning English in modern times?",
                        "options": ["Effective international communication", "Imitating a London accent perfectly", "Forgetting native language", "Passing tests only"],
                        "answer": "Effective international communication",
                        "explanation": "Đoạn văn khẳng định: 'The ultimate goal of learning English today is effective international communication'."
                    }
                ]
            }
        ],
        "listening": [
            {
                "id": "9_lis_1",
                "type": "listening",
                "instruction": "Listen to the career guidance talk and answer.",
                "audio_text": "Welcome ninth graders to the career counseling seminar! When choosing a future career path, you should consider three factors: your genuine passions, your individual strengths, and the current employment demands of the digital society.",
                "question": "What three factors should students consider when choosing a career?",
                "options": [
                    "Passions, strengths, and digital society job demands",
                    "Salary, cars, and clothes",
                    "Friends' opinions only",
                    "School location only"
                ],
                "answer": "Passions, strengths, and digital society job demands",
                "explanation": "Bài nói nêu: 'your genuine passions, your individual strengths, and the current employment demands'."
            }
        ]
    }
}

def get_grade_questions(grade: str):
    """Lấy toàn bộ ngân hàng câu hỏi của một khối lớp"""
    return QUESTION_BANK.get(str(grade), QUESTION_BANK["6"])

def get_all_grades_summary():
    """Trả về danh sách các khối lớp và danh sách Unit"""
    summary = []
    for g, data in QUESTION_BANK.items():
        summary.append({
            "grade": g,
            "title": data["title"],
            "unit_count": len(data["units"]),
            "units": data["units"],
            "question_counts": {
                "phonetics": len(data.get("phonetics", [])),
                "odd_one_out": len(data.get("odd_one_out", [])),
                "multiple_choice": len(data.get("multiple_choice", [])),
                "cloze": len(data.get("cloze", [])),
                "matching": len(data.get("matching", [])),
                "sentence_unscramble": len(data.get("sentence_unscramble", [])),
                "transformation": len(data.get("transformation", [])),
                "reading": len(data.get("reading", [])),
                "listening": len(data.get("listening", []))
            }
        })
    return summary
