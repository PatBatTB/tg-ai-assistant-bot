from aiogram import Bot, Dispatcher, types
from aiogram.client.session.aiohttp import AiohttpSession
from bot.handlers import routers

class TgBot:
    def __init__(self, token: str, proxy_url):
        self.session = AiohttpSession(proxy=proxy_url) if proxy_url else None
        self.bot = Bot(token=token, session=self.session)
        self.dp = Dispatcher()
        self.dp.include_routers(*routers)

    async def run(self):
        await self.dp.start_polling(self.bot)
