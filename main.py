import telebot
from telebot import types
import telebot.apihelper

telebot.apihelper.proxy = {}
# 👇 PASTE HERE (Step 2)
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    file_id = message.photo[-1].file_id
    print("FILE ID:", file_id)
    bot.reply_to(message, f"File ID:\n{file_id}")

# your other commands
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Send me an image and I will give you file_id")


# =========================
# FKX ONLINE MARKET BOT
# =========================

BOT_TOKEN = "8394617212:AAFDYaVyrc9GhbF6Oa3LD5evpItP-2UEgzw"

OWNER_IDS = [6047449871,]

bot = telebot.TeleBot(BOT_TOKEN)

warnings = {}
banned_users = set()
users = set()
user_orders = {}


# =========================
# START
# =========================

@bot.message_handler(commands=['start'])
def start(message):

    user_id = message.from_user.id
    users.add(user_id)

    if user_id in banned_users:
        bot.send_message(
            user_id,
            "❌ You are banned from this bot."
        )
        return

    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    btn1 = types.KeyboardButton("🔥 Free Fire")
    btn2 = types.KeyboardButton("🎮 PUBG")
    btn3 = types.KeyboardButton("📩 Other")

    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)

    photo = open("FKX.JPG", "rb")

    caption = """
🔥 WELCOME TO FKX ONINE MARKET BOT 🔥

💎 CHEAP & FAST TOP UP
✅ TRUSTED SERVICE
⚡ INSTANT DELIVERY

Choose a service below:
"""

    bot.send_photo(
        message.chat.id,
        photo,
        caption=caption,
        reply_markup=markup
    )

# =========================
# FREE FIRE BUTTONS
# =========================

@bot.message_handler(func=lambda m: m.text == "🔥 Free Fire")
def freefire(message):

    markup = types.InlineKeyboardMarkup()

    ff_prices = [
        
        ("💎 100 + 10 Diamonds → 190 Birr", "ff_110"),
        ("💎 200 + 20 Diamonds → 380 Birr", "ff_220"),
        ("💎 535 + 50 Diamonds → 1050 Birr", "ff_585"),
        ("💎 1000 + 108 Diamonds → 1850 Birr", "ff_1108"),
        ("💎 2200 + 220 Diamonds → 3700 Birr", "ff_2420"),
        ("💎 5600 + 600 Diamonds → 8950 Birr", "ff_6200"),

        ("🎫 Booyah Pass → 600 Birr", "ff_booyah"),
        ("📅 Monthly Membership → 2200 Birr", "ff_monthly"),
        ("⚡️ Weekly Membership → 450 Birr", "ff_weekly")
    ]

    for text, data in ff_prices:
        markup.add(types.InlineKeyboardButton(text, callback_data=data))

    bot.send_message(
        message.chat.id,
        "💎 Choose Free Fire Package:",
        reply_markup=markup
    )

# =========================
# PUBG BUTTONS
# =========================

@bot.message_handler(func=lambda m: m.text == "🎮 PUBG")
def pubg(message):

    markup = types.InlineKeyboardMarkup()

    pubg_prices = [
        ("60 UC = 210 Birr", "pubg_60"),
        ("90 UC = 370 Birr", "pubg_90"),
        ("120 UC = 390 Birr", "pubg_120"),
        ("180 UC = 580 Birr", "pubg_180"),
        ("200 UC = 630 Birr", "pubg_200"),
        ("240 UC = 730 Birr", "pubg_240"),
        ("325 UC = 880 Birr", "pubg_325"),
        ("355 UC = 1000 Birr", "pubg_355"),
        ("360 UC = 1060 Birr", "pubg_360"),
        ("385 UC = 1080 Birr", "pubg_385"),
        ("415 UC = 1180 Birr", "pubg_415"),
        ("445 UC = 1280 Birr", "pubg_445"),
        ("475 UC = 1380 Birr", "pubg_475"),
        ("505 UC = 1460 Birr", "pubg_505"),
        ("660 UC = 1730 Birr", "pubg_660"),
        ("720 UC = 1880 Birr", "pubg_720"),
        ("780 UC = 2080 Birr", "pubg_780"),
        ("810 UC = 2130 Birr", "pubg_810"),
        ("1020 UC = 2630 Birr", "pubg_1020"),
        ("1105 UC = 2780 Birr", "pubg_1105"),
        ("1440 UC = 3580 Birr", "pubg_1440"),
        ("1800 UC = 4080 Birr", "pubg_1800"),
        ("2125 UC = 4840 Birr", "pubg_2125"),
        ("3850 UC = 8050 Birr", "pubg_3850"),
        ("8100 UC = 16760 Birr", "pubg_8100")

    ]

    for text, data in pubg_prices:
        markup.add(types.InlineKeyboardButton(text, callback_data=data))

    bot.send_message(
        message.chat.id,
        "🏆 Choose PUBG Package:",
        reply_markup=markup
    )

# =========================
# OTHER
# =========================

@bot.message_handler(func=lambda m: m.text == "📩 Other")
def other(message):

    bot.send_message(
        message.chat.id,
        "📩 Please DM the owner for other services @PIXEL_TOP_UP_1."
    )

## =========================
# CALLBACKS
# =========================

