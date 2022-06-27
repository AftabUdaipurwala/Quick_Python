from datetime import datetime

delta = datetime.now() - datetime(1998, 12, 2)
print(delta.days)

whenever = datetime.strptime('2018-02-02 23:58', '%Y-%m-%d %H:%M')  # here strp means string pass as time
print(whenever)

# to fetch time from date in string
whenever.strftime("%a")  # get day as FRI
whenever.strftime("%c")  # get everything

# Source: http://strftime.org/ get the list of table from here
