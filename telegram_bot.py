import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# === Define your bot token (use env var from Render) ===
TOKEN = os.getenv("TELEGRAM_TOKEN")

# === /start command ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hi! I'm Juju'sOptionbot. Send me a stock ticker to analyze.")

# === message handler ===
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.strip().upper()
    
    if user_message.isalpha():
        await update.message.reply_text(f"📊 Generating strategy for {user_message}... (dummy response)")
        # Here you'd call your actual strategy bot logic
        await update.message.reply_text(f"✅ Strategy: Call Debit Spread\nConfidence: 85%\nIV Rank: 42\nRSI: 67")
    else:
        await update.message.reply_text("⚠️ Please send a valid stock symbol (e.g., AAPL, TSLA, etc.)")

# === Main app entry ===
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
