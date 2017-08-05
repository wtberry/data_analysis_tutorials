import sqlite3
import csv

conn = sqlite3.connect('my_first_sql.db')

sql = '''CREATE TABLE stocks (symbol text, date date, open_price float, close float, volume integer)'''

try:
    conn.execute(sql)
except:
    pass

fin = open('AMEX_daily_prices_N.csv')
fin.readline()
f = csv.reader(fin)

for row in f:
    symbol, date, openp, close, volume = row[1],row[2],row[3],row[6],row[-2],
    #print(symbol, date, openp, close, volume)
    conn.execute('INSERT INTO stocks VALUES (?, ?, ?, ?, ?)', (symbol, date, openp, close, volume))

cur = conn.cursor()
r = 'SELECT * FROM stocks'
for row in cur.execute(r):
    print('from the table:', row)
