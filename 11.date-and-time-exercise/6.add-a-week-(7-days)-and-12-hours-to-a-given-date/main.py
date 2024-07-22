from datetime import datetime,timedelta

def addWeekAnd12Hours(date:datetime):
    return date+timedelta(days=7,hours=12)

# 2020-03-22 10:00:00
given_date = datetime(2020, 3, 22, 10, 0, 0)

print(addWeekAnd12Hours(given_date))