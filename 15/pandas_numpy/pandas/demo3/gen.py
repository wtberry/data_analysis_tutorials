# generate some files that 
# 3x files
# they have four columns:
# date, email, tweet, ig
# 7-10
# each line...
# just one value...
# 
# 
# 
# one file
# date jleague lat long
# 


# make three files
# for loop to cycle through each file


from random import randint, choice



filenames = ['msging_{}.txt'.format(num) for num in range(1, 4)]
for file in filenames:
    with open(file, 'w') as fout:
        for i in range(7):
            date = '2016-03-' + str(randint(1, 16))
            emails = (str(randint(11, 20)), '0', '0')
            tweets = ('0', str(randint(2, 10)), '0')
            igs = ('0', '0', str(randint(1, 3)))
        
            count = choice([emails, tweets, igs])
            output = date + ',' + ','.join(count) + '\n'
            fout.write(output)
        
        
        