import pandas as pd
from pandas import DataFrame, Series

left = pd.read_csv('left_file.csv')
right = pd.read_csv('right_file.csv')
print(left)
print(right)

m = pd.merge(left, right, on=['name'])
m['matchip'] = m.fmip == m.toip

print(m[m.matchip == True])

m.payload
bins = list(range(0, 1000001, 100000))
labels = ['one hundred thousand','two hundred thousand','three hundred thousand','four hundred thousand','five hundred thousand','six hundred thousand','seven hundred thousand','eight hundred thousand','nine hundred thousand', 'one million']
m['bins'] = pd.cut(m.payload, bins, labels = labels)
print(m)
print(len(bins))
print(len(labels))

p = m.pivot(index = 'lat', columns='long', values = 'bins')
print('p\n', p)
