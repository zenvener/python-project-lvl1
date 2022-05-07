#!/usr/bin/env python3
from random import randint


game_set = "What number is missing in the progression?"
START_NUMBER = 1
OVERALL_NUMBERS = 100
MIN_HID_NUMBER = 1
MAX_HID_NUMBER = 9
MIN_NUM_PROGRESSION = 1
MAX_NUM_PROGRESSION = 10



def constr_progression(core_element, step):
    member, progression = core_element, [core_element]
    for i in range(10):
        member += step
        progression.append(member)
    return progression


def get_sentence_out_of_progression(progression, hid_number):
    progression_string = []
    for index in range(0, 10):
        progression_string.append(str(progression[index]))
    progression_string[hid_number] = '..'
    return " ".join(progression_string)


def get_play_overall():
    first_element = randint(START_NUMBER, OVERALL_NUMBERS)
    step = randint(MIN_NUM_PROGRESSION, MAX_NUM_PROGRESSION)
    hidden_number = randint(MIN_HID_NUMBER, MAX_HID_NUMBER)
    progression = construct_progression(first_element, step)
    return (get_sentence_out_of_progression(progression, hidden_number),
            str(progression[hidden_number]))
