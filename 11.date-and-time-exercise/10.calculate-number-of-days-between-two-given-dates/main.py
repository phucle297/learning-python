from datetime import datetime
def daysBetweenTwoDates(date1:datetime, date2:datetime):
    return (date1-date2).days if date1>date2 else (date2-date1).days

date_1 = datetime(2020, 2, 25)
date_2 = datetime(2020, 9, 17)

print(daysBetweenTwoDates(date_1,date_2))