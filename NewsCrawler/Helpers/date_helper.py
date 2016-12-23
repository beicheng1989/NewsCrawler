import datetime

# Datetime Format
# Example: '26-11-2016 12:36 AM'
DATETIME_FORMAT = "%d-%m-%Y %I:%M %p"


def increase_day_by_one(d):
    d += datetime.timedelta(days=1)
    return d


def get_formatted_datetime(d, frmat=DATETIME_FORMAT):
    return strftime(d, frmat)


def dateobject_to_split_date(d, delimiter='-', reverse=False):
    if reverse == True:
        year, month, day = [int(i) for i in d.__str__().split(' ')[
            0].split(delimiter)]
        return (year, month, day)
    else:
        day, month, year = [int(i) for i in d.__str__().split(' ')[
            0].split(delimiter)]
        return (day, month, year)
