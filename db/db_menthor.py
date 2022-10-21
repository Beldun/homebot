import sqlite3
import random
from config import bot


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print('База данных подключена')

    db.execute("CREATE TABLE IF NOT EXISTS form "
               "(id INTEGER PRIMARY KEY, namme TEXT,"
               "branch TEXT, age INTEGER, groupp TEXT)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO form VALUES (?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    results = cursor.execute("SELECT * FROM form ").fetchall()
    random_user = random.choice(results)
    await bot.send_message(message.from_user.id,
                           f"\nID - [{random_user[0]}]"
                           f"\nИмя - {random_user[1]}"
                           f"\nНаправление - {random_user[2]}"
                           f"\nВозраст - {random_user[3]}"
                           f"\nГруппа - {random_user[4]}")


async def sql_command_all():
    return cursor.execute("SELECT * FROM form").fetchall()


async def sql_command_del(id):
    cursor.execute("DELETE FROM form WHERE id = ?", (id,))
    db.commit()
