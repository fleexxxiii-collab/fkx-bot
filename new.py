import telebot
from telebot import types
import sqlite3

# =========================
# BOT TOKEN
# =========================

BOT_TOKEN = "8588322813:AAFaz2QuMxLfaBKznrU2JVMFXV4G2biWofA"

bot = telebot.TeleBot(BOT_TOKEN)

# =========================
# ADMINS
# =========================

ADMINS = [
    6047449871,
]

# =========================
# IMAGE IDS
# =========================

START_IMAGE = "AgACAgQAAxkBAANBahpiVC7tU0yOj1HOa0rwpaQM5TcAAhEPaxteCtFQNgW7RuTFy08BAAMCAAN5AAM7BA"

DONE_IMAGE = "AgACAgQAAxkBAANBahpiVC7tU0yOj1HOa0rwpaQM5TcAAhEPaxteCtFQNgW7RuTFy08BAAMCAAN5AAM7BA"

# =========================
# SQLITE DATABASE
# =========================

conn = sqlite3.connect(
    "fkx.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    banned INTEGER DEFAULT 0
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    package TEXT,
    status TEXT
)
""")

conn.commit()

# =========================
# BOT STATES
# =========================

waiting_payment = {}
waiting_details = set()
broadcast_mode = {}


# =========================
# SAVE USER
# =========================

def save_user(user):

    cursor.execute(
        """
        INSERT OR IGNORE INTO users
        (user_id, username)
        VALUES (?,?)
        """,
        (
            user.id,
            str(user.username)
        )
    )

    conn.commit()

# =========================
# START BUTTON
# =========================

@bot.message_handler(commands=["start"])
def start(message):

    save_user(message.from_user)

    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    markup.row("🔥 Free Fire")
    markup.row("🎮 PUBG")
    markup.row("📩 Other")
    markup.row("📦 My Orders")

    bot.send_photo(
        message.chat.id,
        START_IMAGE,
        caption="""
🔥 WELCOME TO FKX ONLINE MARKET 🔥

What can I help you today?
""",
        reply_markup=markup
    )
# =========================
# FREE FIRE MENU
# =========================

@bot.message_handler(func=lambda m: m.text == "🔥 Free Fire")
def free_fire_menu(message):

    markup = types.InlineKeyboardMarkup(row_width=1)

    buttons = [
        ("💎 100 + 10 Diamonds → 190 Birr", "ff_110"),
        ("💎 200 + 20 Diamonds → 380 Birr", "ff_220"),
        ("💎 535 + 50 Diamonds → 1050 Birr", "ff_585"),
        ("💎 1000 + 108 Diamonds → 1850 Birr", "ff_1108"),
        ("💎 2200 + 220 Diamonds → 3700 Birr", "ff_2420"),
        ("💎 5600 + 600 Diamonds → 8950 Birr", "ff_6200"),
        ("🎫 Booyah Pass → 600 Birr", "ff_booyah"),
        ("📅 Monthly Membership → 2200 Birr", "ff_monthly"),
        ("⚡ Weekly Membership → 450 Birr", "ff_weekly")
    ]

    for text, data in buttons:
        markup.add(
            types.InlineKeyboardButton(
                text=text,
                callback_data=data
            )
        )

    bot.send_message(
        message.chat.id,
        "🔥 Select a Free Fire package:",
        reply_markup=markup
    )

# =========================
# FREE FIRE PACKAGE NAMES
# =========================

FF_PACKAGES = {
    "ff_110": "100 + 10 Diamonds",
    "ff_220": "200 + 20 Diamonds",
    "ff_585": "535 + 50 Diamonds",
    "ff_1108": "1000 + 108 Diamonds",
    "ff_2420": "2200 + 220 Diamonds",
    "ff_6200": "5600 + 600 Diamonds",
    "ff_booyah": "Booyah Pass",
    "ff_monthly": "Monthly Membership",
    "ff_weekly": "Weekly Membership"
}
# =========================
# PUBG MENU
# =========================

@bot.message_handler(func=lambda m: m.text == "🎮 PUBG")
def pubg_menu(message):

    markup = types.InlineKeyboardMarkup(row_width=1)

    packages = [
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

    for text, data in packages:
        markup.add(
            types.InlineKeyboardButton(
                text=text,
                callback_data=data
            )
        )

    bot.send_message(
        message.chat.id,
        "🎮 Select a PUBG package:",
        reply_markup=markup
    )

# =========================
# PUBG PACKAGE NAMES
# =========================

PUBG_PACKAGES = {
    "pubg_60": "60 UC",
    "pubg_90": "90 UC",
    "pubg_120": "120 UC",
    "pubg_180": "180 UC",
    "pubg_200": "200 UC",
    "pubg_240": "240 UC",
    "pubg_325": "325 UC",
    "pubg_355": "355 UC",
    "pubg_360": "360 UC",
    "pubg_385": "385 UC",
    "pubg_415": "415 UC",
    "pubg_445": "445 UC",
    "pubg_475": "475 UC",
    "pubg_505": "505 UC",
    "pubg_660": "660 UC",
    "pubg_720": "720 UC",
    "pubg_780": "780 UC",
    "pubg_810": "810 UC",
    "pubg_1020": "1020 UC",
    "pubg_1105": "1105 UC",
    "pubg_1440": "1440 UC",
    "pubg_1800": "1800 UC",
    "pubg_2125": "2125 UC",
    "pubg_3850": "3850 UC",
    "pubg_8100": "8100 UC"
}
# =========================
# OTHER
# =========================

@bot.message_handler(func=lambda m: m.text == "📩 Other")
def other_menu(message):

    bot.send_message(
        message.chat.id,
        """
