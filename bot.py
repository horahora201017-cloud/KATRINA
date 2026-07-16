# KATRINA v1.2

import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🌸 أهلاً بك في KATRINA 🤖\n\n"
        "بوت إدارة وحماية متطور.\n\n"
        "📖 استخدم /help لعرض قائمة الأوامر.\n"
        "📜 استخدم /rules لعرض قوانين المجموعة.\n\n"
        "✨ نتمنى لك تجربة ممتعة."
    )
    await update.message.reply_text(text)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📖 قائمة الأوامر:\n\n"
        "/start - بدء استخدام البوت\n"
        "/help - عرض قائمة الأوامر\n"
        "/rules - عرض قوانين المجموعة"
    )
    await update.message.reply_text(text)


async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📜 قوانين المجموعة:\n\n"
        "1. احترام جميع الأعضاء.\n"
        "2. يمنع السب والشتم أو الإساءة.\n"
        "3. يمنع إرسال الروابط أو الإعلانات دون إذن.\n"
        "4. يمنع الإزعاج أو السبام.\n"
        "5. يمنع طلب أو إرسال الخاص دون موافقة الطرف الآخر.\n"
        "6. يمنع التحدث في السياسة أو إثارة الفتن.\n"
        "7. الالتزام بتعليمات الإدارة واجب."
    )
    await update.message.reply_text(text)


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("rules", rules))

app.run_polling()
