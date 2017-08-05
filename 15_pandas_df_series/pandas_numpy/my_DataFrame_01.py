import numpy as np
import pandas as pd
from pandas import Series

na_log = pd.read_csv('log_file_na.csv', names = ['name', 'email', 'fm_ip', 'to_ip', 'date_time', 'lat', 'long', 'payload_size'])
print(na_log) 

pan_s = Series(na_log['payload_size'])
minimum = pan_s.min()
print(minimum)
maximum = pan_s.max()
print(maximum)

delta = maximum - minimum
print('delta by python built in max_min:', delta)
