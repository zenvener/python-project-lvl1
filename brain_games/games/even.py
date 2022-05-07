#!/usr/bin/env python3
from random import randint


game_set = 'Answer "yes" if the number is even, oterwise answer "no".'


def get_question_and_decision():
    question = randint(1, 99)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return (question, correct_answer)
