import datetime
from create_bot import sql, logging, save_logging
from other.keyboards import AdminMenuButtons, MenuButtons

async def is_int(str):
    try:
        int(str)
        return True
    except:
        return False

async def logger(text):
    if str(logging) == 1:
        print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S')}] {text}")
    if str(save_loging) == 1:
        with open('logs.txt', 'a', encoding='utf8') as f:
            f.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S')}] {text}\n")

async def GetMenuButtons(id):
    admin = sql.execute("SELECT admin FROM users WHERE id = ?", (id,)).fetchone()
    if int(admin[0]) == 1:
        return AdminMenuButtons
    else:
        return MenuButtons

async def get_info_user(id):
    result = {}
    username = sql.execute("SELECT username FROM users WHERE id = ?", (id,)).fetchone()
    balance = sql.execute("SELECT balance FROM users WHERE id = ?", (id,)).fetchone()
    admin = sql.execute("SELECT admin FROM users WHERE id = ?", (id,)).fetchone()
    logs = sql.execute("SELECT count(key) FROM logs WHERE id = ?", (id,)).fetchone()
    try:
        payments = sql.execute("SELECT count(key) FROM payments WHERE id = ?", (id,)).fetchone()
    except:
        payments = [0]
    ban = sql.execute("SELECT ban FROM users WHERE id = ?", (id,)).fetchone()
    if int(ban[0]) == 1:
        result['ban'] = "Заблокирован"
    else:
        result['ban'] = "Разблокирован"
    result['username'] = username[0]
    result['id'] = id
    result['balance'] = balance[0]
    if int(admin[0]) == 1:
        result['admin'] = "Администратор"
    else:
        result['admin'] = "Пользователь"
    result['logs'] = logs[0]
    result['payments'] = payments[0]

    return result