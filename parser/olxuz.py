from datetime import datetime, timedelta
from aiogram import types, Dispatcher
from other.states import *
from handlers.callbackhandler import *
from other.keyboards import *
from parser.carousellcommy import parse_ad
import asyncio
from create_bot import *


async def parse_ads(message: types.Message, state=ParseAdsData.MaxAds.msg.set()):
    ads_kolvo = 0  # Инициализация переменной ads_kolvo

    try:
        ads_kolvo = int(message.text)
    except ValueError:
        await bot.send_message(chat_id=message.from_user.id,
                               text="Некорректное количество объявлений. Пожалуйста, введите число.")
        return

    await state.update_data(ads_kolvo=ads_kolvo)
    await ParseAdsData.Views.msg.set()

    await bot.send_message(chat_id=message.from_user.id, text="Введите количество просмотров:", reply_markup=BackMenu)


async def views(message: types.Message, state):
    try:
        views_kolvo = int(message.text)
    except ValueError:
        await message.answer("Некорректное количество просмотров. Пожалуйста, введите число.")
        return
    await state.update_data(views_kolvo=views_kolvo)

    await bot.send_message(chat_id=message.from_user.id, text="Введите количество объявлений пользователя:", reply_markup=BackMenu)
    await ParseAdsData.MaxUserAds.msg.set()


async def user_ads(message: types.Message, state):
    try:
        user_ads_count = int(message.text)
    except ValueError:
        await message.answer("Некорректное количество объявлений пользователя. Пожалуйста, введите число.")
        return
    
    async with state.proxy() as data:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f'Начинаем поиск объявлений. \n Кол-во объявлений: {data["ads_kolvo"]}', reply_markup=StopParser)

        ads = parse_ad(
            data['ads_kolvo'],
            data['views_kolvo'],
            user_ads_count
        )

        text = '<b>Название товара:</b> {title}\n' \
                '<b>Стоимость товара:</b> {price}\n\n' \
                '<a href="{seller_link}">Переход на продавца</a>\n' \
                '<a href="{link}">Переход на объявление</a>\n\n' \
                '<b>Дата публикации: {pub_date}</b>\n\n' \
                '<b>Количество объявлений у продавца:</b> {seller_ads_count}\n' \
                '<b>Количество просмотров:</b> {views_count}'

        for ad in ads:
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=ad['image_link'],
                caption=text.format(
                    title=ad['title'],
                    price=ad['price'],
                    seller_link=ad['seller_link'],
                    link=ad['link'],
                    pub_date=ad['pub_date'],
                    seller_ads_count=ad['seller_ads_count'],
                    views_count=ad['views_count']
                ),
                parse_mode='HTML'
            )

        await asyncio.sleep(1)

        await bot.send_message(
            chat_id=message.from_user.id,
            text="✅ Парсинг завершен!", reply_markup=DeleteButton
        )


async def cancel(callback: types.CallbackQuery, state=ParseAdsData.MaxAds.msg):
    await state.finish()
    await callback.message.delete()
    with open('menu.png', 'rb') as photo:
        await bot.send_photo(chat_id=callback.from_user.id, photo=photo,
                             reply_markup=await GetMenuButtons(callback.from_user.id))

def register_olxuz(dp: Dispatcher):
    dp.register_message_handler(parse_ads, state=ParseAdsData.MaxAds.msg)
    dp.register_message_handler(views, state=ParseAdsData.Views.msg)
    dp.register_message_handler(user_ads, state=ParseAdsData.MaxUserAds.msg)
