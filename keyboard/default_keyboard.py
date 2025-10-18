from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard():
    button = KeyboardButton(text="🏢 О нас")
    button2 = KeyboardButton(text="💼 Оставить заявку")
    button3 = KeyboardButton(text="📞 Контакты")
    button4 = KeyboardButton(text="💬 Отзывы и предложения")
    button5 = KeyboardButton(text="🇷🇺/🇺🇿 Tilni o'zgartirish")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button2],
            [button3, button4],
            [button5]
        ],
        resize_keyboard=True
    )
    return rkm


def main1_keyboard():
    button = KeyboardButton(text="Беруний")
    button1 = KeyboardButton(text="Ц-1")
    button2 = KeyboardButton(text="Назад")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button1],
            [button2]
        ],
        resize_keyboard=True
    )
    return rkm

def main2_keyboard():
    button = KeyboardButton(text="Русский")
    button1 = KeyboardButton(text="Узбекский")
    button2 = KeyboardButton(text="Назад1")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button1],
            [button2]
        ],
        resize_keyboard=True
    )
    return rkm

def main3_keyboard():
    button = KeyboardButton(text="🔰 Дискаунтер — это")
    button1 = KeyboardButton(text="📍Ближайший Филиал")
    button2 = KeyboardButton(text="Назад2")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button1],
            [button2]
        ],
        resize_keyboard=True
    )
    return rkm

def til_keyboard():
    button = KeyboardButton(text="🏢  Biz haqimizda")
    button2 = KeyboardButton(text="💼 Ariza qoldiring")
    button3 = KeyboardButton(text="📞 Kontaktlar")
    button4 = KeyboardButton(text="💬 Qayta aloqa")
    button5 = KeyboardButton(text="🇷🇺/🇺🇿 Смена языка")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button2],
            [button3, button4],
            [button5]
        ],
        resize_keyboard=True
    )
    return rkm
# ds
def til2_keyboard():
    button = KeyboardButton(text="Русский")
    button1 = KeyboardButton(text="O'zbekcha")
    button2 = KeyboardButton(text="Назад1")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button1],
            [button2]
        ],
        resize_keyboard=True
    )
    return rkm

def til3_keyboard():
    button = KeyboardButton(text="Отправить геопозицию")
    button2 = KeyboardButton(text="Главное меню")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
        ],
        resize_keyboard=True
    )
    return rkm









