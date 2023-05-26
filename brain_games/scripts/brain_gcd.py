#!/usr/bin/env python3

import brain_games.even
import brain_games.cli


def main():
    print('Welcome to the Brain Games!')
    name = brain_games.cli.welcome_user()
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    three_correct_answer = True

    for i in range(3):
        num_1 = brain_games.even.get_random_number()
        num_2 = brain_games.even.get_random_number()
        print(f'Question: {num_1} {num_2}')
        correct = str(brain_games.even.get_find_gcd(num_1, num_2))
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
