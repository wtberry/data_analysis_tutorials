import csv
import pandas as pd

fin =  pd.read_csv('log_file_1000.csv', names=['name', 'email', 'fmip', 'toip', 'datetime', 'lat', 'long', 'payload'])

count = 0
fin['bol'] = fin.fmip == fin.toip       
print(fin.bol.value_counts())
print('unique', len(fin.payload.unique()))
v_count = fin.fmip.value_counts()
print('max', max(v_count))
print('min', min(v_count))

