from aiogram import Router
from handler import start
from handler import help
from handler import photo
from handler import about

router = Router()

def setup_message_router():
    router.include_router(start.router)
    router.include_router(help.router)
    router.include_router(about.router)

    return router