# <demo> silent
# Title: pd_demo_5.py
# Usage: From an IPython prompt:
#        %run demobatch.py pandas_demo5.py
# Description: Demonstrating Data Aggregation techniques using pandas - borrowing
#     extensively from the book Python for Data Analysis by Wes McKinney
# Date: 20160503
# Revision: 0.5
# Python Version: 3.x
# IPython Version: 2.x
# Author: Chalmer Lowe

# TODO: N/A
# ============================================================================

# <demo> stop
# Agenda
# * Grouping data


# <demo> stop
# Let's start by importing the pertinent libraries and functions

import pandas as pd
from pandas import DataFrame         #, Series
import numpy as np

# Let's start by defining a DataFrame that includes some sample data showing the 
# messages (emails & tweets) received by diana and clark on each of two days

df = DataFrame({'name': ['diana', 'diana', 'clark', 'clark', 'diana'],
                'msgs': ['email', 'tweet', 'email', 'tweet', 'email'],
                'day1': [10, 11, 23, 23, 15],
                'day2': [14, 15, 16, 17, 21]})

df

# <demo> stop
# One means of data aggregation is to group some or all of your data according 
# to certain values in the data.
# In this example, let's group by the name of the person who received 
# the messages and display how many emails or tweets they received ON day 1.
# to do this, we 

grouped = df['day1'].groupby(df['name'])

# A SeriesGroupBy object is simply an object that holds enough information to
# breakup the dataframe content into groups. Once you have a GroupBy object, you can
# then perform calculations/transformations/etc to each of the groups.
# for now, let's just look at what is in each group:
# Notice that only data from 'day1' is included and it is broken up by avenger
# superhero

for items in grouped:
    for item in items:
        print(item)

# <demo> stop
# Once the dataframe is broken up into groups, you can perform calculations,
# such as calculate the mean (average) number of emails or tweets.
# There are a number of such calculations already associated with GroupBy
# objects, such as .mean()

grouped.mean()


# <demo> stop
# if we want to group the object via a hierarchical grouping, we can do that too

means = df['day1',].groupby([df['name'], df['msgs']]).mean()
means


# <demo> stop
# if we decide we want this displayed in a way that might be a bit
# more intuitive to view, we can try:

means.unstack()


# <demo> stop
# Realize that the indices used to group data do not have to be integral to
# the dataframe. You can use any array, series or column that is the same length as your data to group things. Here we put together two numpy arrays
# with 'keys' in them. The first array might represent cities where crime
# occurred. The second array might be the day of the week that emails/tweets
# occurred. As long as the arrays are the same length as your target column,
# you can group using the external keys.

cities = np.array(['ney york', 'baltimore', 'baltimore', 'ney york', 'ney york'])
day = np.array(['mon', 'mon', 'tues', 'mon', 'tues'])

# Here we group the day1 column according to our new/external keys and take the
# mean of each group.

df['day1'].groupby([cities, day]).mean()

# <demo> stop
# if the grouping data is found in the same DataFrame that you are
# working with, you can go ahead and pass column names as the key(s)
df.groupby('name').mean()

# OR
# df.groupby(['name', 'msgs']).mean()



# <demo> stop
# Another very useful GroupBy method allows you to count the number of values
# in a grouped object's groups. This accurately reflects the reality that clark
# had two messages and diana has three.

df.groupby('name').size()

# <demo> stop
# Here we have the same function, but using two keys to create a hierarchical
# index. This time, we see that it accurately reflects the number of
# emails and tweets for each superhero:

df.groupby(['name', 'msgs']).size()


# <demo> stop
# iterating over GroupBy objects parses each object as a series of tuples,
# where each tuple contains the name of the group and the content of that group.
# in this for loop, we can use tuple-unpacking to breakout each part: the name
# and the group-content object

for name, group in df.groupby('msgs'):
    print(name)
    print(group)


# <demo> stop
# Here, since the index is hierarchical (i.e. has more than one key) the 'name'
# is actually broken out into a separate tuple with multiple parts for each
# level of the hierarchical index.

for (k1, k2), group in df.groupby(['name', 'msgs']):
    print(k1, k2)
    print(group)


# <demo> stop
# Especially witha  large dataset, it may not be desirable to group across the
# entire dataset. Thus column-specific grouping may be useful. Here we display
# just the day1 column.

df.groupby(['name', 'msgs'])['day1'].mean()

# The following line does the same thing, but displays multiple columns.
# df.groupby(['key1', 'key2'])[['day1', 'day2']].mean()


# <demo> stop
# There are a number of other ways to implement grouping. One way is using
# dictionaries to map columns (or rows) to values. In this case, we tie each
# of the years to a grouping (pre vs post apocalyptic event and a third
# category for future events).


heroes = DataFrame([[512, 613, 714, 815, 916],
                    [413, 412, 411, 420, 415],
                    [501, 525, 535, 545, 555],
                    [501, 602, 545, 600, 599],
                    [413, 603, 412, 599, 419]],
                    columns=[2011, 2012, 2013, 2014, 2015],
                    index=['clark', 'bruce', 'diana', 'kara', 'selina'])

mapping = {2011: 'pre',
           2012: 'pre',
           2013: 'post',
           2014: 'post',
           2015: 'post',
           2016: 'future'}  


# <demo> stop
# So rather than grouping by a column, we simply drop in the dictionary:
# in this case, we explicitly identify the grouping axis to be the columns
# by using an axis=1 argument (the default is axis=0 for grouping by rows.)

by_column = heroes.groupby(mapping, axis=1)
by_column.sum()


