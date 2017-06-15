import csv

with open('AMEX_daily_prices_N.csv', encoding='utf-8-sig') as fin:
    reader = csv.reader(fin)

    data = {}

    header = ''
    for line in reader:
        if not header:
            header = line
            continue
        exchange, stock_sym, date, _open, high, low, close, volume, adj = line
        data[stock_sym] = data.get(stock_sym, []) + [_open]

print(data)
