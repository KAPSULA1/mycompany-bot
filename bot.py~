from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["About Us", "Contact"], ["Services", "Help"], ["Pricing"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Welcome! 👋 Choose an option:", reply_markup=reply_markup)

async def button_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    
    if text == "about us":
        await update.message.reply_text("We are MyCompany, helping you achieve success!")
    elif text == "contact":
        await update.message.reply_text("Contact us at: email@example.com or +123456789")
    elif text == "services":
        await update.message.reply_text("We offer consulting, support, and more!")
    elif text == "help":
        await update.message.reply_text("Ask anything or type /start to see the menu again.")
    elif text == "pricing":
        await update.message.reply_text("Our pricing starts at 99$/month. Contact us!")
    else:
        await update.message.reply_text(f"Sorry, I don't understand: {update.message.text}")

def main():
    if not TOKEN:
        print("ERROR: BOT_TOKEN environment variable not found!")
        return
        
    print(f"Starting bot with token: {TOKEN[:10]}...")
    
    # Create the Application
    application = Application.builder().token(TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, button_response))
    
    # Run the bot
    print("Bot is starting...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
