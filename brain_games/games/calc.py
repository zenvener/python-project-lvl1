from random import randint, choice


game_set = "What is the result of the expression?"


def get_question_and_solution():
    random_num1 = randint(1, 20)
    random_num2 = randint(1, 20)
    operators = ('+', '-', '*')
    operator = choice(operators)
    if operator == '+':
        expression = random_num1 + random_num2
    elif operator == '-':
        expression = random_num1 - random_num2
    elif operator == '*':
        expression = random_num1 * random_num2

    question = f'{random_num1} {operator} {random_num2}'
    correct_answer = str(expression)

    return (question, correct_answer)
