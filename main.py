from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import wikipedia

wikipedia.set_lang('ru')
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


TOKEN = '6206026928:AAHIPz-f-dlRpXPpoRuxSHpCWqnZnNaSyM8'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('❤️', callback_data="like"), InlineKeyboardButton('🙅', callback_data='dislike')],

])
rkb = ReplyKeyboardMarkup(resize_keyboard=True)
rkb.add(KeyboardButton(text='/help'))
rkb.add(KeyboardButton(text='/restart'))



@dp.message_handler(commands=['start'])
async def start_command(massage: types.Message):
    await massage.reply(text='qalaysan')


# @dp.message_handler()
# async def echo_ansewr(massage: types.Message):
#     await massage.answer(text=massage.text.upper())

@dp.message_handler(Text(equals="commands"))
async def start_commond(massage: types.Message):
    await bot.send_photo(chat_id=massage.from_user.id,
                         photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVVvx7DfBXY0oDlvFxQ_2q3u6_-igZggmWOA&usqp=CAU",
                         caption='Bu rasm sizga yoqdimi',
                         reply_markup=rkb)


@dp.callback_query_handler(text='like')
async def callback(callback: types.callback_query):
    await callback.answer('You like it')


@dp.message_handler(Text(equals='Manzil'))
async def location(massage: types.Message):
    await bot.send_location(chat_id=massage.from_user.id,
                            latitude=41.287629, longitude=69.219357,)
    await massage.answer('Bu Soff Study manzili')
@dp.callback_query_handler(text='dislike')
async def callback(callback: types.callback_query):
    await callback.answer('Yuo dislike it')

@dp.message_handler()
async def sendWiki(massage: types.Message):
    try:
        qaytgan = wikipedia.summary(massage.text)
        await massage.answer(qaytgan)
    except:
        await massage.answer("Bu mavzuga oid ma'lumot topilmadi")

# send foto, inline keyboard button , ReplayKeyboardbutton








if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)
