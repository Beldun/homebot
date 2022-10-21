from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
from db.db_menthor import sql_command_del
import random


async def cat_meme(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_cats = InlineKeyboardButton("Cats", callback_data="button_call_cats")
    button_call_school = InlineKeyboardButton("School", callback_data="button_call_school")
    button_call_messanger = InlineKeyboardButton("Messanger", callback_data="button_call_messanger")
    button_call_programming = InlineKeyboardButton("Programming", callback_data="button_call_programming")
    markup.add(button_call_cats)
    markup.add(button_call_school)
    markup.add(button_call_messanger)
    markup.add(button_call_programming)
    ph_1 = open("memes/Catmeme1.png", "rb")
    ph_2 = open("memes/Catmeme2.jpg", "rb")
    ph_3 = open("memes/Catmeme3.jpeg", "rb")
    ph_4 = open("memes/Catmeme4.jpg", "rb")
    ph_5 = open("memes/Catmeme5.jpg", "rb")
    ph_6 = open("memes/Catmeme6.jpg", "rb")
    ph_7 = open("memes/Catmeme7.jpg", "rb")
    ph_8 = open("memes/Catmeme8.jpg", "rb")
    ph_9 = open("memes/Catmeme9.jpeg", "rb")
    ph_10 = open("memes/Catmeme10.jpg", "rb")
    ph_11 = open("memes/Catmeme11.jpg", "rb")
    ph_random = [ph_1, ph_2, ph_3, ph_4, ph_5, ph_6, ph_7, ph_8, ph_9, ph_10, ph_11]
    await bot.send_photo(call.from_user.id, random.choice(ph_random), reply_markup=markup)


async def school_meme(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_cats = InlineKeyboardButton("Cats", callback_data="button_call_cats")
    button_call_school = InlineKeyboardButton("School", callback_data="button_call_school")
    button_call_messanger = InlineKeyboardButton("Messanger", callback_data="button_call_messanger")
    button_call_programming = InlineKeyboardButton("Programming", callback_data="button_call_programming")
    markup.add(button_call_cats)
    markup.add(button_call_school)
    markup.add(button_call_messanger)
    markup.add(button_call_programming)
    ph_1 = open("memes/schoolmeme1.jpg", "rb")
    ph_2 = open("memes/schoolmeme2.jpg", "rb")
    ph_3 = open("memes/schoolmeme3.jpg", "rb")
    ph_4 = open("memes/schoolmeme4.jpg", "rb")
    ph_5 = open("memes/schoolmeme5.jpg", "rb")
    ph_6 = open("memes/schoolmeme6.jpg", "rb")
    ph_random = [ph_1, ph_2, ph_3, ph_4, ph_5, ph_6]
    await bot.send_photo(call.from_user.id, random.choice(ph_random), reply_markup=markup)


async def messanger_meme(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_cats = InlineKeyboardButton("Cats", callback_data="button_call_cats")
    button_call_school = InlineKeyboardButton("School", callback_data="button_call_school")
    button_call_messanger = InlineKeyboardButton("Messanger", callback_data="button_call_messanger")
    button_call_programming = InlineKeyboardButton("Programming", callback_data="button_call_programming")
    markup.add(button_call_cats)
    markup.add(button_call_school)
    markup.add(button_call_messanger)
    markup.add(button_call_programming)
    ph_1 = open("memes/msmeme1.jpg", "rb")
    ph_2 = open("memes/msmeme2.jpg", "rb")
    ph_3 = open("memes/msmeme3.jpg", "rb")
    ph_4 = open("memes/msmeme4.jpg", "rb")
    ph_5 = open("memes/msmeme5.jpg", "rb")
    ph_6 = open("memes/msmeme6.jpg", "rb")
    ph_7 = open("memes/msmeme7.jpg", "rb")
    ph_random = [ph_1, ph_2, ph_3, ph_4, ph_5, ph_6, ph_7]
    await bot.send_photo(call.from_user.id, random.choice(ph_random), reply_markup=markup)


async def programming_meme(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_cats = InlineKeyboardButton("Cats", callback_data="button_call_cats")
    button_call_school = InlineKeyboardButton("School", callback_data="button_call_school")
    button_call_messanger = InlineKeyboardButton("Messanger", callback_data="button_call_messanger")
    button_call_programming = InlineKeyboardButton("Programming", callback_data="button_call_programming")
    markup.add(button_call_cats)
    markup.add(button_call_school)
    markup.add(button_call_messanger)
    markup.add(button_call_programming)
    ph_1 = open("memes/prmeme1.jpg", "rb")
    ph_2 = open("memes/prmeme2.jpg", "rb")
    ph_3 = open("memes/prmeme3.jpg", "rb")
    ph_4 = open("memes/prmeme4.jpg", "rb")
    ph_5 = open("memes/prmeme5.jpg", "rb")
    ph_6 = open("memes/prmeme6.jpg", "rb")
    ph_7 = open("memes/prmeme7.jpg", "rb")
    ph_random = [ph_1, ph_2, ph_3, ph_4, ph_5, ph_6, ph_7]
    await bot.send_photo(call.from_user.id, random.choice(ph_random), reply_markup=markup)


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_urb = InlineKeyboardButton("Следующий вопрос", callback_data='button_call_urb')
    markup.add(button_call_urb)
    question = "Урбанизация - это..."
    answers = [
        "Быстрый рост и развитие городов",
        "Уборка городов",
        "Густая жидкая масса коричневого цвета",
        "Персонаж из игры"
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        open_period=30,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_mc = InlineKeyboardButton("Следующий вопрос", callback_data='button_call_mc')
    markup.add(button_call_mc)
    question = "Чему равна сила притяжения Земли?"
    answers = [
        "44м/с2",
        "15м/с2",
        "11м/с2",
        "10м/с2"
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        open_period=30,
        reply_markup=markup
    )


async def quiz_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_pic = InlineKeyboardButton("Следующий вопрос", callback_data='button_call_pic')
    markup.add(button_call_pic)
    question = "Кто написал картину 'Крик'?"
    answers = [
        "Винсент ван Гог",
        "Леонардо да Винчи",
        "Эдвард Мунк",
        "Ян Верне"
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        open_period=30,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == "button_call_pic")
async def quiz_f(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_points_1 = InlineKeyboardButton("1", callback_data="button_score")
    button_points_2 = InlineKeyboardButton("2", callback_data="button_score")
    button_points_3 = InlineKeyboardButton("3", callback_data="button_score")
    button_points_4 = InlineKeyboardButton("4", callback_data="button_score")
    button_points_5 = InlineKeyboardButton("5", callback_data="button_score")
    button_points_6 = InlineKeyboardButton("6", callback_data="button_score")
    button_points_7 = InlineKeyboardButton("7", callback_data="button_score")
    button_points_8 = InlineKeyboardButton("8", callback_data="button_score")
    button_points_9 = InlineKeyboardButton("9", callback_data="button_score")
    button_points_10 = InlineKeyboardButton("10", callback_data="button_score")
    markup.add(button_points_1)
    markup.add(button_points_2)
    markup.add(button_points_3)
    markup.add(button_points_4)
    markup.add(button_points_5)
    markup.add(button_points_6)
    markup.add(button_points_7)
    markup.add(button_points_8)
    markup.add(button_points_9)
    markup.add(button_points_10)
    await bot.send_message(call.from_user.id, "Как вам наша викторина? 🤓", reply_markup=markup)


async def ok(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, "Спасибо за ваш отзыв! ☺️")


async def complete_delete(call: types.CallbackQuery):
    await sql_command_del(call.data.replace('delete ', ''))
    await call.answer(text="Удалено из БД", show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


def register_handlers_callback(dp: Dispatcher):
    dp.callback_query_handler(cat_meme, lambda call: call.data == "button_call_cats")
    dp.callback_query_handler(school_meme, lambda call: call.data == "button_call_school")
    dp.callback_query_handler(messanger_meme, lambda call: call.data == "button_call_messanger")
    dp.callback_query_handler(programming_meme, lambda call: call.data == "button_call_programming")
    dp.callback_query_handler(quiz_2, lambda call: call.data == "button_call_ser")
    dp.callback_query_handler(quiz_3, lambda call: call.data == "button_call_urb")
    dp.callback_query_handler(quiz_4, lambda call: call.data == "button_call_mc")
    dp.callback_query_handler(quiz_f, lambda call: call.data == "button_call_pic")
    dp.callback_query_handler(ok, lambda call: call.data == "button_score")
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith('delete '))