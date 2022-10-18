from aiogram.utils import executor

from config import dp
import logging

from handlers import admin, callback, client, extra, fsmAdminMentor

callback.register_handlers_callback(dp)
client.register_handlers_client(dp)
fsmAdminMentor.register_handlers_fsm_mentors(dp)
extra.register_handlers_extra(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)


#Доделать игру с кубиками