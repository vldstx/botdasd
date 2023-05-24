from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from other.functions import GetMenuButtons, logger
from create_bot import sql, db, bot
from other.keyboards import ReplyCancel, AdminPanel
from other.states import *

async def msg(message:types.Message,state=Tickets.Ask.msg):
    users = sql.execute("SELECT id FROM users").fetchall()

    photo_path = "рассылка.png"
    if not os.path.isfile(photo_path):
            await message.answer('<b>Нет фотографии для отправки</b>')
    else:
        await message.answer("<b>Рассылка успешно запущена!</b>", reply_markup=await GetMenuButtons(message.from_user.id))
        await state.finish()
    with open(photo_path, 'rb') as photo: 
        for i in users:
            try:
                await bot.send_photo(chat_id=i[0], caption=message.text, photo=photo, parse_mode='None')
            except:
                pass
    await message.answer("<b>Рассылка закончена!</b>")
async def cancel(callback:types.CallbackQuery,state=Tickets.Ask.msg):
    await state.finish()
    await callback.message.delete()
    await callback.message.answer("<b>Главное меню</b>",reply_markup=await GetMenuButtons(callback.from_user.id))

def register_adminrass(dp:Dispatcher):
    dp.register_message_handler(msg,state=Admin.Rass.msg)
    dp.register_callback_query_handler(cancel,state=Admin.Rass.msg)