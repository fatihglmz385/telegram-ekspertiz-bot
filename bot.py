import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = 8672167333:AAH15H41q0dqvsun5Tbco-JH39qg-XRUBmU

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ekspertiz botuna hoş geldiniz 🚗")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot çalışıyor...")
app.run_polling()
