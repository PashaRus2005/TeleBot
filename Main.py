import telebot
from telebot import types
import json
import random
import os


# Инициализация бота с токеном
bot = telebot.TeleBot("7008306835:AAGZZSS7XqZDc1sO4M2oI8wUe37AdwtDUWY")

# Словарь для хранения результатов пользователей
user_results = {}

texts = {
    "ru": {
        "welcome": "<b>Привет, {name}!</b>\n\nВыберите язык:",
        "choose_language": "Выберите язык:",
        "choose_course": "Выберите курс для тестирования:",
        "choose_test_1": "Выберите тест для 1 курса:",
        "choose_test_2": "Выберите тест для 2 курса:",
        "choose_test_3": "Выберите тест для 3 курса:",
    },
    "uz": {
        "welcome": "<b>Salom, {name}!</b>\n\nTilni tanlang:",
        "choose_language": "Tilni tanlang:",
        "choose_course": "Testni boshlash uchun kursni tanlang 👇",
        "choose_test_1": "1 kurs uchun testni tanlang:",
        "choose_test_2": "2 kurs uchun testni tanlang:",
        "choose_test_3": "3 kurs uchun testni tanlang:",
    }
}


current_language = "ru"

channel_id = "@testttatf" 

def is_subscribed(chat_id):
    try:
        member = bot.get_chat_member(chat_id=channel_id, user_id=chat_id)
        if member.status != 'left':
            return True
        else:
            return False
    except Exception as e:
        print(f"Ошибка при проверке подписки: {e}")
        return False

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    if is_subscribed(message.chat.id):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        ru_btn = types.KeyboardButton("Русский")
        uz_btn = types.KeyboardButton("O'zbek")
        markup.add(ru_btn, uz_btn)
        bot.send_message(
            chat_id=message.chat.id,
            text=texts[current_language]["welcome"].format(name=message.chat.first_name),
            parse_mode="HTML",
            reply_markup=markup
        )
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Пожалуйста, подпишитесь на канал {channel_id}, чтобы использовать бота."
        )

# Обработчик выбора языка
@bot.message_handler(func=lambda message: message.text in ["Русский", "O'zbek"])
def set_language(message):
    global current_language
    if message.text == "Русский":
        current_language = "ru"
    elif message.text == "O'zbek":
        current_language = "uz"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    year1_btn = types.KeyboardButton("1 kurs" if current_language == "uz" else "1 курс")
    year2_btn = types.KeyboardButton("2 kurs" if current_language == "uz" else "2 курс")
    year3_btn = types.KeyboardButton("3 kurs" if current_language == "uz" else "3 курс")
    markup.add(year1_btn, year2_btn, year3_btn)
    bot.send_message(
        chat_id=message.chat.id,
        text=texts[current_language]["choose_course"],
        reply_markup=markup
    )

# Обработчик для 1 курса
@bot.message_handler(func=lambda message: message.text in ["1 курс", "1 kurs"])
def handle_year1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    test1_btn = types.KeyboardButton("Тестирование по Анатомии 1" if current_language == "ru" else "Anatomiya")
    test2_btn = types.KeyboardButton("Тестирование по Гистологии 1" if current_language == "ru" else "Gistologiya")
    test3_btn = types.KeyboardButton("Тестирование по Биологии 1" if current_language == "ru" else "Biologiya")
    test4_btn = types.KeyboardButton("Тестирование по Биофизике 1" if current_language == "ru" else "Biofizika")
    test5_btn = types.KeyboardButton("---" if current_language == "ru" else "Kimyo")
    exit_btn = types.KeyboardButton("Назад" if current_language == "ru" else "Orqaga")
    markup.add(test1_btn, test2_btn, test3_btn, test4_btn, test5_btn, exit_btn)
    bot.send_message(
        chat_id=message.chat.id,
        text=texts[current_language]["choose_test_1"],
        reply_markup=markup
    )

