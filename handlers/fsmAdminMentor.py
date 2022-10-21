import random

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMIN
from keyboard.fsmAdminMentor_kb import branch_markup, submit_markup, cancel_markup, start_markup
from db.db_menthor import sql_command_insert


class FSMAdmin(StatesGroup):
    name = State()
    branch = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if not message.chat.type == "private":
        await message.answer("Данная функция доступна только в л/с бота")
    elif not message.from_user.id in ADMIN:
        await message.answer("Ты не похож на администратора, извини друг )")
    else:
        await FSMAdmin.name.set()
        await message.answer(
            f"Здравствуй, {message.from_user.full_name}! "
            "\nВведи пожалуйста имя ментора:"
        )


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        lst = []
        k = random.randint(100000, 999999)
        while k in lst:
            k = random.randint(100000, 999999)
        lst.append(k)
        data['id'] = k
        if message.text.isalpha():
            data['name'] = message.text
            await FSMAdmin.next()
            await message.answer(f"Какое направление у ментора??", reply_markup=branch_markup)
        else:
            await message.answer("Имя с цифрами? Мне кажется, что ментор не сын Илона")


async def load_branch(message: types.Message, state: FSMContext):
    branch = ["backend", "frontend", "ui/ux", "android", "ios"]
    if message.text.lower() in branch:
        async with state.proxy() as data:
            data['branch'] = message.text
        await FSMAdmin.next()
        await message.answer(f"Сколько лет?", reply_markup=cancel_markup)
    else:
        await message.answer("Такого направления нет")


async def load_age(message: types.Message, state: FSMContext):
    try:
        if int(message.text) < 11:
            await message.answer('Ого, тебе не кажется, что он еще слишком мал? Попробуй заново )')
        elif int(message.text) > 60:
            await message.answer("СТОП, я не думаю, что настолько старый человек, может быть ментором. "
                                "Попробуй еще раз ;)")
        else:
            async with state.proxy() as data:
                data['age'] = int(message.text)
            await FSMAdmin.next()
            await message.answer(f"К какой группе принадлежит?", reply_markup=cancel_markup)
    except:
        await message.answer("По моим данным, как минимум на сегодняшний день, "
                             "чтобы вычеслить возраст, люди еще пользуются цифрами, "
                             "но откуда мне знать, да? Ведь я всего-лишь машина")


async def load_group(message: types.Message, state: FSMContext):
    flag = 0
    for i in message.text:
        if i.isalpha():
            await message.answer("В названиях групп буквы не используются")
            flag = 1
            break
    if not flag:
        async with state.proxy() as data:
            data['groupe'] = message.text
            await message.answer("Для завершения давайте проверим правильность введенных данных:"
                                 f"\nID - [{data['id']}]"
                                 f"\nИмя - {data['name']}"
                                 f"\nНаправление - {data['branch']}"
                                 f"\nВозраст - {data['age']}"
                                 f"\nГруппа - {data['groupe']}")
            await FSMAdmin.next()
            await message.answer(f"Вы подтверждаете записанные данные ментора {data['name']}? "
                                 f"\n<<<да/нет>>>", reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        async with state.proxy() as data:
            await sql_command_insert(state)
            await state.finish()
            await message.answer(f"Поздравляем нового ментора по имени {data['name']}!!!", reply_markup=start_markup)
    elif message.text.lower() == 'нет':
        await state.finish()
        await message.answer('Очень жаль, давай по новой', reply_markup=start_markup)
    else:
        await message.answer("Понятно же написано <<<ДА>>> или <<<НЕТ>>>")


async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Принято! ОТМЕНЯЮ!")


def register_handlers_fsm_mentors(dp: Dispatcher):
    dp.register_message_handler(cancel, Text(equals='cancel', ignore_case=True),
                                state='*')
    dp.register_message_handler(fsm_start, commands=["form"])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_branch, state=FSMAdmin.branch)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)

