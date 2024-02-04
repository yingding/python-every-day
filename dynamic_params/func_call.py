def foo(arg1, arg2, **kwargs):
    print(f'arg1: {arg1}, arg2: {arg2}, kwargs: {kwargs}')


if __name__ == '__main__':
    foo(1, 2, a=3, b=4, c=5)
    args = {"arg2":2, "a":3, "b":4, "c":5}
    foo(arg1=1, **args)