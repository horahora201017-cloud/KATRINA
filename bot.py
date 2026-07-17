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
    for member in update.message.new_chat_members:
        await update.message.reply_text(
            f"🌸 أهلاً وسهلاً {member.mention_html()}\n\n"
            "💜 نورت كروب KATRINA.\n"
            "📜 اقرأ القوانين بالأمر /rules\n"
            "✨ نتمنى لك وقتًا ممتعًا.",
            parse_mode="HTML",
        )


app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("id", user_id))
app.add_handler(CommandHandler("rules", rules))
app.add_handler(CallbackQueryHandler(button))
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
app.run_polling()
