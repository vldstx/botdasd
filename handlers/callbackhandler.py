

from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other.functions import GetMenuButtons, logger
from create_bot import sql, db, bot
from other.keyboards import AdminPanel, BackMenu, ReplyCancel, AdminManuals, BackAdmin, SubBuy, SubChange1,SubChange3, SubChange7, SubChange30, CryptaChoise1, CryptaChoise3, CryptaChoise7, CryptaChoise30
from handlers.promocode import *
from other.states import *
from handlers.messagehandler import *
from handlers.add_balance import duration
from aiogram.dispatcher import FSMContext
from datetime import date
import asyncio
from handlers.cryptopay import *
from parser.olxuz import *

async def callbackhandler(callback:types.CallbackQuery, state: FSMContext):
    #print (callback.data)
    datalang = callback.data
    print(datetime.now().strftime("%H:%M"), datalang)
    lang = callback.data.split('_')[1].lower()
    await state.update_data(target=lang)
    message_id = callback.message.message_id
    msg = sql.execute("SELECT msg FROM admin").fetchone()
    # msg = eval(msg[0])
    if callback.data.startswith("Menu"):
        split = callback.data.split("_")
        type = split[1]
        if type == "Admin":
            if callback.message:
                await callback.message.delete()
            await bot.send_message(chat_id=callback.from_user.id, text="Adminka", reply_markup=AdminPanel)
        elif type == 'Sub':
            if callback.message:
               await callback.message.delete()
            await bot.send_message(chat_id=callback.from_user.id, text='Выберите подписку: \n <b>Подписка распространяется на все площадки.</b>', reply_markup=SubBuy)




        elif type == 'Parser':
            user_id = callback.from_user.id
            subscription_status = sql.execute("SELECT subscription_status FROM users WHERE id = ?", (user_id,)).fetchone()
            if subscription_status and subscription_status[0] == 'active':
                if callback.message:
                    await callback.message.delete()
                await bot.send_message(chat_id=callback.from_user.id, text='test', reply_markup=PloshakdiParser)
            else:
                await callback.answer("У Вас нет активной подписки.", show_alert=True)



        elif type == "List":
            if callback.message:
                await callback.message.delete()
            await start_message(callback)


        elif type == "Test":
            await test_subscription_handler(callback)


        elif type == "Close":
            if callback.message:
                await callback.message.delete()

    elif callback.data.startswith("Sub"):
        split = callback.data.split("_")
        type = split[1]
        if type == "1day":
            if callback.message:
                await callback.message.delete()
            await bot.send_message(chat_id=callback.from_user.id, text="Выберите способ пополнения:", reply_markup=SubChange1)

        elif type == "3day":
            if callback.message:
                await callback.message.delete()
            await bot.send_message(chat_id=callback.from_user.id, text="Выберите способ пополнения:", reply_markup=SubChange3)

        elif type == "7day":
            if callback.message:
                await callback.message.delete()
            await bot.send_message(chat_id=callback.from_user.id, text="Выберите способ пополнения:", reply_markup=SubChange7)


        elif type == "30day":
            if callback.message:
                await callback.message.delete()
            await bot.send_message(chat_id=callback.from_user.id, text="Выберите способ пополнения:", reply_markup=SubChange30)



        elif type == "Promo":
            if callback.message:
                await callback.message.delete()
            await bot.send_message(chat_id=callback.from_user.id, text="<b>Введите промокод:</b>",
                                   reply_markup=BackMenu)
            await Promo.Ask.msg.set()

        elif type == "CryptoBot1":
            if callback.message:
                await callback.message.delete()
            await bot.send_message(chat_id=callback.from_user.id, text="Выберите криптовалюту:", reply_markup=CryptaChoise1)

        elif type == "CryptoBot3":
            if callback.message:
                await callback.message.delete()
            await bot.send_message(chat_id=callback.from_user.id, text="Выберите криптовалюту:", reply_markup=CryptaChoise3)


        elif type == "CryptoBot7":
            if callback.message:
                await callback.message.delete()
            await bot.send_message(chat_id=callback.from_user.id, text="Выберите криптовалюту:", reply_markup=CryptaChoise7)



        elif type == "CryptoBot30":
            if callback.message:
                await callback.message.delete()
            await bot.send_message(chat_id=callback.from_user.id, text="Выберите криптовалюту:", reply_markup=CryptaChoise30)


        # ОПЛАТА НА 1 ДЕНЬ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        elif type == "BTC1":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "BTC", "0.000023", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"                                                  
                                                                       f"<b>Ссылка для оплаты: </b> \n"
                                                                       f"<b>{pay_url}</b>", disable_web_page_preview=True, reply_markup=ProverkaOplata)

        elif type == "TON1":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "TON", "0.341225", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"                                                  
                                                                       f"<b>Ссылка для оплаты: </b> \n"
                                                                       f"<b>{pay_url}</b>", disable_web_page_preview=True, reply_markup=ProverkaOplata)

        elif type == "USDC1":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "USDC", "0.6243", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"                                                  
                                                                       f"<b>Ссылка для оплаты: </b> \n"
                                                                       f"<b>{pay_url}</b>", disable_web_page_preview=True, reply_markup=ProverkaOplata)


        elif type == "ETH1":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "ETH", "0.000345", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"                                                  
                                                                       f"<b>Ссылка для оплаты: </b> \n"
                                                                       f"<b>{pay_url}</b>", disable_web_page_preview=True, reply_markup=ProverkaOplata)


        elif type == "USDT1":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "USDT", "0.62345", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"                                                  
                                                                       f"<b>Ссылка для оплаты: </b> \n"
                                                                       f"<b>{pay_url}</b>", disable_web_page_preview=True, reply_markup=ProverkaOplata)


        elif type == "BUSD1":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "BUSD", "0.6232", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"                                                  
                                                                       f"<b>Ссылка для оплаты: </b> \n"
                                                                       f"<b>{pay_url}</b>", disable_web_page_preview=True, reply_markup=ProverkaOplata)



        # ОПЛАТА НА 3 ДНЕЙ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        elif type == "BTC3":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "BTC", "0.00007", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"                                                  
                                                                       f"<b>Ссылка для оплаты: </b> \n"
                                                                       f"<b>{pay_url}</b>", disable_web_page_preview=True, reply_markup=ProverkaOplata)

        elif type == "TON3":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "TON", "1.03", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"                                                  
                                                                       f"<b>Ссылка для оплаты: </b> \n"
                                                                       f"<b>{pay_url}</b>", disable_web_page_preview=True, reply_markup=ProverkaOplata)



        elif type == "USDC3":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "USDC", "1.87", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"                                                  
                                                                       f"<b>Ссылка для оплаты: </b> \n"
                                                                       f"<b>{pay_url}</b>", disable_web_page_preview=True, reply_markup=ProverkaOplata)




        elif type == "ETH3":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "ETH", "0.001033", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"                                                  
                                                                       f"<b>Ссылка для оплаты: </b> \n"
                                                                       f"<b>{pay_url}</b>", disable_web_page_preview=True, reply_markup=ProverkaOplata)



        elif type == "USDT3":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "USDT", "1.87", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"                                                  
                                                                       f"<b>Ссылка для оплаты: </b> \n"
                                                                       f"<b>{pay_url}</b>", disable_web_page_preview=True, reply_markup=ProverkaOplata)


        elif type == "BUSD3":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "BUSD", "1.87", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"
                                                                           f"<b>Ссылка для оплаты: </b> \n"
                                                                           f"<b>{pay_url}</b>",
                                       disable_web_page_preview=True, reply_markup=ProverkaOplata)

