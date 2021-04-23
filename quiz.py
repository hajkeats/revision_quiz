#!/usr/bin/env python3
import argparse
import json
import random

STANDARD_COLOUR = '\033[95m'
QUESTION_COLOUR = '\033[96m'
CORRECT_COLOUR = '\033[92m'
INCORRECT_COLOUR = '\033[91m'


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("json", help="The json quiz file")
    parser.add_argument("--multiple_choice", action="store_true", help="Start a multiple choice quiz")
    return parser.parse_args()


def main(file_name, multiple_choice=False):
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
        while topic.lower() not in [key.lower() for key in quiz.keys()]:
            topic = input(f'{INCORRECT_COLOUR}Topic not valid. What topic would you like to be quizzed on? '
                          f'The options are {topics}. Type "exit" to finish.\n\n')
            if topic.lower() == "exit":
                exit(0)

        questions = []
        for t in quiz.keys():
            if t.lower() == topic.lower():
                questions = list(quiz[t].items())

        random.shuffle(questions)
        correct = 0
        total = 0

        if multiple_choice:
            for question, answer in questions:
                answer_pool = [a for q, a in questions if a != answer]
                choices = random.sample(answer_pool, 3)
                choices.append(answer)
                random.shuffle(choices)
                letters = ["A", "B", "C", "D"]
                print(f'{QUESTION_COLOUR}{question}\n\n')
                attempt = ""
                correct_letter = "?"
                for i in range(4):
                    if choices[i] == answer:
                        correct_letter = letters[i]
                    if i == 3:
                        attempt = input(f'{QUESTION_COLOUR}{letters[i]}: {choices[i]}\n\n')
                    else:
                        print(f'{QUESTION_COLOUR}{letters[i]}: {choices[i]}\n')

                if attempt.lower() == "exit":
                    print(f'{STANDARD_COLOUR}Your result {correct}/{total}\n')
                    break

                if attempt.lower() == correct_letter.lower():
                    print(f'\n{CORRECT_COLOUR}Correct!\n')
                    correct += 1
                else:
                    print(f'\n{INCORRECT_COLOUR}Incorrect, the correct answer was {correct_letter}\n')
                total += 1
                print(f'{STANDARD_COLOUR}Your result {correct}/{total}\n')
        else:
            for question, answer in questions:
                attempt = input(f'{QUESTION_COLOUR}{question}\n\n')
                if attempt.lower() == "exit":
                    print(f'{STANDARD_COLOUR}Your result {correct}/{total}\n')
                    break
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
    
    Then run ./quiz.py <name>.json and quiz yourself
    
    Optional: Use '--multiple_choice' to create a multiple choice quiz
    """
    args = parse_args()
    try:
        main(args.json, args.multiple_choice)
    except IndexError:
        print('A json file is required as an argument')
