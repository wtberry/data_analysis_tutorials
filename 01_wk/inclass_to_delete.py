# ../datasets/server_location.txt
# 218.69.80.64
# Wilmington

fin = open('../datasets/server_location.txt')
fout = open('../datasets/server_location.csv', 'w')


for line in fin:
    csv_line = line.replace(',', '|')
    fout.write(csv_line)

fout.close()
