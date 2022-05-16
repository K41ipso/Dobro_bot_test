from aiogram import types, Dispatcher
from create_bot import dp, bot
from data_base import sqlite_db
import asyncio
import aioschedule
import random
import datetime


async def commands_start(message : types.Message):
	user_channel_status = await bot.get_chat_member(chat_id='-1001535873670', user_id=message.from_user.id)
	if user_channel_status["status"] != 'left':
		await sqlite_db.new_user(message.from_user.id)
		await bot.send_message(chat_id=message.from_user.id, text='Добро пожаловать в Золотое Яблоко!')
	else:
		await bot.send_message(chat_id=message.from_user.id, text='К сожалению, у вас недостаточно прав на использование этого бота. Обратитесь к системному администратору')

async def command_stop(message : types.Message):
	await sqlite_db.delete_user(message.from_user.id)
	await bot.send_message(chat_id=message.from_user.id, text='До свидания! С наилучшими пожеланиями, Золотое Яблоко')


async def send_milosti():
	phrases_list = ['Бодрости духа!', 'Больших успехов!', 'Всего наилучшего и по высшему классу!', 'Желания идти вперёд!', 'Жизнелюбия!', 'Интересных идей!', 'Максимум позитива!', 'Мудрости и опыта!', 'Настойчивости и упорства!', 'Огонька и задора!', 'Оптимизма!', 'Приятных людей рядом!', 'Приятных открытий!', 'Процветания!', 'Радужной мечты!', 'Свершений!', 'Сияющего солнца!', 'Творчества и созидания!', 'Тёплого отношения окружающих!', 'Уважения!', 'Удачи во всех начинаниях!', 'Улыбок фортуны!', 'Фейерверка эмоций!', 'Чувства юмора!', 'Чуткости!', 'Широких возможностей!', 'Безграничного везенья!', 'Больших и маленьких побед!', 'Больших перспектив!', 'Браться смело за любое дело!', 'Быть всегда на высоте!', 'Будьте первыми!', 'Быть примером для всех!', 'Только позитива!', 'Видеть только лучшее во всем!', 'Во всех делах — ни пуха, ни пера!', 'Возможности заглянуть за горизонт!', 'Всегда делиться положительными эмоциями!', 'Всегда уметь сделать верный и правильный шаг!', 'Всегда уметь слушать и услышать!', 'Дарить добро!', 'День обычно удается, если весело смеешься!', 'Дерзких планов!', 'Доверия в коллективе!', 'Железного терпения!', 'Искренности во всем!', 'Легкости бытия!', 'Мудрости и процветания!', 'Найти нужное!', 'Не терять крепость духа!', 'Неугасаемого огня!', 'Никогда не унывать!', 'Никогда не уставать!', 'Одолеть любой крутой подъем!', 'Оставаться эталоном для всех!', 'Осчастливить кого-нибудь своим вниманием!', 'Отличного настроения!', 'Отличной формы!', 'Пленить всех умом и обаянием!', 'Покорения вершин!', 'Получить кучу комплиментов!', 'Помнить, что каждый день приносит радость!', 'Понимания и тепла!', 'Пусть все улыбаются!', 'Решать молниеносно все проблемы!', 'Свершения задуманного!', 'Светлых мыслей!', 'Совершенства во всем!', 'Теплых улыбок!', 'Чтобы любые идеи по плечу!', 'Чтобы позитив лился рекой!', 'Энергии на великие дела!', 'Карьерного роста!', 'Блестящих побед!', 'Успеха!', 'Хорошего дня!', 'Совершенства!', 'Покорения новых высот!', 'Доблестных дел!', 'Смелых начинаний!', 'Достижения целей!', 'Крутых достижений!', 'Наилучших результатов!', 'Твердости намерений!', 'Гениальных идей!', 'Чудесных перспектив!', 'Творческих находок!', 'Произвести фурор!', 'Быть всегда на высоте!', 'Верить в собственные силы!', 'Всё успевать!', 'Удачи во всем!', 'Радужного настроения!', 'Лучезарных улыбок!', 'Огонька!', 'Отличного дня!', 'Весны в душе!', 'Позитива!', 'Оптимизма!', 'Вдохновения!']
	lst = sqlite_db.user_list()
	for user in lst:
		await bot.send_message(chat_id=user[0], text=f'{random.choice(phrases_list)}')

async def scheduler():
	aioschedule.every().day.at("14:00").do(send_milosti)
	while True:
		await aioschedule.run_pending()
		await asyncio.sleep(1)

def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(commands_start, commands=['start', 'help'])
	dp.register_message_handler(command_stop, commands='stop')
	dp.register_message_handler(send_milosti, )
