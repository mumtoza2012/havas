from aiogram import Router
from keyboard import default_keyboard

router = Router()

def setup_message_router():
    router.include_router(default_keyboard.router)

    return router