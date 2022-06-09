import asyncio
import telegram


async def main():
    bot = telegram.Bot("5480140583:AAH5ZDrvrXMsLkIUSCQIsW97DTCemmoqTMM")
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())
