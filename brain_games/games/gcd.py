import random
import prompt


def start_gcd():
    def low(n1, n2):
        return n1 if n1 <= n2 else n2
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        r_ans = 0
        num1, num2 = random.randint(1, 100), random.randint(1, 100)
        print(f"Question: {num1} {num2}")
        ans = int(input("Your answer: "))
        for i in range(1, low(num1, num2) + 1):
            if num1 % i == 0 and num2 % i == 0:
                r_ans = i
        if r_ans == ans:
            print("Correct!")
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{r_ans}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
