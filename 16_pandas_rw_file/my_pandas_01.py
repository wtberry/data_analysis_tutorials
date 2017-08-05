import pandas as pd

data = pd.read_csv('log_file_sign.csv', names=['name', 'email', 'fmip', 'toip', 'datetime', 'lat', 'long', 'payload'], sep='!', skiprows=range(0, 1000, 2), index_col='datetime')
print()
print(data['2016-01-29T22:27:34':'2016-01-28T22:34:28'])
