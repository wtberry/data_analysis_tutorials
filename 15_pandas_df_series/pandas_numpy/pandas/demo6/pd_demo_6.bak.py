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
# Most of us would probably not have expected this result.


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


