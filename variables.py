from datetime import datetime
# year = 2020
# month = 9
# day = 2

local_time = datetime.now()
year = local_time.year
month = local_time.month
day = local_time.day
hour = local_time.hour
minute = local_time.minute
second = local_time.second
microsecond = local_time.microsecond
tzinfo = local_time.tzinfo

print(year, month, day, hour, minute, second, microsecond, tzinfo)
