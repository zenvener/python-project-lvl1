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


def get_question_and_answer():
    START_NUM = 1
    END_NUM = 20
    NUMBER_1 = randint(START_NUM, END_NUM)
    NUMBER_2 = randint(START_NUM, END_NUM)

    question = f'{NUMBER_1} {NUMBER_2}'

    correct_answer = str(find_gcd(NUMBER_1, NUMBER_2))
    return(question, correct_answer)
