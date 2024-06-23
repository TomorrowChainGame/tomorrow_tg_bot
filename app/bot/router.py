from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def message(message: Message):
    await message.answer(text=str(message.text))
