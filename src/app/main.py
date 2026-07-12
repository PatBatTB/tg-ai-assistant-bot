import asyncio
import logging

from bot.bot import TgBot
from settings.config import get_settings


async def main():
    logging.basicConfig(level=logging.INFO)
    settings = get_settings()
    bot = TgBot(
        token=settings.tg_bot.token.get_secret_value(),
        proxy_url=settings.proxy.get_url())
    await bot.run()

if __name__ == '__main__':
    asyncio.run(main())