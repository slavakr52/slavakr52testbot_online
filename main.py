from loader import bot
from loader import dp
from aiogram.methods import DeleteWebhook
from app.handlers import router
import asyncio

async def main():
    dp.include_router(router)
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print ("Shutdown ...")