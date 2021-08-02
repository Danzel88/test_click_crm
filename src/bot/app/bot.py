from aiogram import Bot, Dispatcher, types

from bot.config import API_TOKEN
from .answers import Answers
from .services import check_request_id

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(Answers.REQUEST_ID.value)







