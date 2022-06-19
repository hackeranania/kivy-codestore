import sqlite3
con = sqlite3.connect('jart.db')
c = con.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS shirt
	(theme text)''')



#c.execute('''INSERT  INTO  shirt VALUES
#('skucolor 1', 'anania shirt','24',250) ''')
c.execute('''INSERT INTO shirt VALUES ('Dark')''')


#c.execute('DELETE FROM shirt WHERE price  ')

c.execute('UPDATE shirt SET theme ="Light" ')
#man = c.fetchmany(2)

#for man in c.execute('SELECT price FROM shirt'):
c.execute('SELECT theme FROM shirt')
man = c.fetchone()

sawo = str(man)
fi = sawo.replace('(','')
tw = fi.replace(')','')
thr = tw.replace(',','')
print(thr)
con.commit()
con.close()












