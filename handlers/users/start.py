from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from loader import dp, user_db
from data.config import ADMINS

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username

    if not user_db.select_user(user_id):
        user_db.add_user(user_id, username)

        user_count = user_db.count_users()
        for admin in ADMINS:
            await dp.bot.send_message(admin, f"Yangi foydalanuvchi: @{username}\nJami: {user_count}")

    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!")
