import csv 
fin = open('AMEX_daily_prices_N.csv')
fin.readline()
csv_stock = csv.reader(fin)
price_change = {}
for line in csv_stock:
    exchange,stock_symbol,date,stock_price_open,stock_price_high,stock_price_low,stock_price_close,stock_volume,stock_price_adj_close = line
    delta = float(stock_price_close)-float(stock_price_open)
    price_change[stock_symbol] = price_change.get(stock_symbol, 0) + delta
#print(price_change)

for k, v in price_change.items():
    if v < -40:
        print(k, v)
