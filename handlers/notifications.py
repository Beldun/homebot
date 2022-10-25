import asyncio
import aioschedule
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from config import bot


async def get_id(message: types.Message):
    global id_n
    id_n = message.from_user.id
    await message.answer('Я уведомлю вас за 24ч. до дедлайна')


async def hw():
    await bot.send_message('До дедлайна осталось 24ч., вы сделали домашку и написали StandUp? '
                           'Если нет, то советую поскорее сделать выше перечисленное')


async def notif_schedule():
    aioschedule.every().friday.at('20:00').do(hw)
    aioschedule.every().wednesday.at('20:00').do(hw)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notifications(dp: Dispatcher):
    dp.register_message_handler(get_id,
                                Text(equals='домашка', ignore_case=True))

