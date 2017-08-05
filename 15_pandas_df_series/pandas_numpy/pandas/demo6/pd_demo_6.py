# <demo> silent
# Title: pd_demo_6.py
# Usage: From an IPython prompt:
#        %run demobatch.py pandas_demo5.py
# Description: Demonstrating date and time manipulation - borrowing
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
# * 
# * 
# * 
# * 
# * 
# * 



# <demo> stop
# Let's start by importing the pertinent libraries and functions

import pandas as pd
from pandas import DataFrame, Series
import numpy as np


# <demo> stop
# Let's start by looking at how we create a date object and what that means
# We purposely use the term 'object' when describing this, because we want 
# to distinguish this from a simple string and remind ourselves that this
# object has behaviors and attributes.
# Caveat: the first part of this conversation is not really pandas specific... we
# will focus heavily on the builtin Python Library: datetime.

from datetime import datetime
from datetime import timedelta
date1 = datetime(2016, 5, 3)
date1


# <demo> stop
# datetime.datetime(2016, 5, 3, 0, 0)
# If we do some introspection on the object we have just created, we note that
# it has the year, month, and the day. It also has several other data points 
# represented by zeroes. Let's take peek in the help documentation to find out
# what those mean.
# we can do this using the name of the datetime function and a '?'

datetime?

# thus we learn that the datetime object can also hold data representing:
# hours
# minutes
# seconds
# microseconds
# time zones


# <demo> stop
# From here, let's take a look at the difference between two datetime objects
# Here, we have added an extra data point to each object:
# date 2 includes an hour of 12
# and date 3 includes an hour of 11
# So let's see how big a time difference there is between the two...

date2 = datetime(2016, 5, 3, 12)
date3 = datetime(2016, 5, 3, 11)

difference = date2 - date3
difference


# <demo> stop
# Most of us would probably not have expected this result. We expected one hour and we
# got 3600 of something...
# Let's use the help functionality to explore this potential discrepancy:

timedelta?

# <demo> stop
# Well, that also wasn't what we expected. Let's use IPython's verbose help
# functionality (access it by using the double ??):
# NOTE: as is customary, escape from help's pager program, by pressing the 'q' button:

timedelta??

# <demo> stop
# The verbose help functionality shows us the source code AND in
# this case, we can see the additional details that the author included...
# such as a snarky comment on what we have just witnessed...
#
# Any category of time that does not fit one of these three classifications:
# days, seconds, microseconds
# will be converted to the closest, lower category. The hour got converted to
# 3600 seconds.

# As an object, to gain access to the individual time categories, we can use dot notation
# to access the attributes for the datetime objects and timedelta objects

# Timedelta:

difference.days
# difference.seconds

# Datetime: 

# date3.hour
# date3.day
# date3.month
# date3.year

# Want to see the other attributes and methods?
# date3.<tab>


# <demo> stop
# datetime objects have a:
#   * default string representation
#   * an ISO representation

# default string format:
print(str(date3))

# ISO format:
print(date3.isoformat())


# <demo> stop
# In addition, the datetime module has the ability to both read in and write out using user defined formats.

#   *.strftime()
#   *.strptime()


# <demo> stop
# string formatting:
# To format the str output of a datetime object to suit your needs, you can use
# strftime() and can mix and match from the formatting specifications

datef = datetime(2009, 9, 9)
datef.strftime('%Y-%m-%d')

# We are not gonna go into the full collection of formatting specifications.
# That is left as an exercise for the student
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

# WARNING:
# I have not confirmed this, but I have heard that the supported formatting codes
# vary across platforms (linux, unix, windows, mac, etc) because Python relies upon
# the underlying C library's strftime() function

# Purportedly, the Python Docs reflect all the formatting codes from the
# 1989 version of the C standard which should be consistent across all platforms

# But some libraries may implement additional formatting codes.
# hattip to Will McCutchen's site: http://strftime.org/


# <demo> stop
# string parsing:
# Sometimes we get strings that contain dates but have unusual formatting. You can 
# parse the string manually and convert it to a datetime object:

