from calendar import  isleap, day_name
from datetime import timedelta, date
MeetupDayException = Exception('Day not found')

STARTS = {
    '1st': 1,
    '2nd': 8,
    '3rd': 15,
    '4th': 22,
    '5th': 29,
    'teenth': 13,
}

def meetup_day(year, month, day_of_the_week, which):
    start = date(year, month, STARTS.get(which, last_day_start(year, month)))
    offset = list(day_name).index(day_of_the_week) - start.weekday()
    return start + timedelta(days=offset % 7)


def last_day_start(year, month):
    return([25, 22 + int(isleap(year))] + [25, 24, 25, 24, 25] * 2)[month - 1]