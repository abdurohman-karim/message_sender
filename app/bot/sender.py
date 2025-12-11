from aiogram import Bot
from app.core.config import settings

bot = Bot(settings.BOT_TOKEN)


async def send_message_to_user(chat_id: int, text: str):
    await bot.send_message(chat_id, text)
