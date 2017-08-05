import csv

def fun1(high, low):
    h = float(high)
    l = float(low)
    if h > l:
        return h-l
    elif l > h:
        return l-h

fin = open('folder/yahoo_prices_short.csv')
fin.readline()
stocks = csv.reader(fin)

for row in stocks:
    date, opn, high, low, close, volume, adj_close = row
    delta = fun1(high, low)
    print(date, delta)
