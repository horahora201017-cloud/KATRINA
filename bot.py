
import os
from telegram import Update
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
        "2. يمنع السب والشتم.\n"
        "3. يمنع إرسال الروابط بدون إذن.\n"
        "4. يمنع الإزعاج أو السبام."
    )
    await update.message.reply_text(text)


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("rules", rules))

app.run_polling()
