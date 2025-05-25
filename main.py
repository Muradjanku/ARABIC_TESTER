from telebot import TeleBot, types

bot = TeleBot("YOUR_BOT_TOKEN_HERE")

# Testlar ma'lumotlari (A1–A2)
a1_a2_tests = [
    {"question": "أنا ___ أمريكا.", "options": ["في", "من", "إلى", "مع"], "answer": "من"},
    {"question": "أنا ___.", "options": ["مصري", "فرنسي", "سعودي", "عراقي"], "answer": "فرنسي"},
    {"question": "هو ___ أحمد.", "options": ["يعمل", "اسمه", "ذهب", "صديقه"], "answer": "اسمه"},
    {"question": "___ أنت فرنسي؟", "options": ["أين", "متى", "هل", "كيف"], "answer": "هل"},
    {"question": "فاطمة ___ ولد.", "options": ["ليس", "عندها", "معها", "تسكن"], "answer": "عندها"},
    {"question": "أحمد ___ ولد وبنت.", "options": ["عنده", "يعمل", "ليس", "ذهب"], "answer": "عنده"},
    {"question": "بيت أحمد ___.", "options": ["صغير", "بعيد", "كبير", "قديم"], "answer": "كبير"},
    {"question": "___ بيت صغير.", "options": ["هذا", "هذه", "هناك", "ذلك"], "answer": "هذا"},
    {"question": "___ عندي سيارة.", "options": ["ليس", "عندها", "هناك", "معي"], "answer": "ليس"},
    {"question": "محمد ___ في الجامعة.", "options": ["يدرس", "يعمل", "يسكن", "يذهب"], "answer": "يعمل"},
    {"question": "سوزان تسكن ___ القاهرة.", "options": ["مع", "في", "إلى", "من"], "answer": "في"},
    {"question": "___ تذهب إلى الجامعة كل يوم.", "options": ["محمد", "سوزان", "فاطمة", "أحمد"], "answer": "فاطمة"},
    {"question": "___ تذهب إلى الجامعة؟", "options": ["أين", "متى", "لماذا", "كيف"], "answer": "متى"},
    {"question": "أحمد ذهب إلى الجامعة ___.", "options": ["اليوم", "غدا", "أمس", "الأسبوع"], "answer": "أمس"},
    {"question": "فاطمة ستزور سوزان ___.", "options": ["اليوم", "غدا", "أمس", "الأسبوع"], "answer": "غدا"},
    {"question": "محمد ___ يذهب إلى العمل غدا.", "options": ["سوف", "لن", "قد", "كان"], "answer": "لن"},
    {"question": "هم ___ يسافرون الأسبوع القادم.", "options": ["لن", "سوف", "قد", "كانوا"], "answer": "سوف"},
    {"question": "نحن سافرنا الأسبوع ___.", "options": ["القادم", "الماضي", "الحالي", "الجديد"], "answer": "الماضي"},
    {"question": "فاطمة ___ صديقتها أمس.", "options": ["درست", "زارت", "سافرت", "عملت"], "answer": "زارت"},
    {"question": "أحمد ___ يزر صديقه أمس.", "options": ["قد", "لم", "سوف", "كان"], "answer": "لم"},
    {"question": "أنا أعود ___ البيت الساعة الخامسة.", "options": ["من", "إلى", "في", "مع"], "answer": "إلى"},
    {"question": "زار صديقه ___ ذهب إلى السوق.", "options": ["قبل أن", "بعد أن", "لأن", "إذا"], "answer": "بعد أن"},
    {"question": "سأنام بعد أن ___ الفيلم.", "options": ["أكتب", "أشاهد", "أدرس", "أعمل"], "answer": "أشاهد"},
    {"question": "أريد ___ أشتري سيارة جديدة.", "options": ["إذا", "أن", "لأن", "كيف"], "answer": "أن"},
    {"question": "هم يحبون أن ___ اللغة العربية.", "options": ["يشاهدوا", "يدرسوا", "يعملوا", "يسافروا"], "answer": "يدرسوا"},
    {"question": "هذه صديقتي ___ تدرس في الجامعة.", "options": ["التي", "الذي", "التي هي", "الذين"], "answer": "التي"},
    {"question": "أين الكتب التي ___ أمس؟", "options": ["قرأتها", "اشتريتها", "كتبتها", "درستها"], "answer": "اشتريتها"},
    {"question": "أنا أدرس العربية ___ صديقي يدرس الفرنسية.", "options": ["أو", "بينما", "لكن", "إذا"], "answer": "بينما"},
    {"question": "لا أحب ___ إلى السوق.", "options": ["الذهاب", "القراءة", "العمل", "الدراسة"], "answer": "الذهاب"},
    {"question": "عدت إلى البيت بعد ___ صديقي.", "options": ["الدراسة", "مقابلة", "السفر", "العمل"], "answer": "مقابلة"},
    {"question": "نمت مبكرا ___ أصحو مبكرا.", "options": ["لأن", "لكي", "إذا", "بعد"], "answer": "لكي"},
    {"question": "كنت طالبا و___ مدرسا.", "options": ["سأكون", "أصبحت", "كنت", "أكون"], "answer": "أصبحت"},
    {"question": "قرأت أربعة ___ خلال الإجازة.", "options": ["أفلام", "كتب", "أماكن", "أيام"], "answer": "كتب"},
    {"question": "غادرت القاهرة ولم ___ أسكن فيها.", "options": ["أبدأ", "أعد", "أذهب", "أعمل"], "answer": "أعد"},
    {"question": "بدأت العمل ___.", "options": ["متعبا", "مسرورا", "حزينا", "مشغولا"], "answer": "مسرورا"},
    {"question": "انتشر الخبر ___ واسعا.", "options": ["قراءة", "انتشارا", "سفرا", "عملا"], "answer": "انتشارا"},
    {"question": "توقفت عن التدخين ___ من الأمراض.", "options": ["حبا", "خوفا", "فرحا", "رغبة"], "answer": "خوفا"},
    {"question": "___ علمت أنك مريض لزرتك.", "options": ["إذا", "لو", "لأن", "بعد"], "answer": "لو"},
]

# /start komandasi
def send_main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📝 Testlar", "📚 Lug‘at")
    markup.add("📖 Kitoblar", "🔙 Orqaga")
    bot.send_message(message.chat.id, "Kerakli bo‘limni tanlang:", reply_markup=markup)

@bot.message_handler(commands=['start'])
def start(message):
    send_main_menu(message)

# Testlar bo‘limi
@bot.message_handler(func=lambda msg: msg.text == "📝 Testlar")
def test_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("A1–A2", "B1–B2", "C1–C2")
    markup.add("🔙 Orqaga")
    bot.send_message(message.chat.id, "Test darajasini tanlang:", reply_markup=markup)

# A1-A2 Test boshlanishi
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

# Orqaga
@bot.message_handler(func=lambda msg: msg.text == "🔙 Orqaga")
def go_back(message):
    send_main_menu(message)

print("Bot ishga tushdi...")
bot.infinity_polling()
