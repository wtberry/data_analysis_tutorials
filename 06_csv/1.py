import csv 
def ip(ip_address):
    each_num = ip_address.split('.')
    if each_num[0] == '75':
        return True

fin = open('folder/log_file_1000.csv')
csv_log = csv.reader(fin)

for row in csv_log:
    name, email, s_ip, d_ip, date_time, lat, lon, num = row
    source = ip(s_ip)
    dest = ip(d_ip)
    if source == True or dest == True:
        print('\n', name, s_ip, d_ip, date_time)
    else:
        print('\n', name, s_ip, d_ip)
