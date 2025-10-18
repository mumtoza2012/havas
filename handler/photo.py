from aiogram import types, Router
from aiogram.filters import Command
photo ="https://c8.alamy.com/comp/G4C2RX/pa-news-phot0-31398-the-princess-royal-arriving-on-fair-isle-today-G4C2RX.jpg"


router = Router()


@router.message(Command("photo"))
async def send_message(message: types.Message):
    await message.answer_photo(photo=photo)