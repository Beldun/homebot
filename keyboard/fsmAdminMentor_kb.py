from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True
)

mem = KeyboardButton('/mem')
quiz = KeyboardButton('/quiz')
watch = KeyboardButton('/watch')
form = KeyboardButton('/form')
delt = KeyboardButton('/del')

start_markup.add(mem, quiz, watch, form, delt)

branch_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

back = KeyboardButton('Backend')
front = KeyboardButton('Frontend')
ui = KeyboardButton('UI/UX')
droid = KeyboardButton('Android')
ios = KeyboardButton('iOS')

branch_markup.add(back, front, ui, droid, ios).add(KeyboardButton('CANCEL'))

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('ДА'), KeyboardButton('НЕТ'))

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('CANCEL'))
