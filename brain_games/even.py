import operator
import random
import prompt


def random_number(min=0, max=100):
    return random.randint(min, max)


def random_symbol():
    symbol = '-', '+', '*'
    return random.choice(symbol)


operands = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def calculator(operand=random_symbol(), num1=1, num2=1):
    return operands[operand](num1, num2)


def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def answer():
    return prompt.string('Your answer: ')
