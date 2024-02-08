from functools import partial

def add(x, y):
    return x + y

add_10 = partial(add, 10)

# always add 10 to a number and use partial to pre-set the value for a python function
print(add_10(5))  # 15