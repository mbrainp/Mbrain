import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات با موفقیت اجرا شد.")

def main():
    token = os.environ.get("TELEGRAM_TOKEN")
    if not token:
        print("ERROR: TELEGRAM_TOKEN environment variable not set")
        return

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot starting... (now run_polling)")
    app.run_polling()

if __name__ == "__main__":
    main()
