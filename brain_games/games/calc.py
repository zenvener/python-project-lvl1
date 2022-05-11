from random import randint, choice


GAME_MAIN_QUESTION = "What is the result of the expression?"


def get_question_and_answer():
    RANDOM_NUM1 = randint(1, 20)
    RANDOM_NUM2 = randint(1, 20)
    OPERATORS = ('+', '-', '*')
    operator = choice(OPERATORS)
    if operator == '+':
        expression = RANDOM_NUM1 + RANDOM_NUM2
    elif operator == '-':
        expression = RANDOM_NUM1 - RANDOM_NUM2
    elif operator == '*':
        expression = RANDOM_NUM1 * RANDOM_NUM2

    question = f'{RANDOM_NUM1} {operator} {RANDOM_NUM2}'
    correct_answer = str(expression)

    return (question, correct_answer)
