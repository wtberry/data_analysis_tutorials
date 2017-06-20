import os
files = ['first.db', 'test2.db', 'data.db', 'customers.db']

for file in files:
    try:
        os.remove(file)
        print('REMOVED:', file)
    except FileNotFoundError:
        print('Could not find:', file)