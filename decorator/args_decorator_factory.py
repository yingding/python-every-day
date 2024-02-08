def decorator_factory(arg1: int, arg2: int) -> callable:
    def wrapper_function(func: callable) -> callable:
        def inner_function(*args, **kwargs):
            print(f"Before calling the function with {arg1=}, {arg2=}")  
            result = func(*args, **kwargs, **{"arg1": arg1, "arg2": arg2})
            print("After calling the function")
            return result
        return inner_function
    return wrapper_function


"""
The decorator_factory takes two arguments and returns a decorator.
Inside the returned decorator, the inner_function takes the function "add" as an argument
and returns the inner_function back to the same name "add" after adding some print statements.

The inner_function will have the access to the arguments passed to the decorator_factory
"""
@decorator_factory(arg1=11, arg2=20)
def add(x, arg1=0, arg2=0):
    return x + arg1 + arg2


if __name__ == "__main__":
    sum = add(x=5)
    print(f"Sum: {sum!r}")  # 36
