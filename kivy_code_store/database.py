import sqlite3
con = sqlite3.connect('sacks.db')
c = con.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS shirt
	(theme integer)''')



#c.execute('''INSERT  INTO  shirt VALUES
#('skucolor 1', 'anania shirt','24',250) ''')
c.execute('''INSERT INTO shirt VALUES (50)''')


#c.execute('DELETE FROM shirt WHERE price  ')

c.execute('UPDATE shirt SET theme = 200 WHERE theme  ')
#man = c.fetchmany(2)

#for man in c.execute('SELECT price FROM shirt'):
c.execute('SELECT theme FROM shirt')
man = c.fetchone()
print(man)

con.commit()
con.close()












