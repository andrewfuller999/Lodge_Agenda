import os
import sys
from pprint import pprint
import inquirer

sys.path.append(os.path.realpath('.'))

questions = [
    inquirer.Checkbox('interests',
                      message="What are you interested in?",
                      choices=['October', 'Books', 'Science', 'Nature', 'Fantasy', 'History'],
                      default=['October']),
]

answers = inquirer.prompt(questions)

pprint(answers)
