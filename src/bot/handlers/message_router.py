from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def message_handler(message: Message):
    if message.text:
        await message.answer(message.text)
    else:
        await message.answer("Я могу отвечать только на текст.")