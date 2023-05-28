import operator
import random
import prompt
import math


def get_random_number(min=0, max=100):
    return random.randint(min, max)


def get_random_symbol():
    symbol = '-', '+', '*'
    return random.choice(symbol)


signs = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def calculator(operand=get_random_symbol(), num1=1, num2=1):
    return signs[operand](num1, num2)


def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def answer():
    return prompt.string('Your answer: ')


def get_find_gcd(num1=1, num2=2):
    return math.gcd(num1, num2)


def genetate_gen(min=5, max=10):
    gen = []
    start_num = get_random_number(1, 10)
    gen.append(start_num)
    step = get_random_number(1, 10)
    for i in range(get_random_number(min, max) - 1):
        start_num += step
        gen.append(start_num)
    return gen


def get_progression():
    progression = genetate_gen()
    hide_num = random.choice(progression)
    progression_str = ''
    for num in progression:
        if hide_num == num:
            progression_str += '.. '
        else:
            progression_str = progression_str + f'{num} '
    return hide_num, progression_str
