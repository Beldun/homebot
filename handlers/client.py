from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp


async def start(message: types.Message):
    await bot.send_message(message.chat.id, f"Приветствую {message.from_user.first_name}. 😁"
                                                 f"\nИспользуйте команду /help для большей информации")


async def help_1(message: types.Message):
    await bot.send_message(message.chat.id, "Используйте команду /quiz чтобы начать викторину."
                                                 "\nИспользуйте команду /mem чтобы выбрать мемы."
                                                 "\nВы можете написать любое сообщение и бот повторит за вами."
                                                 "\nИли любое число и тогда бот возведет его в квадрат."
                                                 "\nА еще вы можете написать мне 'Привет'))")


async def kpop(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_cats = InlineKeyboardButton("Cats", callback_data="button_call_cats")
    button_call_school = InlineKeyboardButton("School", callback_data="button_call_school")
    button_call_messanger = InlineKeyboardButton("Messanger", callback_data="button_call_messanger")
    button_call_programming = InlineKeyboardButton("Programming", callback_data="button_call_programming")
    markup.add(button_call_cats)
    markup.add(button_call_school)
    markup.add(button_call_messanger)
    markup.add(button_call_programming)
    await bot.send_message(message.from_user.id, f"Выберите мем", reply_markup=markup)


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_ser = InlineKeyboardButton("Следующий вопрос", callback_data='button_call_ser')
    markup.add(button_call_ser)

    question = "Гормон радости - это..."
    answers = [
        "Эндорфин",
        "Дофамин",
        "Серотонин",
        "Окситоцин"
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=2,
        open_period=30,
        reply_markup=markup
    )


async def fall(message: types.Message):
    await bot.send_dice(message.chat.id, emoji="")
    await bot.send_dice(message.chat.id, emoji="")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(help_1, commands=["help"])
    dp.register_message_handler(kpop, commands=["mem"])
    dp.register_message_handler(quiz_1, commands=["quiz"])

