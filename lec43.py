# Date and time module
# Module name - datetime
# the date contains year , month , day , hour , minute , second and microsecond

import datetime
x=datetime.datetime.now()
print(x)

y=datetime.datetime(2021,11,18)
print(y)

# strftime() - takes one parameter , format , to specify the format of the returned string
# %b - Month name , short version         : Dec
# %B - Month name , full version          : December
# %m - Month as a number 01-12            : 12
# %y - Year,short version,without century : 18
# %Y - Year , full version                : 2018
# %H - Hour , 00-23                       : 17
# %I - Hour , 00-12                       : 05
# %p - AM/PM                              : PM
# %M - Minute , 00-59                     : 41

import datetime
now=datetime.datetime.now()    # current date and time
year=now.strftime("%Y")
print("year :" , year)
print("date and time :" , now)