# Presume that we have the following string that is a month, day and year separated
# by '|' symbols.
datep = '8|8|2008'
datetime.strptime(datep, '%m|%d|%Y')

# In deference to time, we are gonna leave a deep dive into the
# formatting specifications for the student.

# <demo> stop
# While manually setting the formatting works, for heavy duty datetime parsing, the
# automagic parsing available via the dateutil module is hard to beat. 
# NOTE: the ljust provides a field 30 characters wide that
# is left justified. It is simply for clarity in printing...

from dateutil.parser import parse

p1 = parse('2000-01-01')
print(p1, '\t\t', '2000-01-01')

p2 = parse('December 12, 2001 13:13')
print(p2, '\t\t', 'December 12, 2001 13:13')

p3 = parse('23rd January 2002 21:21:21')
print(p3, '\t\t', '23rd January 2002 21:21:21')

# <demo> stop
# As much as it may seem like it, this talk is NOT intended to cover just the datetime 
# or dateutil modules... but we need to cover them to give us perspective 
# on what pandas can do.
# Let's start by reading in a csv. We:
#   * read in the csv
#   * provide a list of column names
#   * identify a column for use as an index
#   * tell pandas to automagically parse the strings into dates

df = pd.read_csv('../../log_file.csv', names=['name', 'email', 'fmip', 'toip',
                                              'datetime', 'lat', 'long', 'payload'],
                                       index_col='datetime',
                                       parse_dates=True)

df

# <demo> stop
# From here, let's assign a label to the data held in the name column 
# to simplify the task of referencing it.

names = df['name']
names

# <demo> stop
# 'names' is a Series and like any Series, it has an index.
# We can provide a label for the index as a separate entity

ts = names.index
ts

# <demo> stop
# Just like any index... we can select for individual entities from the index
# using indexing and slicing.
# Slicing can be done:
#   * against a standalone index object like 'ts'

ts[5]
# ts[2:6]
# ts[0:8:2]

#   * or against a DataFrame OR Series
# names.index[0]


# <demo> stop
# Within pandas, you can index using the integer count (as we saw above)
# OR 
# using a string representation of a specific timestamp

time = '2016-02-06 21:47:02'
names[time]

# <demo> stop
# Matching against a substring from within a longer string is possible as well.
# Here, let's match against any item in the Series with the substring '2016-02-06'
# in the index.

names['2016-02-06']

# <demo> stop
# For our next trick, let's use a new DataFrame and Series from a longer dataset
# (~1000 records).

df_1000 = pd.read_csv('../../log_file_1000.csv', names=['name', 'email', 'fmip',
                                                        'toip', 'datetime', 'lat',
                                                        'long', 'payload'],
                                                 index_col='datetime',
                                                 parse_dates=True)

names_long = df_1000['name']

# <demo> stop
# NOTE: many of the most common interpretations of a 'datetime', even if they are NOT a
# letter-for-letter match of the string will work for selecting dates.
# This first item will bring back 740+ records that have 2015 in the year.

nl = names_long['2015']
nl

# names_long['September 2015']      <--- yields ~ 180 results
# names_long['Oct, 31 2015']        <--- yields ~ 9 result

# <demo> stop
# if the datetime information in the DataFrame/Series is in chronological
# order you can use slice syntax

names_long['Oct, 29 2015':'Oct, 31 2015']         # <--- yields ~ 28 results


# <demo> stop
# Next, we are gonna ingest a dataset, but we will apply a function to truncate
# the datetime string to only represent the date.

# We define a simple function to split the datetime
# strings into dates and times, and retain only the dates. 
# pandas allows us to apply the function when we read in the data using
# the 'converters' argument of the read_csv() function.

def date_split(dt):
    return dt.split('T')[0]

df2_long = pd.read_csv('../../log_file_1000.csv', names=['name', 'email', 'fmip',
                                                 'toip', 'datetime', 'lat',
                                                 'long', 'payload'],
                      index_col='datetime',
                      converters={'datetime':date_split}, parse_dates=True)

df2_long

# <demo> stop
# With the new dataset, we can see many dates that duplicate or repeat, which means that
# we have the capability to group by those dates.

grouped = df2_long.name.groupby(level=0)
grouped.size()

