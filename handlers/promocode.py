from datetime import datetime, timedelta

from aiogram.types import CallbackQuery

from other.states import *
from aiogram import types, Dispatcher
from handlers.callbackhandler import *
from other.keyboards import *

async def test_subscription_handler(callback: CallbackQuery):

    user_id = callback.from_user.id

    # Проверяем, активировал ли пользователь уже тестовую подписку
    user_info = sql.execute("SELECT `test_subscription_activated` FROM `users` WHERE `id` = ?", (user_id,)).fetchone()
    if user_info and user_info[0] == 1:
        # Если тестовая подписка уже активирована, отправляем сообщение об этом
        await bot.send_message(chat_id=user_id, text="Вы уже активировали тестовую подписку ранее.", reply_markup=DeleteButton)
        return

    # Активируем тестовую подписку для пользователя
    current_datetime = datetime.now()
    expiration_datetime = current_datetime + timedelta(hours=2)
    expiration_date = expiration_datetime.strftime("%Y-%m-%d %H:%M:%S")
    sql.execute("UPDATE users SET subscription_status = 'active', expiration_date = ?, test_subscription_activated = 1 WHERE id = ?", (expiration_date, user_id))
    db.commit()

    # Отправляем сообщение об успешной активации тестовой подписки
    await bot.send_message(chat_id=user_id, text="Тестовая подписка успешно активирована на 2 часа.", reply_markup=DeleteButton)



def register_addpromo(dp: Dispatcher):
    dp.register_message_handler(test_subscription_handler, state=Promo.Ask.msg)
