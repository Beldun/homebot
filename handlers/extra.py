from aiogram import types, Dispatcher
from config import bot, dp, ADMIN
import random


async def echo(message: types.Message):
    emoji = ['🎲', '🏀', '⚽️', '🎯', '🎳', '🎰']
    if message.text.isdigit():
        await bot.send_message(message.from_user.id, int(message.text) * int(message.text))
    elif message.text == "Привет":
        await bot.send_message(message.from_user.id, "Привет 👋 Как дела?🙃")
    elif message.text == "Хорошо" or message.text == 'Отлично':
        await bot.send_message(message.from_user.id,
                               "Рад это слышать 😄, надеюсь ничто не сможет испортить вам "
                               "ваше чудесное настроение 🫢."
                               "\nК сожалению это все что я могу 😔, но я надеюсь мой "
                               "программист дополнит меня и мы с вами еще пообщаемся ☺️."
                               "\nНажмите /help чтобы увидеть все мои функции 😉")
    elif message.text == "Нормально":
        await bot.send_message(message.from_user.id, "Хм 🤔, тогда советую нажать эту кнопочку /mem, "
                                                     "чтобы поднять себе настроение 😉"
                                                     "\nИли может викторина /quiz вам поможет? 🤔")
    elif message.text == "Плохо":
        await bot.send_message(message.from_user.id, "Ох 😱, печально слышать это 🥺. "
                                                     "К сожалению все что я могу - это предложить вам сыграть "
                                                     "в викторину /quiz или увидеть мем /mem 😔. "
                                                     "Надеюсь это поможет вам поднять настроение 😊")
    elif message.text.startswith('!pin') and message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    elif message.text.startswith('game'):
        if message.from_user.id not in ADMIN:
            await message.answer("Доступно только для админа!")
        else:
            await bot.send_dice(message.chat.id, emoji=random.choice(emoji))
    else:
        await bot.send_message(message.from_user.id, message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
