from aiogram import types, Router,F
from aiogram.filters import Command

from keyboard.default_keyboard import main1_keyboard, main3_keyboard, til_keyboard, til2_keyboard, til3_keyboard
from keyboard.default_keyboard import main_keyboard
from keyboard.default_keyboard import main2_keyboard

photo ="https://www.gazeta.uz/media/img/2020/03/sHjOtR15830234652152_b.jpg"
photo1="https://uznews.uz/storage/uploads/2025/5/7/file_681adf5dbc64d_orig.jpg"
photo2 = "https://www.gazeta.uz/media/img/2023/03/lotzFh16780847845486_l.jpg"



router = Router()


@router.message(F.text == "🏢 О нас")
async def send_message(message: types.Message):
    await message.answer_photo(photo=photo ,
                               caption="""🌠HAVAS

📌СЕТЬ ДИСКАУНТЕРОВ "У ДОМА"
Мы предлагаем нашим покупателям качественные продукты по выгодной цене.                                            
В наших магазинах представлены товары известных мировых и локальных брендов,
а также товары собственного производства.""",
                               reply_markup = main3_keyboard())


@router.message(F.text == "Назад2")
async def send_message(message: types.Message):
    await message.answer( text="Назад",
                        reply_markup = main_keyboard() )


@router.message(F.text == "💼 Оставить заявку")
async def send_message(message: types.Message):
    await message.answer( text="📍 Выберите регион",
                        reply_markup = main1_keyboard() )


@router.message(F.text == "Назад")
async def send_message(message: types.Message):
    await message.answer( text="Назад",
                        reply_markup = main_keyboard() )

@router.message(F.text == "📞 Контакты")
async def send_message(message: types.Message):
    await message.answer_photo( photo=photo1  ,
                        caption="""🤝Для связи:
☎️Контакты +998 71 205 95 95
📩Электронная почта havas_uz@mail.ru""")


@router.message(F.text == "💬 Отзывы и предложения")
async def send_message(message: types.Message):
    await message.answer( text="Напишите нам сюда, мы обязательно ответим.", )


@router.message(F.text == "🇷🇺/🇺🇿 Tilni o'zgartirish")
async def send_message(message: types.Message):
    await message.answer( text="Поменять язык"
                    , reply_markup= main2_keyboard())

@router.message(F.text == "Назад1")
async def send_message(message: types.Message):
    await message.answer( text="Назад",
                        reply_markup = main_keyboard() )

@router.message(F.text == "Беруний")
async def send_message(message: types.Message):
    await message.answer( text="Заявка успешно принята.", )

@router.message(F.text == "Ц-1")
async def send_message(message: types.Message):
    await message.answer( text="Заявка успешно принята.", )

@router.message(F.text == "Узбекский")
async def send_message(message: types.Message):
    await message.answer( text="Поменять язык"
                    , reply_markup= til_keyboard())


@router.message(F.text == "Русский")
async def send_message(message: types.Message):
    await message.answer( text="Поменять язык"
                    , reply_markup= main_keyboard())



@router.message(F.text == "🇷🇺/🇺🇿 Смена языка")
async def send_message(message: types.Message):
    await message.answer( text="Поменять язык"
                    , reply_markup= til2_keyboard())


@router.message(F.text == "🔰 Дискаунтер — это")
async def send_message(message: types.Message):
    await message.answer_photo( photo=photo2
    ,caption="""Дискаунтер — это выгодный для потребителей формат магазинов, в котором продаются товары по цене ниже обычной

В дискаунтере низкие цены достигаются за счет снижения издержек, многофункциональности персонала и лучших условий с поставщиками

Для удобства посетителей, ассортимент подбирается таким образом, что на полках всегда можно найти все самое необходимое

Сеть дискаунтеров Havas еще удобна и тем, что расположена рядом с потребителями. Можно совершать выгодные покупки недалеко от дома""", )



@router.message(F.text == "📍Ближайший Филиал")
async def send_message(message: types.Message):
    await message.answer( text="Отправьте свое местоположение для определения ближайшего филиала",
                          reply_markup=til3_keyboard())

@router.message(F.text == "Главное меню")
async def send_message(message: types.Message):
    await message.answer( text="Назад",
                        reply_markup = main_keyboard() )


