from gc import callbacks

from aiogram import types, Router
from aiogram.filters import Command
from handler.photo import photo
from keyboard.default_keyboard import main_keyboard

photo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTL3uSZsVHEk0xpw0LpIMuPpMiEGjpkVPkGJQ&s"


router = Router()


@router.message(Command('start'))
async def send_message(message: types.Message):
    await message.answer_photo(photo=photo,
                         caption = """Приветствую Вас, я HR-бот Havas

🤖Я:
- расскажу Вам о компании и о преимуществах работы у нас;
- помогу найти актуальные вакансии и заполнить анкету.

_______________________________________

Xush kelibsiz, men HR-bot Havas

🤖Men:
- sizga kompaniya haqida va biz bilan ishlashning afzalliklari haqida gapirib beraman;
- mavjud vakansiyalarni topishga va so'rovnomani to'ldirishga yordam beraman.""",
                               reply_markup=main_keyboard())