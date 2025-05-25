from telebot import TeleBot, types
from config import TOKEN

bot = TeleBot(TOKEN)

# Testlar ma'lumotlari (A1–A2)
a1_a2_tests = [
    {"question": "أنا ___ أمريكا.", "options": ["في", "من", "إلى", "مع"], "answer": "من"},
    {"question": "أنا ___.", "options": ["مصري", "فرنسي", "سعودي", "عراقي"], "answer": "فرنسي"},
    # ... qolgan testlar shu yerda ...
]

def send_main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📝 Testlar", "📚 Lug‘at")
    markup.add("📖 Kitoblar", "🔙 Orqaga")
    bot.send_message(message.chat.id, "Kerakli bo‘limni tanlang:", reply_markup=markup)

@bot.message_handler(commands=['start'])
def start(message):
    send_main_menu(message)

@bot.message_handler(func=lambda msg: msg.text == "📝 Testlar")
def test_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("A1–A2", "B1–B2", "C1–C2")
    markup.add("🔙 Orqaga")
    bot.send_message(message.chat.id, "Test darajasini tanlang:", reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text == "A1–A2")
def start_a1_tests(message):
    bot.send_message(message.chat.id, "A1–A2 testlar boshlandi.")
    ask_test_question(message.chat.id, 0)

def ask_test_question(chat_id, index):
    if index < len(a1_a2_tests):
        q = a1_a2_tests[index]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        for opt in q['options']:
            markup.add(opt)
        msg = bot.send_message(chat_id, q['question'], reply_markup=markup)
        bot.register_next_step_handler(msg, check_answer, index)
    else:
        bot.send_message(chat_id, "Test tugadi. ✅")

def check_answer(message, index):
    correct = a1_a2_tests[index]['answer']
    if message.text == correct:
        bot.send_message(message.chat.id, "✅ To‘g‘ri")
    else:
        bot.send_message(message.chat.id, f"❌ Noto‘g‘ri. To‘g‘ri javob: {correct}")
    ask_test_question(message.chat.id, index + 1)

@bot.message_handler(func=lambda msg: msg.text == "🔙 Orqaga")
def go_back(message):
    send_main_menu(message)

print("Bot ishga tushdi...")
bot.infinity_polling()
