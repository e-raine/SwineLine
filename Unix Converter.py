# importing datetime module
import datetime
import time

date = []
date.insert(0,int(input("Year:")))
date.insert(1,int(input("Month:")))
date.insert(2,int(input("Day: ")))

date_time = datetime.datetime(date[0], date[1], date[2], 21, 20)

print("date_time =>",date_time)

print("unix_timestamp => ",
	(time.mktime(date_time.timetuple())))


"""
The datetime module has many methods that return many information about the date object.

The mktime is the method of time whish is the inverse function of local time, this method is used to convert datetime to Unix timestamp.

The timetuple() is a method of datetime class that returns the attributes of datetime as a name tuple.

"""