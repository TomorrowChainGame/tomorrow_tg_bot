from aiogram import Dispatcher
from .router import router


dp = Dispatcher()


dp.include_router(router)