📩 Contact Owner

👤 @et_flexi
👤 @fkx_markett

Send your request directly.
"""
    )
# =========================
# WAITING FOR SCREENSHOT
# =========================

waiting_payment = {}
broadcast_mode = {}

# =========================
# PACKAGE CALLBACK
# =========================

@bot.callback_query_handler(
    func=lambda call:
    call.data.startswith("ff_")
    or
    call.data.startswith("pubg_")
)
def package_selected(call):

    user_id = call.from_user.id

    if call.data in FF_PACKAGES:
        package = FF_PACKAGES[call.data]

    elif call.data in PUBG_PACKAGES:
        package = PUBG_PACKAGES[call.data]

    else:
        return

    waiting_payment[user_id] = package

    cursor.execute(
        """
        INSERT INTO orders
        (user_id, package, status)
        VALUES (?, ?, ?)
        """,
        (
            user_id,
            package,
            "WAITING_PAYMENT"
        )
    )

    conn.commit()

    bot.send_message(
        user_id,
        f"""
✅ Package Selected

📦 {package}

━━━━━━━━━━━━━━━━━━━

🩸 PAYMENT METHODS ✅

🏦 Telebirr : 0919303975

🏦 Name : GETACHEW

🏝 CBE : COMING SOON

━━━━━━━━━━━━━━━━━━━

⚠️ SEND PAYMENT SCREENSHOT AFTER PAYMENT
"""
    )

    bot.answer_callback_query(call.id)
# =========================
# PAYMENT SCREENSHOT
# =========================

@bot.message_handler(content_types=['photo'])
def payment_screenshot(message):

    user_id = message.from_user.id

    if user_id not in waiting_payment:
        return

    package = waiting_payment[user_id]

    markup = types.InlineKeyboardMarkup()

    approve = types.InlineKeyboardButton(
        "✅ Approve",
        callback_data=f"approve_{user_id}"
    )

    reject = types.InlineKeyboardButton(
        "❌ Reject",
        callback_data=f"reject_{user_id}"
    )

    ban = types.InlineKeyboardButton(
        "🚫 Ban",
        callback_data=f"ban_{user_id}"
    )

    markup.add(approve)
    markup.add(reject)
    markup.add(ban)

    caption = f"""
💰 PAYMENT RECEIVED

👤 User ID: {user_id}

📦 Package:
{package}

Approve or Reject
"""

    for admin in ADMINS:

        bot.send_photo(
            admin,
            message.photo[-1].file_id,
            caption=caption,
            reply_markup=markup
        )

    bot.send_message(
    user_id,
    """
✅ Screenshot Sent

Please wait for admin approval.
"""
)

    cursor.execute(
        """
        UPDATE orders
        SET status=?
        WHERE user_id=?
        """,
        (
            "PAYMENT_REVIEW",
            user_id
        )
    )

    conn.commit()

    # =========================
# APPROVE PAYMENT
# =========================

@bot.callback_query_handler(
    func=lambda call:
    call.data.startswith("approve_")
)
def approve_payment(call):

    user_id = int(
        call.data.split("_")[1]
    )

    waiting_details.add(user_id)

    cursor.execute(
        """
        UPDATE orders
        SET status=?
        WHERE user_id=?
        """,
        (
            "WAITING_DETAILS",
            user_id
        )
    )

    conn.commit()

    bot.send_message(
        user_id,
        """
✅ PAYMENT APPROVED

━━━━━━━━━━━━━━━

Please send your account details.

Examples:

🔥 Free Fire
UID: xxxxxxxx

🎮 PUBG
ID: xxxxxxxx

📧 Email:
xxxxxxxx@gmail.com

━━━━━━━━━━━━━━━

Send all required details now.
"""
    )

    bot.answer_callback_query(
        call.id,
        "Payment Approved"
    )

    # =========================
# REJECT PAYMENT
# =========================

warnings = {}

@bot.callback_query_handler(
    func=lambda call:
    call.data.startswith("reject_")
)
def reject_payment(call):

    user_id = int(
        call.data.split("_")[1]
    )

    if user_id not in warnings:
        warnings[user_id] = 0

    warnings[user_id] += 1

    bot.send_message(
        user_id,
        f"""
