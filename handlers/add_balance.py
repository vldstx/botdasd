from datetime import datetime, timedelta
from aiogram import types, Dispatcher
from other.states import *
from handlers.callbackhandler import *
from other.keyboards import *

async def msg(message: types.Message, state):
    admin_user_id = message.from_user.id
    user_id = message.text

    # Проверка, является ли отправитель сообщения администратором
    admin_users = sql.execute("SELECT id FROM users WHERE admin = 1").fetchall()
    admin_chat_ids = [admin_user[0] for admin_user in admin_users]
    if admin_user_id not in admin_chat_ids:
        await message.answer("У вас нет прав на начисление подписки.")

    # Проверка, существует ли указанный user_id в базе данных
    user_exists = sql.execute("SELECT id FROM users WHERE id = ?", (user_id,)).fetchone()
    if user_exists is None:
        await message.answer("Пользователь с указанным user_id не найден.", reply_markup=BackMenu)

    else:
        await message.answer("Введите количество часов подписки:", reply_markup=BackMenu)
        await Balance.Duration.msg.set()
        await state.update_data(user_id=user_id)

async def duration(message: types.Message, state):
        # Получение данных из предыдущего состояния
        data = await state.get_data()
        user_id = data.get('user_id')

        # Получение количества часов
        duration_hours = int(message.text)

        # Вычисление даты и времени окончания подписки
        current_datetime = datetime.now()
        expiration_datetime = current_datetime + timedelta(hours=duration_hours)
        expiration_date = expiration_datetime.strftime("%Y-%m-%d %H:%M:%S")
        new_expiration_datetime = expiration_datetime + timedelta(hours=duration_hours)
        new_expiration_date = new_expiration_datetime.strftime("%Y-%m-%d %H:%M:%S")

        # Обновление данных пользователя в базе данных
        sql.execute("UPDATE users SET subscription_status = 'active', expiration_date = ? WHERE id = ?", (new_expiration_date, user_id))
        db.commit()


        await message.reply(f"Подписка пользователя {user_id} активирована и будет действовать в течение {duration_hours} часов.", reply_markup=BackMenu)
        await bot.send_message(chat_id=user_id, text=f'На Ваш аккаунт добавлена подписка на {duration_hours} часов.', reply_markup=DeleteButton)


        await state.finish()


async def cancel(callback: types.CallbackQuery, state=Balance.Ask.msg):
    await state.finish()
    await callback.message.delete()
    with open('menu.png', 'rb') as photo:
        await bot.send_photo(chat_id=callback.from_user.id, photo=photo,
                             reply_markup=await GetMenuButtons(callback.from_user.id))


def register_addbalance(dp: Dispatcher):
    dp.register_message_handler(msg, state=Balance.Ask.msg)
    dp.register_message_handler(duration, state=Balance.Duration.msg)
    dp.register_callback_query_handler(cancel, state=[Balance.Ask.msg, Balance.Duration.msg])