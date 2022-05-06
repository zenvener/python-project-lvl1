#!/usr/bin/env python3
from random import randint


game_set = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_number_prime(a):
    if a < 2:
        return False
    i = 2
    while i <= a ** (1 / 2):
        if a % i == 0:
            return False
        i += 1
    return True


def get_question_and_decision():
    question = randint(1, 1000)
    correct_answer = 'yes' if is_number_prime(question) else 'no'

    return (question, correct_answer)
