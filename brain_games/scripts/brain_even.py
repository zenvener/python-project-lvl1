#!/usr/bin/env python3
import prompt
import random


def main():
    def corr(x):
        return "yes" if x % 2 == 0 else "no"
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        r = random.randint(1, 100)
        print(f"Question: {r}")
        ans = input("Your answer: ")
        if (r % 2 == 0 and ans.lower() == "yes"):
            print("Correct!")
        elif (r % 2 == 1 and ans.lower() == "no"):
            print("Correct!")
        else:
            print(f"'{ans}' is wrong answer ;(.", end="")
            print(f"Correct answer was '{corr(r)}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()