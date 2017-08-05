import csv

def conv(volume):
    num = str(round(int(volume)/1000000, 1))[0:3]
    num1 = num[0:2]
    num2 = num[2:]
    num3 = '.'.join([num1, num2])
    return num3 + 'M'

fin = open('folder/yahoo_prices_short.csv')
fin.readline()
csv_yahoo = csv.reader(fin)

for row in csv_yahoo:
    date, opn, high, low, close, volume, close = row
    v = conv(volume)
    print(date, v)
