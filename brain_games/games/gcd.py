#!/usr/bin/env python3
from random import randint

game_set = "Find the greatest common divisor of given numbers."

def find_gcd(q, w):
    if q < w:
        q, w = w, q
    div_remainder = q % w
    while div_remainder != 0:
        q = w
        w = div_remainder
        div_remainder = q % w
    return w
def get_question_and_decision():
    start_num = 1
    end_num = 20
    number_1 = randint(start_num, end_num)
    number_2 = randint(start_num, end_num)

    question = f'{number_1} {number_2}'

    correct_answer = str(find_gcd(number_1, number_2))
    return(question, correct_answer)
