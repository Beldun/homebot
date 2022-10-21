from aiogram.utils import executor
from config import dp
import logging
from handlers import admin, callback, client, extra, fsmAdminMentor
from db.db_menthor import sql_create

callback.register_handlers_callback(dp)
client.register_handlers_client(dp)
fsmAdminMentor.register_handlers_fsm_mentors(dp)
admin.register_handlers_admin(dp)

extra.register_handlers_extra(dp)


async def on_startup(_):
    sql_create()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


#Доделать игру с кубиками