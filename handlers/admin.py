from aiogram import types, Dispatcher
from config import bot, dp, ADMIN
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from db.db_menthor import sql_command_all


async def delete_data(message: types.Message):
    if not message.from_user.id in ADMIN:
        await message.answer("Доступ имеет только АДМИНИСТРАТОР!!!")
    else:
        users = await sql_command_all()
        for user in users:
            await bot.send_message(message.from_user.id,
                                   f"\nID - [{user[0]}]"
                                   f"\nИмя - {user[1]}"
                                   f"\nНаправление - {user[2]}"
                                   f"\nВозраст - {user[3]}"
                                   f"\nГруппа - {user[4]}",
                                   reply_markup=InlineKeyboardMarkup().add(
                                        InlineKeyboardButton(f"Delete {user[1]}",
                                                             callback_data=f"delete {user[0]}")
                                     ))


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(delete_data, commands=['del'])
