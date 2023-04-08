from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
TOKEN = '6206026928:AAHIPz-f-dlRpXPpoRuxSHpCWqnZnNaSyM8'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)


@dp.message_handler(commands=['start'])
async def start_command(massage: types.Message):
    await massage.reply(text='qalaysan')


# @dp.message_handler()
# async def echo_ansewr(massage: types.Message):
#     await massage.answer(text=massage.text.upper())

@dp.message_handler(Text(equals="commands"))
async def get_commands(massage: types.Message):
    text = """
/start - yordam berish
/keyingi - o'tgazib yuborish
    """
    await massage.answer(text=text)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)









