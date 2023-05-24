from aiogram.utils import executor
from create_bot import dp
from handlers import messagehandler, callbackhandler, edit_msg, admin_rass, add_balance, promocode
from parser import olxuz


messagehandler.register_message(dp)
callbackhandler.register_callbackhandler(dp)
edit_msg.register_editmsg(dp)
admin_rass.register_adminrass(dp)
add_balance.register_addbalance(dp)
promocode.register_addpromo(dp)
olxuz.register_olxuz(dp)


if __name__ == '__main__':
    print(f'==============================\nBOT started!\n==============================\n')
    executor.start_polling(dp)

