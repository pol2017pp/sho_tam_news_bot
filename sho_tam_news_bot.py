
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

# 🔐 ВСТАВ СЮДИ ТОКЕН ТВОГО БОТА
BOT_TOKEN = "8173205057:AAEwUMkQB7djHVw-ysntIkD8yQZE09liHTc"

# 🆔 ВСТАВ СЮДИ CHAT_ID твоєї групи або каналу
MODERATION_CHAT_ID = -1002355606956  # приклад ID каналу

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# 🔹 Обробка команди /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привіт! Надішліть нам новину, фото або відео — ми переглянемо, і якщо буде цікаво — опублікуємо у каналі.

"
        "📎 Можна прикріплювати медіа, писати текст або надсилати все разом.

"
        "📩 Чекаємо на твоє повідомлення!"
    )

# 🔹 Обробка всіх інших повідомлень
async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Ігноруємо команди
    if update.message.text and update.message.text.startswith("/"):
        return

    try:
        # Переслати повідомлення в канал/групу
        await update.message.forward(chat_id=MODERATION_CHAT_ID)

        # Надіслати відповідь
        await update.message.reply_text(
            "📩 Дякуємо! Якщо новина буде цікавою — ми обов'язково її опублікуємо у каналі."
        )
    except Exception as e:
        logging.error(f"Error forwarding message: {e}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, forward_message))

print("✅ Бот запущено. Очікує повідомлення...")
app.run_polling()
