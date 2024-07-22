from datetime import datetime

def formatDate(date:datetime):
    return date.strftime('%A %d %B %Y')

given_date = datetime(2020, 2, 25)

print(formatDate(given_date))