from random import randint

GAME_MAIN_QUESTION = 'What number is missing in the progression?'


def get_question_and_answer():
    START_NUMBER = randint(0, 900)
    RANGE_LENGTH = randint(5, 10)
    STEP_RANGE = randint(1, 5)
    RANDOM_INDEX = randint(1, RANGE_LENGTH - 1)

    progression = list(range(
        START_NUMBER, START_NUMBER + RANGE_LENGTH * STEP_RANGE, STEP_RANGE))
    progression = [str(i) for i in progression]

    correct_answer = progression[RANDOM_INDEX]

    progression[RANDOM_INDEX] = '..'

    question = " ".join(progression)

    return (question, correct_answer)
