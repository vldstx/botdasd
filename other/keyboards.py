from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


cancel = InlineKeyboardButton("↩️ Назад", callback_data="Menu_List")

MenuButtons = InlineKeyboardMarkup(row_width=2)
mb_1 = InlineKeyboardButton("💬Парсинг", callback_data="Menu_Parser")
mb_2 = InlineKeyboardButton("📢Подписка", callback_data="Menu_Sub")
mb_3 = InlineKeyboardButton('✍Информация', callback_data='Menu_Info')
mb_4 = InlineKeyboardButton('❗Тестовая подписка❗', callback_data='Menu_Test')
MenuButtons.add(mb_1,mb_2).row(mb_3).row(mb_4)
BackMenu = InlineKeyboardMarkup(row_width=1)
bm_1 = InlineKeyboardButton("↩️ Назад", callback_data="Menu_List")
BackMenu.add(bm_1)

AdminPanel = InlineKeyboardMarkup(row_width=2)
ap_1 = InlineKeyboardButton("💬 Начислить подписку", callback_data="Admin_Balance")
ap_2 = InlineKeyboardButton("Рассылка", callback_data="Admin_Rass")
ap_3 = InlineKeyboardButton("📊 Статистика", callback_data="Admin_Stat")
ap_back = InlineKeyboardButton("↩️ Назад", callback_data="Menu_List")
AdminPanel.add(ap_1,ap_2).row(ap_3).row(ap_back)

AdminMenuButtons = InlineKeyboardMarkup(row_width=2)
AdminMenuButtons.add(mb_1,mb_2).row(mb_3, mb_4)
AdminMenuButtons.add(
    InlineKeyboardButton("⚠️ Админ панель", callback_data="Menu_Admin")
)

ReplyCancel = InlineKeyboardMarkup(row_width=2)
ReplyCancel.add(cancel)

NoneReply = InlineKeyboardMarkup(row_width=1)

AdminManuals = InlineKeyboardMarkup(row_width=2)
am_1 = InlineKeyboardButton("➖ Удалить мануал", callback_data="Manuals_Remove")
am_2 = InlineKeyboardButton("➕ Добавить мануал", callback_data="Manuals_Add")
am_3 = InlineKeyboardButton("↩️ Назад", callback_data="Menu_Admin")
AdminManuals.add(am_1,am_2).row(am_3)

BackAdmin = InlineKeyboardMarkup(row_width=2)
ba_1 = InlineKeyboardButton("↩️ Назад", callback_data="Menu_Admin")
BackAdmin.add(ba_1)


SubBuy = InlineKeyboardMarkup(row_width=2)
sb_1 = InlineKeyboardButton('1 день [50 RUB]', callback_data='Sub_1day')
sb_2 = InlineKeyboardButton('3 дня [150 RUB]', callback_data='Sub_3day')
sb_3 = InlineKeyboardButton('7 дней [300 RUB]', callback_data='Sub_7day')
sb_4 = InlineKeyboardButton('30 дней [1200 RUB]', callback_data='Sub_30day')
sb_back = InlineKeyboardButton("↩️ Назад", callback_data="Menu_List")
SubBuy.add(sb_1,sb_2).row(sb_3,sb_4).row(sb_back)

ProverkaOplata = InlineKeyboardMarkup(row_width=1)
po_1 = InlineKeyboardButton('Проверить оплату', callback_data='Sub_Proverka')
ProverkaOplata.add(po_1)

SubChange1 = InlineKeyboardMarkup(row_width=2)
sc_1 = InlineKeyboardButton('CryptoBot', callback_data='Sub_CryptoBot1')
sc_back = InlineKeyboardButton('↩️ Назад', callback_data='Menu_List')
SubChange1.add(sc_1).row(sb_back)

SubChange3 = InlineKeyboardMarkup(row_width=2)
sc_1 = InlineKeyboardButton('CryptoBot', callback_data='Sub_CryptoBot3')
sc_back = InlineKeyboardButton('↩️ Назад', callback_data='Menu_List')
SubChange3.add(sc_1).row(sb_back)

SubChange7 = InlineKeyboardMarkup(row_width=2)
sc_1 = InlineKeyboardButton('CryptoBot', callback_data='Sub_CryptoBot7')
sc_back = InlineKeyboardButton('↩️ Назад', callback_data='Menu_List')
SubChange7.add(sc_1).row(sb_back)


