import random
import prompt


def random_number(min=0, max=100):
    return random.randint(min, max)


def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def answer():
    return prompt.string('Your answer: ')