@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    data = call.data

    if data.startswith("done_"):

        user_id = int(data.split("_")[1])

        photo = open("FKX.JPG", "rb")

        caption = """
✅ YOUR ORDER IS DONE!

🔥 FKX MARKET 💯 TRUSTED 🔥

📩 DM TO BUY MORE
"""

        bot.send_photo(
            user_id,
            photo,
            caption=caption
        )

        bot.answer_callback_query(
            call.id,
            "Order completed"
        )
        bot.answer_callback_query(call.id, "Order completed")
    # =====================
    # PRODUCT CHOOSE
    # =====================

    if data.startswith("ff_") or data.startswith("pubg_"):
        
        selected = data.replace("_", " ").upper()
        user_orders[call.from_user.id] = selected
        payment_text = f"""
✅ YOU SELECTED:

{selected}

━━━━━━━━━━━━━━━━━━━

🩸 PAYMENT METHODS ✅

🏦 Telebirr : 0919303975
🏦 Name : GETACHEW 

🏝 CBE: COMMING SOON


━━━━━━━━━━━━━━━━━━━

⚠️ SEND PAYMENT SCREENSHOT AFTER PAYMENT
"""

        bot.send_message(
            call.message.chat.id,
            payment_text
        )

        bot.send_message(
            call.message.chat.id,
            "📸 Now send your payment screenshot proof."
        )

    # =====================
    # APPROVE
    # =====================

    elif data.startswith("approve_"):

        user_id = int(data.split("_")[1])

        bot.send_message(
            user_id,
            "✅ PAYMENT APPROVED!\n\n📩 Now send your UID / EMAIL / ACCOUNT."
        )

        bot.answer_callback_query(call.id, "Approved")

    # =====================
    # REJECT
    # =====================

    elif data.startswith("reject_"):

        user_id = int(data.split("_")[1])

        warnings[user_id] = warnings.get(user_id, 0) + 1

        count = warnings[user_id]

        if count >= 5:

            banned_users.add(user_id)

            bot.send_message(
                user_id,
                "❌ You are banned for sending fake proofs."
            )

        else:

            bot.send_message(
                user_id,
                f"⚠️ Fake proof!\nWarning {count}/5"
            )

        bot.answer_callback_query(call.id, "Rejected")

# =========================
# RECEIVE SCREENSHOT
# =========================

@bot.message_handler(content_types=['photo'])
def photo(message):

    user = message.from_user

    order = user_orders.get(user.id, "UNKNOWN ORDER")

    caption = f"""
📥 NEW PAYMENT PROOF

🛒 ORDER: {order}

👤 USER: @{user.username}
🆔 ID: {user.id}
"""

    markup = types.InlineKeyboardMarkup()

    approve = types.InlineKeyboardButton(
        "✅ APPROVE",
        callback_data=f"approve_{user.id}"
    )

    reject = types.InlineKeyboardButton(
        "❌ FAKE",
        callback_data=f"reject_{user.id}"
    )

    markup.add(approve, reject)

    for owner in OWNER_IDS:

        bot.send_photo(
            owner,
            message.photo[-1].file_id,
            caption=caption,
            reply_markup=markup
        )

    bot.send_message(
        message.chat.id,
        "⏳ WAITING FOR ADMIN APPROVAL..."
    )

# =========================
# USER UID / ACCOUNT
# =========================

@bot.message_handler(func=lambda m: True)
def user_data(message):

    if message.text.startswith("/"):
        return

    markup = types.InlineKeyboardMarkup()

    done_btn = types.InlineKeyboardButton(
        "✅ DONE",
        callback_data=f"done_{message.from_user.id}"
    )

    markup.add(done_btn)

    for owner in OWNER_IDS:

        bot.send_message(
            owner,
            f"""
📩 USER ACCOUNT INFO

👤 USER ID: {message.from_user.id}

📝 DATA:
{message.text}
""",
            reply_markup=markup
        )
        

# =====================
# DONE BUTTON
# =====================


# =========================
# BAN
# =========================

@bot.message_handler(commands=['ban'])
def ban(message):

    if message.from_user.id not in OWNER_IDS:
        return

    try:

        user_id = int(message.text.split()[1])

        banned_users.add(user_id)

        bot.reply_to(
            message,
            f"✅ USER {user_id} BANNED"
        )

    except:

        bot.reply_to(
            message,
            "Usage:\n/ban USER_ID"
        )

# =========================
# UNBAN
# =========================

@bot.message_handler(commands=['unban'])
def unban(message):

    if message.from_user.id not in OWNER_IDS:
        return

    try:

        user_id = int(message.text.split()[1])

        banned_users.discard(user_id)

        bot.reply_to(
            message,
            f"✅ USER {user_id} UNBANNED"
        )

    except:

        bot.reply_to(
            message,
            "Usage:\n/unban USER_ID"
        )

# =========================
# BROADCAST
# =========================

@bot.message_handler(commands=['broadcast'])
def broadcast(message):

    if message.from_user.id not in OWNER_IDS:
        return

    text = message.text.replace("/broadcast ", "")

    sent = 0

    for user_id in users:

        try:

            bot.send_message(
                user_id,
                f"📢 BROADCAST\n\n{text}"
            )

            sent += 1

        except:
            pass

    bot.reply_to(
        message,
        f"✅ SENT TO {sent} USERS"
    )

# =========================
# RUN BOT
# =========================

print("🔥 FKX BOT RUNNING 🔥")
bot.infinity_polling(skip_pending=True)

bot.infinity_polling()
