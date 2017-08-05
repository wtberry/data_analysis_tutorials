import csv

def UID(address):
    ind = address.index('@')

    UID = address[:ind]
    return UID    

fin = open('folder/log_file_1000.csv')

log = csv.reader(fin, delimiter = ',')

for line in log:
    name, email, s_ip, d_ip, date_time, lat, lon, num = line
    user_name = UID(email)
    print('user name:', user_name, 'latitude', lat, 'longtitude', lon)
