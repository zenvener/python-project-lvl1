#!/usr/bin/env python3
from random import randint


game_set = 'What number is missing in the progression?'


def get_question_and_decision():
    first_number = randint(0, 900)
    random_index = randint(1, range_length - 1)
    scale_step = randint(1, 5)
    overall_length = randint(5, 10)
    
    

    progression = list(range(
        first_number, first_number + overall_length * scale_step, scale_step))
    progression = [str(i) for i in progression]

    correct_answer = progression[random_index]

    progression[random_index] = '..'

    question = " ".join(progression)

    return (question, correct_answer)