# Обработчик для 2 курса
@bot.message_handler(func=lambda message: message.text in ["2 курс", "2 kurs"])
def handle_year2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    test1_btn = types.KeyboardButton("Тестирование по Биохимии 2" if current_language == "ru" else "Biokimyo")
    test2_btn = types.KeyboardButton("Тестирование по БКП 2" if current_language == "ru" else "BKP")
    test3_btn = types.KeyboardButton("---" if current_language == "ru" else "ICP")
    test4_btn = types.KeyboardButton("Тестирование по Физиология 2" if current_language == "ru" else "Fiziologiya")
    exit_btn = types.KeyboardButton("Назад" if current_language == "ru" else "Orqaga")
    markup.add(test1_btn, test2_btn, test3_btn, test4_btn, exit_btn)
    bot.send_message(
        chat_id=message.chat.id,
        text=texts[current_language]["choose_test_2"],
        reply_markup=markup
    )

# Обработчик для 3 курса
@bot.message_handler(func=lambda message: message.text in ["3 курс", "3 kurs"])
def handle_year3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    pharmacology_btn = types.KeyboardButton("Тест по Фармакологии 3" if current_language == "ru" else "Farmakologiya")
    bcp_btn = types.KeyboardButton("Тест по БКП 3" if current_language == "ru" else "BKP3")
    patan_btn = types.KeyboardButton("Тестирование по Патан 3" if current_language == "ru" else "---")
    exit_btn = types.KeyboardButton("Назад" if current_language == "ru" else "Orqaga")
    markup.add(pharmacology_btn, bcp_btn, patan_btn, exit_btn)
    bot.send_message(
        chat_id=message.chat.id,
        text=texts[current_language]["choose_test_3"],
        reply_markup=markup
    )

