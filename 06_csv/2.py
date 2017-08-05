import csv

def rod(lat, lon):
    rlat = round(float(lat), 2)
    rlon = round(float(lon), 2)
    return rlat, rlon

fin = open('folder/log_file_1000.csv')
csv_log = csv.reader(fin)

for fields in csv_log:
    name, email, s_ip, d_ip, date_time, lat, lon, num = fields
    rlat, rlon = rod(lat, lon)
    print('\n', 'latitude:', rlat, 'longtitude:', rlon, date_time)
