def foo(arg1, arg2, **kwargs):
    print(f'arg1: {arg1}, arg2: {arg2}, kwargs: {kwargs}')


if __name__ == '__main__':
    foo(1, 2, a=3, b=4, c=5)
    args = {"arg2":2, "a":3, "b":4, "c":5}
    foo(arg1=1, **args)
    arg_set1 = {"arg2":2}
    arg_set2 = {"a":3, "b":4, "c":5}
    foo(arg1=1, **arg_set1, **arg_set2)
    foo(**arg_set1, **arg_set2, arg1=1)
    arg_set3 = {"a":3, "arg2":2}
    arg_set4 = {"b":4, "c":5}
    foo(**arg_set3, **arg_set4, arg1=1)