# ОПЛАТА НА 7 ДНЕЙ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        elif type == "BTC7":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "BTC", "0.00014", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"                                                  
                                                                       f"<b>Ссылка для оплаты: </b> \n"
                                                                       f"<b>{pay_url}</b>", disable_web_page_preview=True, reply_markup=ProverkaOplata)

        elif type == "TON7":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "TON", "2.05", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"                                                  
                                                                       f"<b>Ссылка для оплаты: </b> \n"
                                                                       f"<b>{pay_url}</b>", disable_web_page_preview=True, reply_markup=ProverkaOplata)



        elif type == "USDC7":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "USDC", "3.74", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"                                                  
                                                                       f"<b>Ссылка для оплаты: </b> \n"
                                                                       f"<b>{pay_url}</b>", disable_web_page_preview=True, reply_markup=ProverkaOplata)




        elif type == "ETH7":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "ETH", "0.002062", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"                                                  
                                                                       f"<b>Ссылка для оплаты: </b> \n"
                                                                       f"<b>{pay_url}</b>", disable_web_page_preview=True, reply_markup=ProverkaOplata)



        elif type == "USDT7":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "USDT", "3.74", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"                                                  
                                                                       f"<b>Ссылка для оплаты: </b> \n"
                                                                       f"<b>{pay_url}</b>", disable_web_page_preview=True, reply_markup=ProverkaOplata)


        elif type == "BUSD7":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "BUSD", "3.74", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"
                                                                           f"<b>Ссылка для оплаты: </b> \n"
                                                                           f"<b>{pay_url}</b>",
                                       disable_web_page_preview=True, reply_markup=ProverkaOplata)


    # ОПЛАТА НА 7 ДНЕЙ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



        elif type == "BTC30":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "BTC", "0.000558", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"                                                  
                                                                       f"<b>Ссылка для оплаты: </b> \n"
                                                                       f"<b>{pay_url}</b>", disable_web_page_preview=True, reply_markup=ProverkaOplata)

        elif type == "TON30":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "TON", "8.2", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"                                                  
                                                                       f"<b>Ссылка для оплаты: </b> \n"
                                                                       f"<b>{pay_url}</b>", disable_web_page_preview=True, reply_markup=ProverkaOplata)



        elif type == "USDC30":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "USDC", "14.9", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"                                                  
                                                                       f"<b>Ссылка для оплаты: </b> \n"
                                                                       f"<b>{pay_url}</b>", disable_web_page_preview=True, reply_markup=ProverkaOplata)




        elif type == "ETH30":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "ETH", "0.008247", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"                                                  
                                                                       f"<b>Ссылка для оплаты: </b> \n"
                                                                       f"<b>{pay_url}</b>", disable_web_page_preview=True, reply_markup=ProverkaOplata)



        elif type == "USDT30":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "USDT", "14.9", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"                                                  
                                                                       f"<b>Ссылка для оплаты: </b> \n"
                                                                       f"<b>{pay_url}</b>", disable_web_page_preview=True, reply_markup=ProverkaOplata)


        elif type == "BUSD30":

            # Создайте платеж и получите ссылку на оплату
            invoice_id, pay_url = create_invoice(api_token, "BUSD", "14.9", "Оплата товара")
            if invoice_id and pay_url:
                await bot.send_message(chat_id=callback.from_user.id, text=f"— Номер счета: {invoice_id} \n"
                                                                           f"\n"
                                                                           f"\n"
                                                                           f"<b>Ссылка для оплаты: </b> \n"
                                                                           f"<b>{pay_url}</b>",
                                       disable_web_page_preview=True, reply_markup=ProverkaOplata)




    elif callback.data.startswith("Admin"):
        split = callback.data.split("_")
        type = split[1]
        if type == "Msg":
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
        elif type == "Manuals":
            await callback.message.edit_text("<b>📚 Мануалы</b>",reply_markup=AdminManuals)

        elif type == "Balance":
            await callback.message.edit_text(text="Введите ID для начисления подписки:", reply_markup=BackMenu)
            await Balance.Ask.msg.set()

        elif type == "Support":
            btn_add = []
            question = sql.execute("SELECT key FROM tickets WHERE status = 0").fetchall()
            questionSupport = InlineKeyboardMarkup(row_width=2)
            for i in question:
                add = InlineKeyboardButton(f"#{i[0]}", callback_data=f"Tickets_Answer_{i[0]}")
                btn_add.append(add)
            for i in range(len(btn_add)):
                if len(btn_add) >= 2:
                    questionSupport.add(btn_add[0], btn_add[1])
                    btn_add.pop(0)
                    btn_add.pop(0)
                elif len(btn_add) == 1:
                    questionSupport.add(btn_add[0])
                    btn_add.pop(0)
            add = InlineKeyboardButton("↩️ Назад", callback_data="Menu_Admin")
            questionSupport.add(add)
            await callback.message.edit_text("<b>Тех.Поддержка</b>",reply_markup=questionSupport)
        elif type == "Rass":
            await callback.message.edit_text("<b>Введите текст для рассылки</b>",reply_markup=ReplyCancel)
            await Admin.Rass.msg.set()
        elif type == "Stat":
            all_users = sql.execute("SELECT count(key) FROM users").fetchone()
           # day_users = sql.execute("SELECT count(key) FROM users WHERE date = ?", (date.today(),)).fetchone()
           # week = datetime.date.today()-datetime.timedelta(days=7)
          #  #month = datetime.date.today()-datetime.timedelta(days=30)
          #  week_users = sql.execute("SELECT count(key) FROM users WHERE date BETWEEN ? and ?", (week, date.today(),)).fetchone()
          #  month_users = sql.execute("SELECT count(key) FROM users WHERE date BETWEEN ? and ?", (month, date.today(),)).fetchone()
            await callback.message.edit_text("<b>Статистика бота</b>\n\n"
                                             f"<b>— Всего пользователей: </b><code>{all_users[0]}</code>\n"
                                           ,reply_markup=BackAdmin)
    elif callback.data.startswith("Edit"):
        split = callback.data.split("_")
        type = split[1]
        if type == "Msg":
            type = split[2]
            sql.execute("UPDATE users SET temp = ? WHERE id = ?", (type.lower(), callback.from_user.id,))
            db.commit()
            await callback.message.edit_text(f"<b>Введите новый текст для {type.lower()}</b>",reply_markup=ReplyCancel)
            await Admin.Edit.msg.set()

    if callback.data.startswith("Parser"):
        split = callback.data.split("_")
        type = split[1]
        if type == "OlxUZ":
            await bot.send_message(chat_id=callback.from_user.id, text="Введите количество объявлений (от 0 до 50):",
                                   reply_markup=BackMenu)
            await ParseAdsData.MaxAds.msg.set()

def register_callbackhandler(dp:Dispatcher):
    dp.register_callback_query_handler(callbackhandler)