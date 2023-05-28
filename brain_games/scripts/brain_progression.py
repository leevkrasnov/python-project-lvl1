#!/usr/bin/env python3

import brain_games.even
import brain_games.cli


def main():
    print('Welcome to the Brain Games!')
    name = brain_games.cli.welcome_user()
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    three_correct_answer = True

    for i in range(3):
        progression = brain_games.even.get_progression()
        print(f'Question: {progression[1]}')
        correct = str(progression[0])
        answ = brain_games.even.answer()
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
