from aiogram.dispatcher.filters.state import StatesGroup, State

class Admin(StatesGroup):
    class Edit(StatesGroup):
        msg = State()
    class Rass(StatesGroup):
        msg = State()

class Manuals(StatesGroup):
    add_name = State()
    add_url = State()

class Tickets(StatesGroup):
    class Answer(StatesGroup):
        msg = State()
    class Ask(StatesGroup):
        msg = State()

class QR(StatesGroup):
    class Answer(StatesGroup):
        msg = State()
    class Ask(StatesGroup):
        msg = State()

class Balance(StatesGroup):
    class Duration(StatesGroup):
        msg = State()
    class Ask(StatesGroup):
        msg = State()

class Promo(StatesGroup):
    class Ask(StatesGroup):
        msg = State()


class ParseAdsData(StatesGroup):
    class MaxAds(StatesGroup):
        msg = State()

    class MaxUserAds(StatesGroup):
        msg = State()

    class Views(StatesGroup):
        msg = State()

    class RegistrationDate(StatesGroup):
        msg = State()

    class CreationDate(StatesGroup):
        msg = State()