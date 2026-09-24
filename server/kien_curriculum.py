# -*- coding: utf-8 -*-
"""
HỆ THỐNG PHÂN PHỐI CHƯƠNG TRÌNH & KIẾN THỨC 105 TIẾT (LỚP 6, 7, 8, 9)
Trích xuất từ thư mục 'Kien' - Sách Tiếng Anh THCS Global Success
Tác giả: Thầy giáo Đinh Văn Thành - Hotline / Zalo: 0915.213717
Đơn vị: Trường THCS Đồng Yên
"""

import os
import glob

# Định vị thư mục Kien
BASE_WORKSPACE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
KIEN_DIR = os.path.join(BASE_WORKSPACE, "Kien")

# Danh mục kiến thức trọng tâm chuẩn 105 tiết của từng khối lớp
CURRICULUM_DATA = {
    "6": {
        "title": "Tiếng Anh 6 - Global Success (105 tiết)",
        "units": [
            {"id": "U1", "title": "Unit 1: My New School", "topics": "School things, Present Simple, Present Continuous, sounds /ɑː/ and /ʌ/"},
            {"id": "U2", "title": "Unit 2: My House", "topics": "Rooms, Furniture, Prepositions of place, sounds /s/ and /z/"},
            {"id": "U3", "title": "Unit 3: My Friends", "topics": "Personality adjectives, Body parts, Be + V-ing for future, sounds /b/ and /p/"},
            {"id": "REV1", "title": "Review 1 & Mid-Term Test 1", "topics": "Language review Units 1-3 & The first mid-term test (Tiết 25)"},
            {"id": "U4", "title": "Unit 4: My Neighbourhood", "topics": "Places, Comparative adjectives, sounds /iː/ and /ɪ/"},
            {"id": "U5", "title": "Unit 5: Natural Wonders of Viet Nam", "topics": "Travel items, Superlative adjectives, Must/Mustn't, sounds /t/ and /d/"},
            {"id": "U6", "title": "Unit 6: Our Tet Holiday", "topics": "Tet activities, Should/Shouldn't, Some/Any, sounds /s/ and /ʃ/"},
            {"id": "REV2", "title": "Review 2 & Term 1 Exam", "topics": "Language review Units 4-6 & Speaking Test & The first term test (Tiết 54)"},
            {"id": "U7", "title": "Unit 7: Television", "topics": "TV programmes, Conjunctions (and, but, so), Question words, sounds /θ/ and /ð/"},
            {"id": "U8", "title": "Unit 8: Sports and Games", "topics": "Sports equipment, Past Simple, Imperatives, sounds /e/ and /æ/"},
            {"id": "U9", "title": "Unit 9: Cities of the World", "topics": "City landmarks, Possessive pronouns, sounds /əʊ/ and /aʊ/"},
            {"id": "REV3", "title": "Review 3 & Mid-Term Test 2", "topics": "Language review Units 7-9 & The second mid-term test (Tiết 77)"},
            {"id": "U10", "title": "Unit 10: Houses in the Future", "topics": "Appliances, Future Simple with Will, Might for possibility"},
            {"id": "U11", "title": "Unit 11: Our Greener World", "topics": "3Rs (Reduce, Reuse, Recycle), First Conditional"},
            {"id": "U12", "title": "Unit 12: Robots", "topics": "Daily tasks, Could for past ability, Will be able to for future"},
            {"id": "REV4", "title": "Review 4 & Final Year Exam", "topics": "Review Units 10-12 & Speaking Test & Final exam (Tiết 105)"}
        ]
    },
    "7": {
        "title": "Tiếng Anh 7 - Global Success (105 tiết)",
        "units": [
            {"id": "U1", "title": "Unit 1: Hobbies", "topics": "Verbs of liking + V-ing, Present Simple, sounds /ə/ and /ɜː/"},
            {"id": "U2", "title": "Unit 2: Healthy Living", "topics": "Health issues, Simple sentences, Imperatives with more/less"},
            {"id": "U3", "title": "Unit 3: Community Service", "topics": "Volunteer activities, Past Simple tense, donating, green living"},
            {"id": "REV1", "title": "Review 1 & Mid-Term Test 1", "topics": "Language review Units 1-3 & Mid-term test (Tiết 25)"},
            {"id": "U4", "title": "Unit 4: Music and Arts", "topics": "Comparisons: as... as, different from, the same as"},
            {"id": "U5", "title": "Unit 5: Food and Drink", "topics": "Countable/Uncountable nouns, Some/Any/A lot of/How many/How much"},
            {"id": "U6", "title": "Unit 6: A Visit to a School", "topics": "Prepositions of time & place, School facilities"},
            {"id": "REV2", "title": "Review 2 & Term 1 Exam", "topics": "Review Units 4-6 & Speaking Test & The first term test (Tiết 54)"},
            {"id": "U7", "title": "Unit 7: Traffic", "topics": "Means of transport, It indicates distance, Used to + V"},
            {"id": "U8", "title": "Unit 8: Films", "topics": "Types of films, Although/Though, However/Nevertheless"},
            {"id": "U9", "title": "Unit 9: Festivals around the World", "topics": "Festivals, Adverbial phrases, Yes/No questions"},
            {"id": "REV3", "title": "Review 3 & Mid-Term Test 2", "topics": "Review Units 7-9 & Mid-term 2 test (Tiết 77)"},
            {"id": "U10", "title": "Unit 10: Energy Sources", "topics": "Renewable & non-renewable energy, Present Continuous for future"},
            {"id": "U11", "title": "Unit 11: Travelling in the Future", "topics": "Future vehicles, Will for prediction, Possessive pronouns"},
            {"id": "U12", "title": "Unit 12: English-Speaking Countries", "topics": "Countries, People, Articles A/An/The"},
            {"id": "REV4", "title": "Review 4 & Final Year Exam", "topics": "Review Units 10-12 & Speaking Test & Final exam (Tiết 105)"}
        ]
    },
    "8": {
        "title": "Tiếng Anh 8 - Global Success (105 tiết)",
        "units": [
            {"id": "U1", "title": "Unit 1: Leisure Time", "topics": "Verbs of liking/disliking + Gerund / To-infinitive"},
            {"id": "U2", "title": "Unit 2: Life in the Countryside", "topics": "Comparative adverbs (-er, more), Life in villages"},
            {"id": "U3", "title": "Unit 3: Teenagers", "topics": "Compound sentences with connectors, Modal verbs should/must"},
            {"id": "REV1", "title": "Review 1 & Mid-Term Test 1", "topics": "Language review Units 1-3 & Mid-term test (Tiết 25)"},
            {"id": "U4", "title": "Unit 4: Ethnic Groups of Viet Nam", "topics": "Yes/No & Wh-questions, Articles with ethnic names"},
            {"id": "U5", "title": "Unit 5: Our Customs and Traditions", "topics": "Zero and First conditionals, Should vs Have to"},
            {"id": "U6", "title": "Unit 6: Lifestyles", "topics": "Past Simple vs Past Continuous with When/While"},
            {"id": "REV2", "title": "Review 2 & Term 1 Exam", "topics": "Review Units 4-6 & Speaking Test & The first term test (Tiết 54)"},
            {"id": "U7", "title": "Unit 7: Environmental Protection", "topics": "Complex sentences with adverbial clauses of cause & effect"},
            {"id": "U8", "title": "Unit 8: Shopping", "topics": "Adverbs of frequency, Present Simple for future timetables"},
            {"id": "U9", "title": "Unit 9: Natural Disasters", "topics": "Past Continuous, Passive voice, Emergency preparedness"},
            {"id": "REV3", "title": "Review 3 & Mid-Term Test 2", "topics": "Review Units 7-9 & Mid-term 2 test (Tiết 77)"},
            {"id": "U10", "title": "Unit 10: Communication in the Future", "topics": "Prepositions of time, Future Continuous"},
            {"id": "U11", "title": "Unit 11: Science and Technology", "topics": "Reported speech: Statements and Wh-questions"},
            {"id": "U12", "title": "Unit 12: Life on Other Planets", "topics": "Reported speech: Questions and commands, May/Might"},
            {"id": "REV4", "title": "Review 4 & Final Year Exam", "topics": "Review Units 10-12 & Speaking Test & Final exam (Tiết 105)"}
        ]
    },
    "9": {
        "title": "Tiếng Anh 9 - Global Success (105 tiết)",
        "units": [
            {"id": "U1", "title": "Unit 1: Local Community", "topics": "Question words before To-infinitive, Phrasal verbs"},
            {"id": "U2", "title": "Unit 2: City Life", "topics": "Double comparatives (The more... the more...), Adjectives of city life"},
            {"id": "U3", "title": "Unit 3: Healthy Living for Teens", "topics": "Modal verbs in First Conditional, Past habits"},
            {"id": "REV1", "title": "Review 1 & Mid-Term Test 1", "topics": "Language review Units 1-3 & Mid-term test (Tiết 25)"},
            {"id": "U4", "title": "Unit 4: Remembering the Past", "topics": "Used to + V, Wish for present situation"},
            {"id": "U5", "title": "Unit 5: Wonders of Viet Nam", "topics": "Impersonal passive (It is said that...), Suggest + V-ing / Should"},
            {"id": "U6", "title": "Unit 6: English in the World", "topics": "Relative clauses: Defining and Non-defining"},
            {"id": "REV2", "title": "Review 2 & Term 1 Exam", "topics": "Review Units 4-6 & Speaking Test & The first term test (Tiết 54)"},
            {"id": "U7", "title": "Unit 7: Natural World", "topics": "Present Perfect Continuous, Mixed conditionals"},
            {"id": "U8", "title": "Unit 8: Tourism", "topics": "Compound nouns, Relative pronouns with prepositions"},
            {"id": "U9", "title": "Unit 9: World Englishes", "topics": "Varieties of English, Conditional sentence types 1 & 2"},
            {"id": "REV3", "title": "Review 3 & Mid-Term Test 2", "topics": "Review Units 7-9 & Mid-term 2 test (Tiết 77)"},
            {"id": "U10", "title": "Unit 10: Space Exploration", "topics": "Past Perfect tense, Defining relative clauses"},
            {"id": "U11", "title": "Unit 11: Changing Roles in Society", "topics": "Future Passive, Non-finite clauses"},
            {"id": "U12", "title": "Unit 12: My Future Career", "topics": "Clauses of concession, result, reason"},
            {"id": "REV4", "title": "Review 4 & Final Year Exam", "topics": "Review Units 10-12 & Speaking Test & Final exam (Tiết 105)"}
        ]
    }
}

def get_curriculum(grade: str):
    return CURRICULUM_DATA.get(str(grade), CURRICULUM_DATA["6"])
