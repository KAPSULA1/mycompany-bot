from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
import logging, random, os

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# --- STEP 1: Load token safely from environment ---
TOKEN = os.environ.get("BOT_TOKEN")  # <-- Add your token as GitHub secret or local environment variable

if not TOKEN:
    print("ERROR: BOT_TOKEN environment variable not found!")
    exit()

# --- STEP 2: Random quotes/fun messages ---
QUOTES = [
    "Success is not final; failure is not fatal. Keep going! 💪",
    "Innovation distinguishes a leader from a follower. 🚀",
    "Small steps every day lead to big results. 🐾",
    "Hustle in silence, let success make the noise. 🔥"
]

# --- STEP 3: /start command with main menu ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["About Us", "Contact"], ["Services", "Help"], ["Pricing", "Quote"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Welcome! 👋 Choose an option below to explore:", reply_markup=reply_markup)

# --- STEP 4: Handle text messages ---
async def button_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    
    if text == "about us":
        await update.message.reply_text("We are MyCompany, helping you achieve success! 🌟")
    elif text == "contact":
        await update.message.reply_text("📧 Email: email@example.com\n📞 Phone: +123456789")
    elif text == "services":
        # Inline buttons example
        keyboard = [
            [InlineKeyboardButton("Consulting", callback_data="service_consulting")],
            [InlineKeyboardButton("Support", callback_data="service_support")],
            [InlineKeyboardButton("Back to menu", callback_data="back_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Choose a service:", reply_markup=reply_markup)
    elif text == "help":
        await update.message.reply_text("Type any menu button or command to explore. Try /quote for inspiration!")
    elif text == "pricing":
        price = random.choice([99, 199, 222, 299])
        await update.message.reply_text(f"Our pricing starts at ${price}/month 💰. Contact us for details!")
    elif text == "quote":
        await update.message.reply_text(random.choice(QUOTES))
    else:
        await update.message.reply_text(f"🤔 Sorry, I don't understand: {update.message.text}")

# --- STEP 5: Handle inline button clicks ---
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # acknowledge button press
    
    if query.data == "service_consulting":
        await query.edit_message_text("💼 Consulting: We provide business & tech consulting.")
    elif query.data == "service_support":
        await query.edit_message_text("🛠 Support: 24/7 assistance for your business.")
    elif query.data == "back_menu":
        await start(update, context)

# --- STEP 6: Run the bot ---
def main():
    app = Application.builder().token(TOKEN).build()
    
    # Commands
    app.add_handler(CommandHandler("start", start))
    
    # Catch all text messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, button_response))
    
    # Inline button clicks
    app.add_handler(CallbackQueryHandler(button_callback))
    
    print("Mindblow bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
