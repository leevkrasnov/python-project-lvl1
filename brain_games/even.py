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
