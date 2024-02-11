import datetime
import time


def population():
    # Date_Time -> Unix Time
    date = []
    date.insert(0,int(input("Year: ")))
    date.insert(1,int(input("Month: ")))
    date.insert(2,int(input("Day: ")))

    date_time = datetime.date(date[0], date[1], date[2])
    unix_time = time.mktime(date_time.timetuple())
    pop = int(input("Number of Swine: "))

    list = [date_time, unix_time, pop]
    return list


def culled():
    date = []
    date.insert(0,int(input("Year: ")))
    date.insert(1,int(input("Month: ")))
    date.insert(2,int(input("Day: ")))

    date_time_cull = datetime.date(date[0], date[1], date[2])
    unix_time_cull = time.mktime(date_time_cull.timetuple())
    unix_time_process = unix_time_cull - (int(input("Processing time (in day/s): ")) * 86400)
    pop = int(input("Number of Swine Culled: "))

    list =[date_time_cull, unix_time_cull, pop, unix_time_process]

    return list

