import sqlite3 as sq3
import pandas as pd

conn = sq3.connect('log_file.sql')
cur = conn.cursor()

data = pd.read_sql("SELECT name, payload, datetime FROM superheroes WHERE payload > 486000 AND payload < 489500",conn)

print('min\n', data.payload.min())
print('max\n', data.payload.max())
print('median\n', data.payload.median())
print('payload\n',data.payload)
print(data.info())
