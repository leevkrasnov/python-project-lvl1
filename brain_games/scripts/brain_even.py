#!/usr/bin/env python3

import brain_games.games.even
import brain_games.cli


def main():
    print('Welcome to the Brain Games!')
    name = brain_games.cli.welcome_user()
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    three_correct_answer = True

    for i in range(3):
        num = brain_games.games.even.random_number()
        print(f'Question: {num}')
        correct = brain_games.games.even.is_even(num)
        answ = brain_games.games.even.answer()
        if correct != answ:
            string = "is wrong answer ;(. Correct answer was"
            print(f"'{answ}' {string} '{correct}'.")
            print(f"Let's try again, {name}!")
            three_correct_answer = False
            break
        else:
            print("Correct!")
    if three_correct_answer:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