# Обработчик нажатия кнопки "Назад/Orqaga"
@bot.message_handler(func=lambda message: message.text in ["Назад", "Orqaga"])
def exit_test(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    year1_btn = types.KeyboardButton("1 kurs" if current_language == "uz" else "1 курс")
    year2_btn = types.KeyboardButton("2 kurs" if current_language == "uz" else "2 курс")
    year3_btn = types.KeyboardButton("3 kurs" if current_language == "uz" else "3 курс")
    markup.add(year1_btn, year2_btn, year3_btn)
    bot.send_message(
        chat_id=message.chat.id,
        text=texts[current_language]["choose_course"],
        reply_markup=markup
    )

# Обработчик команд с несуществующим тестом в этой раскладке 
@bot.message_handler(func=lambda message: message.text == "---")
def handle_no_test(message):
    if current_language == "ru":
        text = "Тестирование данной дисциплины в этой раскладке языка нету, ожидайте."
    else:
        text = "Ushbu test joriy til sozlamalarida mavjud emas, iltimos kuting."
    bot.send_message(chat_id=message.chat.id, text=text)


# Курс 1

#Русский

@bot.message_handler(func=lambda message: message.text == "Тестирование по Гистологии 1")
def start_gistologiya_test_ru(message):
    text = "📚Введите количество вопросов, пример 30-60. 📝Тест содержит в себе 445 вопросов:"
    bot.send_message(chat_id=message.chat.id, text=text)
    file_path = os.path.join('Курс 1 RU', 'Гистология 1 курс.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        questions = json.load(file)
    bot.register_next_step_handler(message, set_questions_count, questions)

@bot.message_handler(func=lambda message: message.text == "Тестирование по Анатомии 1")
def start_anatomy1_test_ru(message):
    text = "📚Введите количество вопросов, пример 30-60. 📝Тест содержит в себе 605 вопросов:"
    bot.send_message(chat_id=message.chat.id, text=text)
    file_path = os.path.join('Курс 1 RU', 'Анатомия 1 курс.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        questions = json.load(file)
    bot.register_next_step_handler(message, set_questions_count, questions)

@bot.message_handler(func=lambda message: message.text == "Тестирование по Биологии 1")
def start_biology1_test_ru(message):
    text = "📚Введите количество вопросов, пример 30-60. 📝Тест содержит в себе 615 вопросов:"
    bot.send_message(chat_id=message.chat.id, text=text)
    file_path = os.path.join('Курс 1 RU', 'Биология 1 курс.json')
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        questions = json.load(file)
    bot.register_next_step_handler(message, set_questions_count, questions)
    
@bot.message_handler(func=lambda message: message.text == "Тестирование по Биофизике 1")
def start_biophysics1_test_ru(message):
    text = "📚Введите количество вопросов, пример 30-60. 📝Тест содержит в себе ХХХ вопросов:"
    bot.send_message(chat_id=message.chat.id, text=text)
    file_path = os.path.join('Курс 1 RU', 'Биофизика 1 курс.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        questions = json.load(file)
    bot.register_next_step_handler(message, set_questions_count, questions)



# Узбекский



@bot.message_handler(func=lambda message: message.text == "Gistologiya")
def start_gistologiya_test_uz(message):
    text = "📚Savollar sonini kiriting, masalan 30-60. 📝Testda 581 ta savol mavjud:"
    bot.send_message(chat_id=message.chat.id, text=text)
    file_path = os.path.join('Курс 1 UZ', '1 kurs gista UZ update.json')
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        questions = json.load(file)
    bot.register_next_step_handler(message, set_questions_count, questions)

@bot.message_handler(func=lambda message: message.text == "Anatomiya")
def start_anatomy1_test_uz(message):
    text = "📚Savollar sonini kiriting, masalan 30-60. 📝Testda 545 ta savol mavjud:"
    bot.send_message(chat_id=message.chat.id, text=text)
    file_path = os.path.join('Курс 1 UZ', 'анатомия 1 курс.json')
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        questions = json.load(file)
    bot.register_next_step_handler(message, set_questions_count, questions)

@bot.message_handler(func=lambda message: message.text == "Biologiya")
def start_biology1_test_uz(message):
    text = "📚Savollar sonini kiriting, masalan 30-60. 📝Testda 614 ta savol mavjud:"
    bot.send_message(chat_id=message.chat.id, text=text)
    file_path = os.path.join('Курс 1 UZ', 'Biologiya 1 kurs UZ.json')
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        questions = json.load(file)
    bot.register_next_step_handler(message, set_questions_count, questions)

@bot.message_handler(func=lambda message: message.text == "Biofizika")
def start_biophysics1_test_uz(message):
    text = "📚Savollar sonini kiriting, masalan 30-60. 📝Testda 400 ta savol mavjud:"
    bot.send_message(chat_id=message.chat.id, text=text)
    file_path = os.path.join('Курс 1 UZ', 'Биофизика UZ 1.json')
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        questions = json.load(file)
    bot.register_next_step_handler(message, set_questions_count, questions)

@bot.message_handler(func=lambda message: message.text == "Kimyo")
def start_chemistry1_test_uz(message):
    text = "📚Savollar sonini kiriting, masalan 30-60. 📝Testda 543 ta savol mavjud:"
    bot.send_message(chat_id=message.chat.id, text=text)
    file_path = os.path.join('Курс 1 UZ', 'Химия UZ 1.json')
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        questions = json.load(file)
    bot.register_next_step_handler(message, set_questions_count, questions)



# Курс 2

#Узбетский

@bot.message_handler(func=lambda message: message.text == "BKP")
def start_bcp_test_uz(message):
    text = "📚Savollar sonini kiriting, masalan 30-60. 📝Testda 616 ta savol mavjud:"
    bot.send_message(chat_id=message.chat.id, text=text)
    file_path = os.path.join('Курс 2 UZ', 'БКП.json')
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        questions = json.load(file)
    bot.register_next_step_handler(message, set_questions_count, questions)

@bot.message_handler(func=lambda message: message.text == "Fiziologiya")
def start_physiology1_test_uz(message):
    text = "📚Savollar sonini kiriting, masalan 30-60. 📝Testda 600 ta savol mavjud:"
    bot.send_message(chat_id=message.chat.id, text=text)
    file_path = os.path.join('Курс 2 UZ', 'Физиология.json')
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        questions = json.load(file)
    bot.register_next_step_handler(message, set_questions_count, questions)

@bot.message_handler(func=lambda message: message.text == "Biokimyo")
def start_biochemistry_test_uz(message):
    text = "📚Savollar sonini kiriting, masalan 30-60. 📝Testda 619 ta savol mavjud:"
    bot.send_message(chat_id=message.chat.id, text=text)
    file_path = os.path.join('Курс 2 UZ', 'Биохимия.json')
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        questions = json.load(file)
    bot.register_next_step_handler(message, set_questions_count, questions)

@bot.message_handler(func=lambda message: message.text == "ICP")
def start_icp_test_uz(message):
    text = "📚Savollar sonini kiriting, masalan 30-60. 📝Testda 600 ta savol mavjud:"
    bot.send_message(chat_id=message.chat.id, text=text)
    file_path = os.path.join('Курс 2 UZ', 'ИКП.json')
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        questions = json.load(file)
    bot.register_next_step_handler(message, set_questions_count, questions)



# Русский
@bot.message_handler(func=lambda message: message.text == "Тестирование по БКП 2")
def start_bcp_test(message):
    text = "📚Введите количество вопросов, например, от 30 до 60. 📝В тесте 616 вопросов:"
    bot.send_message(chat_id=message.chat.id, text=text)
    file_path = os.path.join('Курс 2 RU', 'БКП.json')
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        questions = json.load(file)
    bot.register_next_step_handler(message, set_questions_count, questions)
    
@bot.message_handler(func=lambda message: message.text == "Тестирование по Физиология 2")
def start_physiology_test(message):
    text = "📚Введите количество вопросов, например, от 30 до 60. 📝В тесте 600 вопросов:"
    bot.send_message(chat_id=message.chat.id, text=text)
    file_path = os.path.join('Курс 2 RU', 'Физиология.json')
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        questions = json.load(file)
    bot.register_next_step_handler(message, set_questions_count, questions)

@bot.message_handler(func=lambda message: message.text == "Тестирование по Биохимии 2")
def start_biochemistry_test(message):
    text = "📚Введите количество вопросов, например, от 30 до 60. 📝В тесте 620 вопросов:"
    bot.send_message(chat_id=message.chat.id, text=text)
    file_path = os.path.join('Курс 2 RU', 'Биохимия 2 курс Ру.json')
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        questions = json.load(file)
    bot.register_next_step_handler(message, set_questions_count, questions)



# Курс 3

# Русский

@bot.message_handler(func=lambda message: message.text == "Тест по БКП 3")
def start_bcp_test(message):
    text = "📚Введите количество вопросов, например, от 30 до 60. 📝В тесте 616 вопросов:"
    bot.send_message(chat_id=message.chat.id, text=text)
    file_path = os.path.join('Курс 3 RU', 'БКП.json')
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        questions = json.load(file)
    bot.register_next_step_handler(message, set_questions_count, questions)

@bot.message_handler(func=lambda message: message.text == "Тест по Фармакологии 3")
def start_physiology_test(message):
    text = "📚Введите количество вопросов, например, от 30 до 60. 📝В тесте 600 вопросов:"
    bot.send_message(chat_id=message.chat.id, text=text)
    file_path = os.path.join('Курс 3 RU', 'Фармакология.json')
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        questions = json.load(file)
    bot.register_next_step_handler(message, set_questions_count, questions)
    
@bot.message_handler(func=lambda message: message.text == "Тестирование по Патан 3")
def start_patan3_test(message):
    text = "📚Введите количество вопросов, например, от 30 до 60. 📝В тесте 748 вопросов:"
    bot.send_message(chat_id=message.chat.id, text=text)
    file_path = os.path.join('Курс 3 RU', 'Патан.json')
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        questions = json.load(file)
    bot.register_next_step_handler(message, set_questions_count, questions)

# Узбетский



# Функция для установки количества вопросов
def set_questions_count(message, questions):
    # Обработка кнопки "Назад"
    if message.text == ("Назад" if current_language == "ru" else "Orqaga"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        russian_btn = types.KeyboardButton("Русский")
        uzbek_btn = types.KeyboardButton("O'zbek")
        markup.add(russian_btn, uzbek_btn)
        msg = bot.send_message(
            chat_id=message.chat.id,
            text=("Выберите язык" if current_language == "ru" else "Tilni tanlang:"),
            reply_markup=markup
        )
        bot.register_next_step_handler(msg, send_welcome)
        return
    try:
        count_range = message.text.split('-')
        start = int(count_range[0])
        end = int(count_range[1])
        if 1 <= start <= end <= 750:
            user_id = message.chat.id
            user_results[user_id] = {
                "current_question": 0,
                "total_questions": end - start + 1,
                "questions": [questions[i - 1] for i in range(start, end + 1)]
            }
            send_question(message.chat.id)
        else:
            bot.send_message(message.chat.id, ("Некорректный формат ввода. Пожалуйста, введите число от 1 до 30." if current_language == "ru" else "Noto'g'ri formatda kiritildi. Iltimos, 1 dan 30 gacha raqam kiriting."))
            bot.register_next_step_handler(message, set_questions_count, questions)
    except (ValueError, IndexError):
        bot.send_message(message.chat.id, ("Некорректный формат ввода. Пожалуйста, введите число от 1 до 30." if current_language == "ru" else "Noto'g'ri formatda kiritildi. Iltimos, 1 dan 30 gacha raqam kiriting."))
        bot.register_next_step_handler(message, set_questions_count, questions)

# Функция для отправки вопроса пользователю
def send_question(chat_id):
    user_id = chat_id
    current_question = user_results[user_id]["current_question"]
    question = user_results[user_id]["questions"][current_question]

    options = question["Options"] + question["Answers"]
    random.shuffle(options)  # Рандомизация вариантов ответа
    options_text = "\n".join([f"{i + 1}. {option}" for i, option in enumerate(options)])
    message_text = f"{question['Number']}. {question['Text']}\n{options_text}"

    bot.send_message(chat_id, message_text)

    user_results[user_id]["current_options"] = options

    
    
# Обработчик ответов пользователя
@bot.message_handler(func=lambda message: message.chat.id in user_results)
def handle_answer(message):
    user_id = message.chat.id
    question_index = user_results[user_id]["current_question"]
    question = user_results[user_id]["questions"][question_index]
    options = user_results[user_id]["current_options"]
    correct_answers = [answer.lower() for answer in question["Answers"]]

    user_answers = message.text.strip().lower().split()
    parsed_answers = []
    for answer in user_answers:
        try:
            answer_index = int(answer) - 1
            if 0 <= answer_index < len(options):
                parsed_answers.append(options[answer_index].lower())
        except ValueError:
            parsed_answers.append(answer)

    # Проверка правильности ответов
    correct_count = sum(1 for answer in parsed_answers if answer in correct_answers)
    score = calculate_score(len(correct_answers), correct_count)
    user_results[user_id]["score"] = user_results[user_id].get("score", 0) + score

    if correct_count == len(correct_answers):
        bot.send_message(chat_id=user_id, text=f"Правильный ответ! ✅")
    elif correct_count == 0:
        bot.send_message(chat_id=user_id, text=f"Неправильный ответ. Вы не получили баллов.❌")
        bot.send_message(chat_id=user_id, text=f"Правильные ответы: {', '.join(correct_answers)}")
    else:
        bot.send_message(chat_id=user_id, text=f"Вы ввели {correct_count} из {len(correct_answers)} правильных ответов💡")
        bot.send_message(chat_id=user_id, text=f"Правильные ответы: {', '.join(correct_answers)}")

    user_results[user_id]["current_question"] += 1
    user_results[user_id]["questions"][question_index]["user_answers"] = parsed_answers

    if user_results[user_id]["current_question"] < user_results[user_id]["total_questions"]:
        send_question(user_id)
    else:
        total_score = user_results[user_id]["score"]
        max_score = user_results[user_id]["total_questions"] * 3.3
        percentage = (total_score / max_score) * 100
        result_message = f"🏁Тест завершен!\n\n📝Ваш итоговый балл: {total_score:.2f}/{max_score} ({percentage:.2f})"

        correct_count = sum(1 for question in user_results[user_id]["questions"] if set(question.get("user_answers", [])) == set([ans.lower() for ans in question["Answers"]]))
        incorrect_count = user_results[user_id]["total_questions"] - correct_count
        result_message += f"\n\n✅Правильных ответов: {correct_count}\n❌Неправильных ответов: {incorrect_count}"
        
        bot.send_message(chat_id=user_id, text=result_message)
        user_results.pop(user_id, None)

# Функция для подсчета баллов за правильный ответ
def calculate_score(correct_answers_count, correct_count):
    if correct_answers_count == 1:
        return 3.3 if correct_count == 1 else 0
    else:
        score_per_answer = 3.3 / correct_answers_count
        return round(score_per_answer * correct_count, 2)
    
# Запускаем бота
bot.polling()
