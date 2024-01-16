import asyncio

import handlers.menu_handlers
from config import bot, dp
from middlware.usercheck_middlware import UserCheckMessageMiddleware, UserCallbackCheckMiddleware

import logging


async def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s] - %(name)s - '
                               '(%(filename)s).%(funcName)s(%(lineno)d - %(message)s')

    dp.message.middleware.register(UserCheckMessageMiddleware())
    dp.callback_query.middleware.register(UserCallbackCheckMiddleware())
    dp.include_routers(handlers.menu_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
