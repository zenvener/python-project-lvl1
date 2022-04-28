import random
import prompt


def start_progression():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('What number is missing in the progression?')
    for i in range(3):
        a, d = random.randint(1, 100), random.randint(1, 10)
        p = [int(i) for i in range(a, a + d * 9 + 1, d)]
        r_ans = random.choice(p)
        r_index = p.index(r_ans)
        p[r_index] = ".."
        print("Question: ", end="")
        print(*p)
        ans = int(input("Your answer: "))
        if r_ans == ans:
            print("Correct!")
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{r_ans}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")