SubChange30 = InlineKeyboardMarkup(row_width=2)
sc_1 = InlineKeyboardButton('CryptoBot', callback_data='Sub_CryptoBot30')
sc_back = InlineKeyboardButton('↩️ Назад', callback_data='Menu_List')
SubChange30.add(sc_1).row(sb_back)

CryptaChoise1 = InlineKeyboardMarkup(row_width=3)
cs_1 = InlineKeyboardButton('BTC', callback_data='Sub_BTC1')
cs_2 = InlineKeyboardButton('TON', callback_data='Sub_TON1')
cs_3 = InlineKeyboardButton('USDC', callback_data='Sub_USDC1')
cs_4 = InlineKeyboardButton('ETH', callback_data='Sub_ETH1')
cs_5 = InlineKeyboardButton('USDT', callback_data='Sub_USDT1')
cs_6 = InlineKeyboardButton('BUSD', callback_data='Sub_BUSD1')
cs_back = InlineKeyboardButton('↩️ Назад', callback_data='Menu_List')
CryptaChoise1.add(cs_1,cs_2,cs_3).row(cs_4,cs_5,cs_6).row(cs_back)

CryptaChoise3 = InlineKeyboardMarkup(row_width=3)
cs_1 = InlineKeyboardButton('BTC', callback_data='Sub_BTC3')
cs_2 = InlineKeyboardButton('TON', callback_data='Sub_TON3')
cs_3 = InlineKeyboardButton('USDC', callback_data='Sub_USDC3')
cs_4 = InlineKeyboardButton('ETH', callback_data='Sub_ETH3')
cs_5 = InlineKeyboardButton('USDT', callback_data='Sub_USDT3')
cs_6 = InlineKeyboardButton('BUSD', callback_data='Sub_BUSD3')
cs_back = InlineKeyboardButton('↩️ Назад', callback_data='Menu_List')
CryptaChoise3.add(cs_1,cs_2,cs_3).row(cs_4,cs_5,cs_6).row(cs_back)

CryptaChoise7 = InlineKeyboardMarkup(row_width=3)
cs_1 = InlineKeyboardButton('BTC', callback_data='Sub_BTC7')
cs_2 = InlineKeyboardButton('TON', callback_data='Sub_TON7')
cs_3 = InlineKeyboardButton('USDC', callback_data='Sub_USDC7')
cs_4 = InlineKeyboardButton('ETH', callback_data='Sub_ETH7')
cs_5 = InlineKeyboardButton('USDT', callback_data='Sub_USDT7')
cs_6 = InlineKeyboardButton('BUSD', callback_data='Sub_BUSD7')
cs_back = InlineKeyboardButton('↩️ Назад', callback_data='Menu_List')
CryptaChoise7.add(cs_1,cs_2,cs_3).row(cs_4,cs_5,cs_6).row(cs_back)

CryptaChoise30 = InlineKeyboardMarkup(row_width=3)
cs_1 = InlineKeyboardButton('BTC', callback_data='Sub_BTC30')
cs_2 = InlineKeyboardButton('TON', callback_data='Sub_TON30')
cs_3 = InlineKeyboardButton('USDC', callback_data='Sub_USDC30')
cs_4 = InlineKeyboardButton('ETH', callback_data='Sub_ETH30')
cs_5 = InlineKeyboardButton('USDT', callback_data='Sub_USDT30')
cs_6 = InlineKeyboardButton('BUSD', callback_data='Sub_BUSD30')
cs_back = InlineKeyboardButton('↩️ Назад', callback_data='Menu_List')
CryptaChoise30.add(cs_1,cs_2,cs_3).row(cs_4,cs_5,cs_6).row(cs_back)


PloshakdiParser = InlineKeyboardMarkup(row_width=2)
pp_1 = InlineKeyboardButton('olx.uz🇺🇿', callback_data='Parser_OlxUZ')
pp_back = InlineKeyboardButton('↩️ Назад', callback_data='Menu_List')
PloshakdiParser.add(pp_1).row(pp_back)


StopParser = InlineKeyboardMarkup(row_width=1)
sp_1 = InlineKeyboardButton('❌Остановить парсинг❌', callback_data='Stop_Parser')
StopParser.add(sp_1)



DeleteButton = InlineKeyboardMarkup(row_width=1)
db_1 = InlineKeyboardButton('Удалить', callback_data='Menu_Close')
DeleteButton.add(db_1)

