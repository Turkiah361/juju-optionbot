from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7922821938:AAGCQ-wQDaWLNYrvGRlNDuefArqt4DMhGA4"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to Juju's Option Bot! Send me a stock like TSLA or AMD.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.upper()

    if text == "TSLA":
        await update.message.reply_text("📊 TSLA Strategy:\n✅ Put Debit Spread\nConfidence: 75%\nRSI: 43\nIVR: 39")
    elif text == "AMD":
        await update.message.reply_text("📊 AMD Strategy:\n✅ Call Debit Spread\nConfidence: 85%\nRSI: 64\nIVR: 51")
    else:
        await update.message.reply_text(f"⚠️ Sorry, I don't have strategy data for {text} yet.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
