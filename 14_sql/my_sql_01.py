import sqlite3 as sq

conn = sq.connect('my_first_sql.db')
sql = '''CREATE TABLE stocks (symbol text, date date, open_price float, close float, volume integer)'''

try:
    conn.execute(sql)
except:
    pass


fin = open('AMEX_daily_prices_N.csv')
fin.readline()
insert = 'INSERT INTO stocks VALUES (?, ?, ?, ?, ?)'
for line in fin:
    exchange, symbol, date, open_price, high, low, close, volume, adjust = line.strip().split(',')
    #print(line)
    conn.execute(insert, (symbol, date, open_price, close, volume))

cur = conn.cursor()
reference = 'SELECT * FROM stocks'
print('table')
for row in cur.execute(reference):
    print(row)
conn.close()
