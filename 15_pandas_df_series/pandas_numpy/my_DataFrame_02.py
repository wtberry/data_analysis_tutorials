import pandas as pd
from pandas import Series
na_log = pd.read_csv('log_file_na.csv', names = ['name', 'email', 'fm_ip', 'to_ip', 'date_time', 'lat', 'long', 'payload_size'])

print('long and latitudes\n', na_log.long, na_log.lat)

dif = na_log.long - na_log.lat
dif_r = round(dif, 0)
print('dif, rounded', dif_r.unique())
