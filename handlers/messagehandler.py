import datetime
from datetime import datetime
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other.functions import GetMenuButtons, logger
from create_bot import sql, db, bot
from other.keyboards import ReplyCancel, AdminPanel
from other.states import *
from datetime import date
import aiocron


async def start_message(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.username



    admin_users = sql.execute("SELECT id FROM users WHERE admin = 1").fetchall()
    for admin_user in admin_users:
        admin_chat_id = admin_user[0]
    user_exists = sql.execute("SELECT id FROM users WHERE id = ?", (user_id,)).fetchone()
    if user_exists is None:
        sql.execute("INSERT INTO users(`id`, `username`, `date`, `subscription_status`, `expiration_date`) VALUES(?, ?, ?, 'inactive', NULL)", (user_id, user_name, date.today()))
        db.commit()

    # Расчет времени до окончания подписки в часах
    query = "SELECT expiration_date FROM users WHERE id = ?"
    sql.execute(query, (user_id,))
    expiration_date = sql.fetchone()[0]
    with open('menu.png', 'rb') as photo:
     if expiration_date:
        expiration_datetime = datetime.strptime(expiration_date, "%Y-%m-%d %H:%M:%S")
     #   if expiration_datetime <= datetime.now():
         #   sql.execute("UPDATE users SET subscription_status = 'inactive' WHERE id = ?", (user_id,))
         #   sql.execute("UPDATE users SET expiration_date = NULL WHERE id = ?", (user_id,))
        #    db.commit()
        remaining_hours = (expiration_datetime - datetime.now()).total_seconds() / 3600
        remaining_hours = int(max(remaining_hours, 0))
        await bot.send_photo(
                chat_id=message.from_user.id,
                photo=photo,
                caption=f'🆔Ваш ID: <code>{user_id}</code>'
                    f'\n♻️ Подписка действует ещё: {remaining_hours} ч.',
                reply_markup=await GetMenuButtons(message.from_user.id)
        )
     else:
        await bot.send_photo(
                chat_id=message.from_user.id,
                photo=photo,
                caption=f'🆔Ваш ID: <code>{user_id}</code>'
                    f'\n♻️ Подписка неактивна.',
                reply_markup=await GetMenuButtons(message.from_user.id)
        )


async def messagehandler(message:types.Message):
    msg = sql.execute("SELECT msg FROM admin").fetchone()
    msg = eval(msg[0])


async def check_subscription_status():
    users = sql.execute("SELECT id, expiration_date FROM users").fetchall()

    for user in users:
        user_id = user[0]
        expiration_date = user[1]

        username = "SELECT username FROM users WHERE id = ?"
        sql.execute(username, (user_id,))
        result = sql.fetchone()
        username = result[0] if result else None

        if expiration_date:
            expiration_datetime = datetime.strptime(expiration_date, "%Y-%m-%d %H:%M:%S")
            if expiration_datetime <= datetime.now():
                await bot.send_message(chat_id=1592632638, text=f'Подписка у @{username} истекла!')
                sql.execute("UPDATE users SET subscription_status = 'inactive', expiration_date = NULL WHERE id = ?", (user_id,))
                db.commit()
            else:
                remaining_hours = (expiration_datetime - datetime.now()).total_seconds() / 3600
                remaining_hours = int(max(remaining_hours, 0))


aiocron.crontab('*/1 * * * *')(check_subscription_status)

def register_message(dp:Dispatcher):
    dp.register_message_handler(start_message, commands=['start'])
    dp.register_message_handler(messagehandler)

