from random import randint

game_set = "Find the greatest common divisor of given numbers."

def find_gcd(a, b):
    if a < b:
        a, b = b, a
    div_remainder = a % b
    while div_remainder != 0:
        a = b
        b = div_remainder
        div_remainder = a % b
    return b


def get_question_and_solution():
    start_num = 1
    end_num = 20
    number_1 = randint(start_num, end_num)
    number_2 = randint(start_num, end_num)

    question = f'{number_1} {number_2}'

    correct_answer = str(find_gcd(number_1, number_2))
    return(question, correct_answer)
