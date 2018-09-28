from calendar import month_name, day_name
from collections import namedtuple
from datetime import datetime, timedelta
import math


def ordinal(n):
    # Returns 1st, 2nd, 3rd for any number n (1, 2, 3 etc)
    return "%d%s" % (n, "tsnrhtdd"[(math.floor(n / 10) % 10 != 1) * (n % 10 < 4) * n % 10::4])


def nth_weekday(the_date, nth_week, week_day):
    temp = the_date.replace(day=1)
    adj = (week_day - temp.weekday()) % 7
    temp += timedelta(days=adj)
    temp += timedelta(weeks=nth_week - 1)
    return temp


Meeting = namedtuple('Meeting', 'month week day special')

meetings = [
    Meeting(month=2, week=3, day=4, special=None),
    Meeting(month=3, week=3, day=4, special=None),
    Meeting(month=5, week=3, day=4, special=None),
    Meeting(month=6, week=3, day=4, special=None),
    Meeting(month=9, week=2, day=4, special='Past Masters'),
    Meeting(month=10, week=3, day=4, special='Installation'),
    Meeting(month=12, week=3, day=4, special='Christmas'),
]

meetings.sort(key=lambda x: x.month)

for meeting in meetings:
    print(meeting)

for year in range(2018, 2028):
    print()
    meeting_str = 'Meetings for {}'.format(year)
    print(meeting_str)
    print('='*len(meeting_str))
    for meeting in meetings:

        meeting_date = nth_weekday(datetime(year=year, month=meeting.month, day=1), nth_week=meeting.week,
                                   week_day=meeting.day)

        meeting_str = 'Our {} meeting '.format(month_name[meeting_date.month])

        if meeting.special:
            meeting_str += 'is our {} meeting and '.format(meeting.special)

        meeting_str += 'is on {} {} {} {}.'.format(day_name[meeting.day], ordinal(meeting_date.day),
                                                   month_name[meeting_date.month], meeting_date.year)
        print(meeting_str)

        offset = (meeting_date.weekday() - 1) % 7
        rehearsal_date = meeting_date - timedelta(days=offset+7)
        rehearsal_str = 'The rehearsal is on {} {} {} {}.'.format(day_name[rehearsal_date.weekday()], ordinal(rehearsal_date.day),
                                                   month_name[rehearsal_date.month], rehearsal_date.year)

        print(rehearsal_str)