# grouped.first()

# <demo> stop
# Occastionally, our time series doesn't have all the periods that we might want...
# resampling can solve that problem.
# Similarly, sometimes our time series might have too many samples

df_res = df2_long.resample('4h')

# df_res2D = df2_long.resample('2D')

# When resampling, by default, pandas applies the mean. We will also see other ways of
# handling resampling.

# Frequencies are defined as a base frequency and a multiplier...
# 2M - every two months
# 2h30min - every two hours, 30 mins
# D - daily
# B - business daily

# BM - End of the business month

# W-MON - weekly on a given day of the week
# WOM-1TUE - week of the month(1st, 2nd, etc) and day of week
# QS-JAN - start of the quarter


# <demo> stop
# Often, knowing how to handle Time Zones is important ... especially in ensuring 
# accuracy across time zones
# Let's take just the first 750 lines of the column 'name' in the long file.
# At this moment, there is no explicit time zone associated with these
# time stamps. This is referred to as time zone naive

times = df_1000.name[:750]
print(times.index.tz)

# <demo> stop
# To translate from naive to a specific timezone, we use the localize
# function. Common practice it to define the 'local' timezone using the
# standard name.

times_est = times.tz_localize('US/Eastern')

# <demo> stop
# Once you set the local timezone for a TimeSeries, you can convert it to
# match other time zones.

times_hi = times_est.tz_convert('US/Hawaii')

# Combinations between two different timezones will result in an output
# normalized to UTC

# <demo> stop
# Thus far, we have dealt predominantly with potentially irregularly
# timestamped data. One of the other main classes of timing data is periodic
# time spans such as years, months, minutes.

period = pd.Period(2015, freq='W-MON')

# this period represents a single time span across all of 2015.


# <demo> stop
# To see a sequence or range of periods, you can use the period_range function

per_range = pd.period_range('12/12/2010', '12/12/2015', freq='Q')
per_range

# <demo> stop
# To convert to a different frequency, you can use the *.asfreq() function:

period.asfreq('W', how='start')


# <demo> stop
# We can similarly convert whole sequences of periods:

per_range.asfreq('D', how='start')


# <demo> stop
# 

df_period = df_1000.to_period('M')
df_period

# <demo> stop
# To convert back to timestamps...
# The day of month data gets lost in the above conversion, so pandas resorts to
# a default.

df_ts = df_period.to_timestamp(how='start')
df_ts

# <demo> stop
# The resampling process allows you to choose different ways of handling the
# resultant values: as we noted earlier, mean is the default, but we can also
# use other functions...

df_1000[['lat', 'long']].resample('Q', how='max', kind='period')

# how =>>> any of the following:
# mean
# median
# std
# first
# last
# min
# max
# var
# count
# mode


# <demo> stop
# As a wrap-up, let's take a look at plotting some of this data.
# (For more examples of plotting, one of our earlier demo scripts has a variety
# of sample plots. Also, matplotlib has an extensive library of sample plots).

# We'll start with setting up the interactive environment so we can manipulate 
# the graph

import matplotlib.pyplot as plt
plt.interactive(True)

# <demo> stop
# From there, we create a reduced dataset and create a subplot that is two rows
# high, one column wide and we activate the first subplot. Then we set up the
# graph for that subplot to display the latitude in black circles.

df_1000 = df_1000[['lat', 'long']][:750]
plt.subplot(2, 1, 1)
df_1000['lat'].plot(style='ko')


# Next we activate the second subplot and set up the graph for that subplot to
# display the longitude in
plt.subplot(2, 1, 2)
df_1000['long'].plot(style='b^')

# <demo> stop
# Say we want a bar chart and say we want to plot two pieces of information
# on a stacked barchart, showing a primary value topped by a secondary value
# Using a slightly smaller dataset to keep the images cleaner:

df_40 = df_1000[['lat', 'long']][:40]

# resampling the data down to the mean for each day:
ts = df_40.resample('b', how='mean')
p1 = plt.bar(ts.index, ts.lat, 0.2, color='r')
p2 = plt.bar(ts.index, ts.long, 0.2, bottom=ts.lat, color='b')
