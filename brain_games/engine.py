import prompt


def launch(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.GAME_MAIN_QUESTION)
    MAXIMUM_ROUNDS = 3
    for _ in range(MAXIMUM_ROUNDS):
        question, correct_answer = game.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer != correct_answer:
            print(
                f'"{user_answer}" is wrong anwer ;(. Correct answer was'
                f' "{correct_answer}".\nLet\'s try again, {user_name}!'
            )
            break
        else:
            print('Correct!')
    else:
        print(f'Congratulations, {user_name}!')