❌ PAYMENT REJECTED

Warning:
{warnings[user_id]}/5

Please send a valid screenshot.
"""
    )

    bot.answer_callback_query(
        call.id,
        "Payment Rejected"
    )

# =========================
# BAN USER
# =========================

@bot.callback_query_handler(
    func=lambda call:
    call.data.startswith("ban_")
)
def ban_user(call):

    user_id = int(
        call.data.split("_")[1]
    )

    cursor.execute(
        """
        UPDATE users
        SET banned=1
        WHERE user_id=?
        """,
        (user_id,)
    )

    conn.commit()

    bot.send_message(
        user_id,
        "🚫 You have been banned from FKX Market."
    )

    bot.answer_callback_query(
        call.id,
        "User Banned"
    )

# =========================
# ACCOUNT DETAILS
# =========================

@bot.message_handler(
    func=lambda message:
    message.from_user.id in waiting_details
)
def receive_account_details(message):

    user_id = message.from_user.id

    details = message.text

    waiting_details.remove(user_id)

    cursor.execute(
        """
        UPDATE orders
        SET status=?
        WHERE user_id=?
        """,
        (
            "PENDING",
            user_id
        )
    )

    conn.commit()

    bot.send_message(
        user_id,
        """
⏳ YOUR ORDER IS NOW PENDING

Please wait 1-15 minutes.

We will notify you when
your order is completed.
"""
    )

    markup = types.InlineKeyboardMarkup()

    done_btn = types.InlineKeyboardButton(
        "✅ ORDER DONE",
        callback_data=f"done_{user_id}"
    )

    markup.add(done_btn)

    for admin in ADMINS:

        bot.send_message(
            admin,
            f"""
🔥 NEW ACCOUNT DETAILS

👤 USER ID:
{user_id}

━━━━━━━━━━━━━━━

{details}

━━━━━━━━━━━━━━━

Press DONE after topup.
""",
            reply_markup=markup
        )
# =========================
# DONE ORDER
# =========================

@bot.callback_query_handler(
    func=lambda call:
    call.data.startswith("done_")
)
def done_order(call):

    user_id = int(
        call.data.split("_")[1]
    )

    cursor.execute(
        """
        UPDATE orders
        SET status=?
        WHERE user_id=?
        """,
        (
            "DONE",
            user_id
        )
    )

    conn.commit()

    bot.send_photo(
        user_id,
        DONE_IMAGE,
        caption="""
🎉 YOUR ORDER IS COMPLETED

━━━━━━━━━━━━━━━

✅ FKX MARKET

💯 100% TRUSTED

Thank you for choosing us ❤️
"""
    )

    bot.answer_callback_query(
        call.id,
        "Order Completed"
    )
# =========================
# MY ORDERS
# =========================

@bot.message_handler(
    func=lambda m: m.text == "📦 My Orders"
)
def my_orders(message):

    user_id = message.from_user.id

    cursor.execute(
        """
        SELECT package,status
        FROM orders
        WHERE user_id=?
        ORDER BY order_id DESC
        LIMIT 10
        """,
        (user_id,)
    )

    rows = cursor.fetchall()

    if not rows:

        bot.send_message(
            user_id,
            "❌ No orders found."
        )
        return

    text = "📦 YOUR ORDERS\n\n"

    for package, status in rows:

        text += f"""
📦 {package}
📍 Status: {status}

"""

    bot.send_message(
        user_id,
        text
    )
# =========================
# BROADCAST COMMAND
# =========================

broadcast_mode = {}

@bot.message_handler(
    commands=["broadcast"]
)
def broadcast_command(message):

    if message.from_user.id not in ADMINS:
        return

    broadcast_mode[
        message.from_user.id
    ] = True

    bot.reply_to(
        message,
        "📢 Send broadcast message."
    )

# =========================
# SEND BROADCAST
# =========================

@bot.message_handler(
    func=lambda m:
    m.from_user.id in broadcast_mode
)
def send_broadcast(message):

    admin_id = message.from_user.id

    del broadcast_mode[admin_id]

    cursor.execute(
        "SELECT user_id FROM users"
    )

    users = cursor.fetchall()

    sent = 0

    for user in users:

        try:

            bot.send_message(
                user[0],
                f"""
📢 FKX MARKET

{message.text}
"""
            )

            sent += 1

        except:
            pass

    bot.send_message(
        admin_id,
        f"✅ Broadcast sent to {sent} users."
    )
# =========================
# RUN BOT
# =========================

print("🔥 FKX BOT RUNNING 🔥")

bot.infinity_polling(
    skip_pending=True
)
