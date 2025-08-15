from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, CallbackContext
import os

# Load token
TOKEN = os.environ.get("BOT_TOKEN")

# 1️⃣ Define all commands and responses in a dictionary
COMMANDS = {
    "about_us": "We are MyCompany, helping you achieve success!",
    "contact": "Contact us at: email@example.com or +123456789",
    "services": "We offer consulting, support, and more!",
    "help": "Ask anything or type /start to see the menu again.",
    "pricing": "Our pricing starts at 99$/month. Contact us for custom plans!"
}

# 2️⃣ /start command with inline buttons
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("About Us", callback_data="about_us"),
         InlineKeyboardButton("Contact", callback_data="contact")],
        [InlineKeyboardButton("Services", callback_data="services"),
         InlineKeyboardButton("Help", callback_data="help")],
        [InlineKeyboardButton("Pricing", callback_data="pricing")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Welcome! 👋 Choose an option:", reply_markup=reply_markup)

# 3️⃣ Handle button clicks
def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()  # acknowledge the button click

    # Get response from COMMANDS dictionary
    response = COMMANDS.get(query.data, "Sorry, I don't understand this command.")
    query.edit_message_text(text=response)

# 4️⃣ Handle free text messages
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text.lower()

    # Simple "smart" responses
    if "hello" in text or "hi" in text:
        update.message.reply_text("Hello! 👋 How can I help you today?")
    elif "price" in text or "cost" in text:
        update.message.reply_text(COMMANDS["pricing"])
    else:
        update.message.reply_text("I’m not sure about that 🤔. Please use the menu or type /start.")

# 5️⃣ Main function
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button_handler))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))

    updater.start_polling()
    print("Bot is running...")
    updater.idle()

if __name__ == "__main__":
    main()
