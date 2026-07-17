KATRINA v1.4

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

reply_markup = InlineKeyboardMarkup(keyboard)  

await update.message.reply_text(  
    text,  
    reply_markup=reply_markup  
)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
query = update.callback_query
await query.answer()

if query.data == "lang_ar":  
    await query.edit_message_text(  
        "✅ تم اختيار اللغة العربية 🇮🇶"  
    )  

elif query.data == "lang_en":  
    await query.edit_message_text(  
        "✅ English language selected 🇺🇸"  

    )

async def user_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
f"🆔 آيديك هو: {update.effective_user.id}",
parse_mode="Markdown"
)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
text = (
"📖 قائمة الأوامر:\n\n"
"/start - بدء استخدام البوت\n"
"/help - عرض قائمة الأوامر\n"
"/rules - عرض قوانين المجموعة"
)
await update.message.reply_text(text)
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
for member in update.message.new_chat_members:
await update.message.reply_text(
f"""🌸 أهلاً وسهلاً {member.mention_html()}

💜 نورت كروب KATRINA.

📜 يرجى قراءة القوانين باستخدام /rules

✨ نتمنى لك وقتاً ممتعاً بيننا.""",
parse_mode="HTML"
)

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
app.add_handler(CommandHandler("id", user_id))
app.add_handler(CommandHandler("rules", rules))
app.add_handler(CallbackQueryHandler(button))
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
app.run_polling()
