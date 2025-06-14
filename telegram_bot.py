<<<<<<< HEAD
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os

TOKEN = os.getenv("BOT_TOKEN", "your-real-token-here")  # Replace this if needed

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Juju'sOptionbot! 🚀\nSend /help to see what I can do.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Use /start to begin.\nSoon, I’ll fetch stock trades, insights, and more!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
=======
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os

TOKEN = os.getenv("BOT_TOKEN", "7922821938:AAGCQ-wQDaWLNYrvGRlNDuefArqt4DMhGA4")

app = Flask(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to Juju's Option Bot!\nType a stock like TSLA or AMD.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip().upper()

    if user_text == "TSLA":
        await update.message.reply_text("📊 TSLA Strategy:\n✅ Put Debit Spread\nConfidence: 75%\nRSI: 43\nIVR: 39")
    elif user_text == "AMD":
        await update.message.reply_text("📊 AMD Strategy:\n✅ Call Debit Spread\nConfidence: 85%\nRSI: 64\nIVR: 51")
    else:
        await update.message.reply_text(f"⚠️ Sorry, I don’t have data for {user_text} yet.")

def run_bot():
    telegram_app = ApplicationBuilder().token(TOKEN).build()
    telegram_app.add_handler(CommandHandler("start", start))
    telegram_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    telegram_app.run_polling()

if __name__ == "__main__":
    run_bot()
>>>>>>> 815e9dbbc85bc69a36d630564a8b08eeec1ae62e
