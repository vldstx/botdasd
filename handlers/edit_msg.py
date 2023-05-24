import datetime

from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from other.functions import GetMenuButtons, logger
from create_bot import sql, db, bot
from other.keyboards import AdminPanel, BackMenu, ReplyCancel
from other.states import *

async def edit_msg(message:types.Message,state=Admin.Edit.msg):
    temp = sql.execute("SELECT temp FROM users WHERE id = ?", (message.from_user.id,)).fetchone()
    msg = sql.execute("SELECT msg FROM admin").fetchone()
    msg = eval(msg[0])
    msg[temp[0]] = message.text
    sql.execute("UPDATE admin SET msg = ?", (str(msg),))
    db.commit()
    await message.answer("<b>Успешно!</b>")
    btn_add = []
    msg_edit = InlineKeyboardMarkup(row_width=2)
    for i in msg:
        add = InlineKeyboardButton(str(i), callback_data=f"Edit_Msg_{i}")
        btn_add.append(add)
    for i in range(len(btn_add)):
        if len(btn_add) >= 2:
            msg_edit.add(btn_add[0], btn_add[1])
            btn_add.pop(0)
            btn_add.pop(0)
        elif len(btn_add) == 1:
            msg_edit.add(btn_add[0])
            btn_add.pop(0)
    add = InlineKeyboardButton("↩️ Назад", callback_data="Menu_List")
    msg_edit.add(add)
    await message.answer("<b>💬 Сообщения</b>", reply_markup=msg_edit)
    await state.finish()

async def edit_msg_call(callback:types.CallbackQuery,state=Admin.Edit.msg):
    if callback.data.startswith("Menu"):
        split = callback.data.split("_")
        type = split[1]
        if type == "List":
            msg = sql.execute("SELECT msg FROM admin").fetchone()
            msg = eval(msg[0])
            btn_add = []
            msg_edit = InlineKeyboardMarkup(row_width=2)
            for i in msg:
                add = InlineKeyboardButton(str(i), callback_data=f"Edit_Msg_{i}")
                btn_add.append(add)
            for i in range(len(btn_add)):
                if len(btn_add) >= 2:
                    msg_edit.add(btn_add[0], btn_add[1])
                    btn_add.pop(0)
                    btn_add.pop(0)
                elif len(btn_add) == 1:
                    msg_edit.add(btn_add[0])
                    btn_add.pop(0)
            add = InlineKeyboardButton("↩️ Назад", callback_data="Menu_List")
            msg_edit.add(add)
            await callback.message.edit_text("<b>💬 Сообщения</b>", reply_markup=msg_edit)
            await state.finish()

def register_editmsg(dp:Dispatcher):
    dp.register_message_handler(edit_msg,state=Admin.Edit.msg)
    dp.register_callback_query_handler(edit_msg_call,state=Admin.Edit.msg)