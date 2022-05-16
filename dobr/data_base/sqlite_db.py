import sqlite3 as sq 
from create_bot import dp, bot

def sql_start():
	global base, cur 
	base = sq.connect('dobr.db')
	cur = base.cursor()
	if base:
		print('Data base connected.')
	base.execute('CREATE TABLE IF NOT EXISTS gold(userid TEXT)')
	base.commit()


async def new_user(data):
	r = cur.execute('SELECT userid FROM gold WHERE userid == ?', (data,)).fetchone()
	if bool(r) is False:
		cur.execute('INSERT INTO gold VALUES(?)', (data,))
		base.commit()
	else:
		pass

async def delete_user(data):
	cur.execute('DELETE FROM gold WHERE userid == ?', (data,))
	base.commit()

def user_list():
	lst = cur.execute('SELECT * FROM gold').fetchall()
	return lst