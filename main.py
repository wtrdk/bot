import asyncio
import telegram
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


async def main():
    bot = telegram.Bot("TOKEN")
    async with bot:

        print((await bot.get_updates())[0])
