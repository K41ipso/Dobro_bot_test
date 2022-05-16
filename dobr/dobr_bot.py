from aiogram.utils import executor 
from create_bot import dp 
from data_base import sqlite_db
import asyncio
import aioschedule

async def on_startup(_):
	asyncio.create_task(client.scheduler())
	print('Bot is online.')
	sqlite_db.sql_start()


from handlers import client

client.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

