# KATRINA v1.4
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🌸 أهلاً بك في KATRINA 🤖\n\n"
        "بوت إدارة وحماية متطور.\n\n"
        "📖 استخدم /help لعرض قائمة الأوامر.\n"
        "📜 استخدم /rules لعرض قوانين المجموعة.\n\n"
        "🌍 اختر لغتك من الأزرار بالأسفل."
    )
    keyboard = [
        [InlineKeyboardButton("🇮🇶 العربية", callback_data="lang_ar")],
        [InlineKeyboardButton("🇺🇸 English", callback_data="lang_en")],
    ]
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "lang_ar":
        await query.edit_message_text("✅ تم اختيار اللغة العربية 🇮🇶")

    elif query.data == "lang_en":
        await query.edit_message_text("✅ English language selected 🇺🇸")

    elif query.data == "admin":
        await query.edit_message_text(
            "👮 إدارة KATRINA\n\n"
            "إذا واجهت أي مشكلة تواصل مع إدارة المجموعة."
        )

    elif query.data == "rules":
        await query.edit_message_text(
            "📜 قوانين المجموعة:\n\n"
            "1- احترام الجميع.\n"
            "2- يمنع السب.\n"
            "3- يمنع الروابط.\n"
            "4- يمنع السبام.\n"
            "5- يمنع طلب الخاص."
        )


async def user_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🆔 آيديك هو: `{update.effective_user.id}`",
        parse_mode="Markdown",
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 قائمة الأوامر:\n\n"
        "/start\n/help\n/id\n/rules"
    )


async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📜 قوانين المجموعة:\n\n"
        "1. احترام الجميع.\n"
        "2. يمنع السب والشتم.\n"
        "3. يمنع الروابط والإعلانات.\n"
        "4. يمنع السبام.\n"
        "5. يمنع طلب الخاص.\n"
        "6. الالتزام بتعليمات الإدارة."
    )

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    keyboard = [
        [
            InlineKeyboardButton("👮 الإدارة", callback_data="admin"),
            InlineKeyboardButton("📜 القوانين", callback_data="rules"),
        ],
        [
            InlineKeyboardButton(
                "📢 قناتنا",
                url="https://t.me/Silas0001"
            )
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    for member in update.message.new_chat_members:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"""🌸 <b>KATRINA</b>

✨ أهلاً وسهلاً بك

👤 {member.mention_html()}

💜 وجودك أسعدنا بانضمامك إلى عائلتنا الراقية.

احترم الجميع، والتزم بالقوانين، ونتمنى لك وقتاً ممتعاً معنا.

🤍 شكراً لانضمامك.""",
            parse_mode="HTML",
            reply_markup=reply_markup,
        )

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.strip().lower()

    replies = {
        "كاترينا": "نعم؟ 🌸",
        "بوت": "معكم KATRINA 🤖",
        "هلو": "هلا وغلا 💜",
        "السلام عليكم": "وعليكم السلام ورحمة الله وبركاته 🌸",
        "صباح الخير": "صباح النور والسرور ☀️",
        "مساء الخير": "مساء الورد 🌹",
    }

    if text == "معلومات" and update.message.reply_to_message:
        await user_info(update, context)
        return

    if text in replies:
        await update.message.reply_text(replies[text])

async def user_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.reply_to_message:
        return

    user = update.message.reply_to_message.from_user

    username = f"@{user.username}" if user.username else "لا يوجد"

    text = (
        f"👤 معلومات العضو\n\n"
        f"🆔 الآيدي: {user.id}\n"
        f"📛 الاسم: {user.full_name}\n"
        f"🔗 اليوزر: {username}\n"
        f"🤖 بوت: {'نعم' if user.is_bot else 'لا'}"
    )

    await update.message.reply_text(text)

async def delete_links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    member = await context.bot.get_chat_member(
        update.effective_chat.id,
        update.effective_user.id,
    )

    if member.status in ["administrator", "creator"]:
        return

    text = update.message.text.lower()

    if (
        "http://" in text
        or "https://" in text
        or "t.me/" in text
        or "telegram.me/" in text
    ):
        await update.message.delete()
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"🚫 {update.effective_user.mention_html()} يمنع إرسال الروابط.",
            parse_mode="HTML",
        )
        return

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("id", user_id))
app.add_handler(CommandHandler("rules", rules))

app.add_handler(CallbackQueryHandler(button))

app.add_handler(
    MessageHandler(
        filters.StatusUpdate.NEW_CHAT_MEMBERS,
        welcome,
    )
)

app.add_handler(
    MessageHandler(
        filters.TEXT & filters.Regex(r"(http://|https://|t\.me/|telegram\.me/)"),
        delete_links,
    )
)

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        auto_reply,
    )
)

app.run_polling(
    allowed_updates=Update.ALL_TYPES
)
