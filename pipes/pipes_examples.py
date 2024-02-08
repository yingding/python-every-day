from functools import partial


def add(x, y):
    return x + y


add_3 = partial(add, y=3)


if __name__ == '__main__':
    # the precedence operator "|" only works for langchain objects, not for regular functions
    # "|" is the merge operator for dictionaries object above python 3.9 
    value = 3
    # not working in python at all
    # value | add_3 | print