#!/usr/bin/env python3


import prompt


def welcome_user():
    return prompt.string('May I have your name? ')


def main():
    welcome_user()


if __name__ == '__main__':
    main()
