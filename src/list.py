import os
import sys
import inquirer
from datetime import datetime, timedelta

from pprint import pprint

sys.path.append(os.path.realpath('.'))


def nth_weekday(the_date, nth_week, week_day):
    temp = the_date.replace(day=1)
    adj = (week_day - temp.weekday()) % 7
    temp += timedelta(days=adj)
    temp += timedelta(weeks=nth_week - 1)
    return temp


now = datetime.now()
oct_meeting = nth_weekday(datetime(day=1, month=2, year=2019), 3, 4)

meetings = ['October (Install)', 'December', 'February', 'March', 'May', 'June', 'September (Past Masters)']

questions = [
    inquirer.List('meeting',
                  message="Which meeting do you want to create an agenda for?",
                  choices=meetings,
                  ),
]

answers = inquirer.prompt(questions)

pprint(now)
print(oct_meeting)
pprint(answers)
