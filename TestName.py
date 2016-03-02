import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    retz = r'^UTC([\+-]\d{1,2})\:(00)$'
    tz2 = re.match(retz, tz_str)
    tz = int(tz2.group(1))
    cday = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    tz = timezone(timedelta(hours=tz))
    dt = cday.replace(tzinfo=tz)
    return dt.timestamp()

    pass

#test
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('pass')
