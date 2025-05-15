
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# 🔐 ВСТАВ СЮДИ ТОКЕН ТВОГО БОТА
BOT_TOKEN = "8173205057:AAEwUMkQB7djHVw-ysntIkD8yQZE09liHTc"

# 🆔 ВСТАВ СЮДИ CHAT_ID твоєї групи або каналу
MODERATION_CHAT_ID = -1002355606956  # приклад ID каналу

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Ігноруємо команду /start або інші команди
    if update.message.text and update.message.text.startswith("/"):
        return

    try:
        # Переслати повідомлення в канал/групу
        await update.message.forward(chat_id=MODERATION_CHAT_ID)

        # Надіслати відповідь, тільки якщо це не команда
        await update.message.reply_text(
            "📩 Дякуємо! Якщо новина буде цікавою — ми обов'язково її опублікуємо у каналі."
        )
    except Exception as e:
        logging.error(f"Error forwarding message: {e}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward_message))

print("✅ Бот запущено. Очікує повідомлення...")
app.run_polling()
