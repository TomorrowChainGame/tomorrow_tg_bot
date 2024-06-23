import asyncio

from bot.settings import settings
from bot.main import dp
from bot.bot import bot


if __name__ == "__main__":
    if settings.DEBUG:
        import logging

        logging.basicConfig(level=logging.DEBUG)

    asyncio.run(dp.start_polling(bot))
