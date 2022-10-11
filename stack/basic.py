from inspect import stack
from sys import maxsize

def create_stack() -> list:
    stack = []
    return stack

def is_empty(stack : list) -> bool:
    return len(stack) == 0

def push(stack: list, value: object):
    stack.append()

def pop(stack: list):
    if stack.is_empty(stack):
        return
    stack.pop()
