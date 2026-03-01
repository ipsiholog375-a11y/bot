import asyncio

from loader import bot, dp, logger
from routes import router
from stats import init_db


async def main() -> None:
    init_db()
    dp.include_router(router)
    logger.info("Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


