#!/usr/bin/env python3
from sys import argv
import json
import random

STANDARD_COLOUR = '\033[95m'
QUESTION_COLOUR = '\033[96m'
CORRECT_COLOUR = '\033[92m'
INCORRECT_COLOUR = '\033[91m'


def main(file_name):
    """
    Quiz yourself on your quiz.json
    """
    with open(file_name) as f:
        quiz = json.load(f)
    topics = ', '.join(quiz.keys())

    while True:
        topic = input(f'{STANDARD_COLOUR}What topic would you like to be quizzed on? The options are {topics}. '
                      f'Type "exit" to finish.\n\n')
        if topic.lower() == "exit":
            exit(0)
        while topic not in quiz.keys():
            topic = input(f'{INCORRECT_COLOUR}Topic not valid. What topic would you like to be quizzed on? '
                          f'The options are {topics}. Type "exit" to finish.\n\n')
            if topic.lower() == "exit":
                exit(0)
        questions = list(quiz[topic].items())
        random.shuffle(questions)
        correct = 0
        total = 0
        for question, answer in questions:
            attempt = input(f'{QUESTION_COLOUR}{question}\n\n')
            if attempt.lower() == answer.lower():
                print(f'\n{CORRECT_COLOUR}Correct!\n')
                correct += 1
            else:
                print(f'\n{INCORRECT_COLOUR}Incorrect, the correct answer was {answer}\n')
            total += 1
        print(f'{STANDARD_COLOUR}Your result {correct}/{total}\n')


if __name__ == '__main__':
    """
    Quiz yourself on a set of questions and answers.
    Within a <name>.json file, create a structure like:
    {
        "Topic 1": {
            "Question 1": "Answer 1",
            "Question 2": "Answer 2"
        },
        "Topic 2" : {
            ...
    }
    
    Then run ./quiz.py <name>.json and quiz yourself!
    """
    try:
        main(argv[1])
    except IndexError:
        print("A json file is required as an argument")