# <demo> stop
# NOTE: pre/post are lexigraphically sortable, and leads to all the 'post'
# years being displayed infront of the 'pre' years, which seems weird, so
# we tell the function to skip the alphabetical sorting process, which
# leaves the 'pre' group (years 2011, 2012) in front of the 'post' group (years
# 2013, 2014, 2015).

by_column = heroes.groupby(mapping, axis=1, sort=False)
by_column.sum()
# by_dolumn.mean()
# by_column.describe()


# <demo> stop
# You can GroupBy the outputs of functions. it does not matter where the
# function comes from, as long as it provides an output. For example, this
# sample functions counts the number of vowels that show up in a superhero's
# name.

def count_vowels(name):
    count = 0
    for letter in name:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count

# The following will group the heroes based on the number of vowels in their
# name (1, 2 or 3) and then will calculate the means of their emails by group.

heroes.groupby(count_vowels).mean()

# <demo> stop
# What other aggregations can you do on data?
# by_column.mean()
# by_column.sum()
# by_column.min()
# by_column.max()
# by_column.median()
# by_column.first()
# by_column.last()
by_column.describe()

# by_column.<tab>        # pressing the <tab> key in ipython after typing
                         # "by_column.' will display all the methods/attributes


# <demo> stop
# it is possible to apply any aggregation funtion to your data. for example
# if we want to know how far off from the max, any given mean is, we can
# calculate that:

def max_mean_diff(arr):
    return arr.max() - arr.mean()

grouped.agg(max_mean_diff)

# <demo> stop
# for the next bit, let's look at a slightly more sophisticated dataset
# this is data that I generated randomly.
# we start by reading in the data
# then we perform a calculation to determine the relative pct between
# the student's gpa and change in the gpa

gpas = pd.read_csv('gpa_short.csv')
gpas['gpa pct'] = gpas['gpa change'] / gpas['gps']

# from there, we group by the gender and the athlete (or not) statues.

grouped = gpas.groupby(['gender', 'athlete'])

# then we pull out just the gpa_pct column in reference to the groupings

grouped_pct = grouped['gpa_pct']

# <demo> stop
# at this point we can apply some functions to this data. Notice the
# use/non-use of quotes. for built-in functions, you need to use the
# quotations. For funtions that you have defined in the current namespace
# you can get away with not using the quotes:

grouped_pct.agg(['max', 'mean', max_mean_diff])

# <demo> stop
# there are multiple ways to slice the data into columns that you want and
# then aggregate the data in those columns. here is another method, where
# we choose several columns and then apply four functions against each 
# of the columns:

funtions = ['median', 'min', 'max', 'count']
result = grouped['gpa_pct', 'gpa'].agg(functions)

# <demo> stop
# if we want to focus on just a single grouping at a time, we can select
# for that grouping via dictionary-like indexing.

result['gpa_pct']


# <demo> stop
# There is a way to map certain functions to only certain columns by using a dictionary to perform the mapping:

mapping = {'gpa_change': 'min', 'duration': 'mean'}
grouped.agg(mapping)

# <demo> stop
# This can get pretty sophisticated:

mapping2 = {'gpa_change': ['min', 'max', 'median'], 'duration': 'mean'}
grouped.agg(mapping2)

# <demo> stop
# sometimes, we want to perform aggregation, but we want to retain the
# overall shape of the data, much like we did using the as_index=False argument
# this is where the transform method comes in. Let's look at two attempts
# to examine the mean for our heroes DataFrame

k = ['cat_a', 'cat_b', 'cat_a', 'cat_b', 'cat_a']

# Method 1

heroes.groupby(k).mean()

# Method 2

# heroes.groupby(k).transform('mean')

# NOTE: as before, any function that can be applied to the group can be fed
# into the transform function, for example:
# heroes.groupby(k).transform(max_mean_diff)

# <demo> stop
# there is another fundamental way to apply functions to the data in a Pandas
# object: using apply()
# let's say we want to find the best performers in terms of grade changes across
# each group

def best(df, n=10, column='gpa_pct'):
    return df.sort_index(by=column)[-n:]

# if we simply apply this to the gpas DataFrame, as a whole, we will see the
# most improved students and their characteristics, here we use n=7 to get the
# top seven.

best(gpas, n=7)

# <demo> stop
# if we use a GroupBy and then apply the function to the GroupBy object

gpas.groupby('athlete').apply(best)
# gpas.groupby('athlete').apply(best, n=2, column='gpa_change')

# <demo> stop
#
gpas.groupby(['athlete', 'gender']).apply(best, n=3)[['duration',
                                                      'gpa_pct',
                                                      'gpa_change']]

# <demo> stop
#

dfc = gpas[['gpa', 'gpa_change', 'gpa_pct']]
gpabins = pd.cut(dfc.gpa_change, 10)
gpabins

# <demo> stop
#

def stat_summary(grp):
    return {'min': grp.min(),
            'max': grp.max(),
            'median': grp.median(),
            'std': grp.std()}

grouped = dfc.gpa_pct.groupby(gpabins)
grouped.apply(stat_summary)
# grouped.apply(stat_summary).unstack()

# <demo> stop
#


# <demo> stop
#


# <demo> stop
#




# heroes2 = DataFrame([[1, 2, 3, 4, 5],
#                     [2, 4, 6, 8, 10],
#                     [1, 25, 50, 75, 100],
#                     [1, 2, 3, 4, 100],
#                     [100, 90, 80, 70, 60]], columns=[2011, 2012, 2013, 2014, 2015],
#                     index=['clark', 'tony', 'diana', 'thor', 'jessica'])
# 
# mapping = {2011: 'pre',
#            2012: 'pre',
#            2013: 'post',
#            2014: 'post',
#            2015: 'post',
#            2016: 'future'}
# 
# by_column2 = heroes.groupby(mapping, axis=1, sort=False)