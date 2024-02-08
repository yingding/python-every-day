def wrapper_function(func: callable) -> callable:
    def inner_function(*args, **kwargs):
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result
    return inner_function

"""
This wrapper_function is a decorator that takes the function "add" as an argument
and returns the inner_function back to the same name "add" after adding some print statements.
"""
@wrapper_function
def add(x, y):
    return x + y


if __name__ == '__main__':
    sum = add(x=5, y=10)
    print(f"Sum: {sum!r}")