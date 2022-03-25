from datetime import datetime
from functools import wraps


def log(fn):
    @wraps(fn)
    def logger(*args, **kwargs):
        args_values_types = [(a, type(a)) for a in args]
        kwargs_values_types = [(k, v, type(v)) for k, v in kwargs.items()]
        arguments = args_values_types + kwargs_values_types
        time = datetime.utcnow()
        time = time.strftime("%H:%M:%S")
        fn_result = fn(*args, **kwargs)
        print("Function  {} was called at {} with params {} and returned {}".format(fn.__name__, time, arguments, fn_result))
        return fn_result
    return logger


@log
def divide_integers(a: int , b: int) -> float:
    result = a / b
    return result


def main():
    print(divide_integers(10,2))


if __name__ == "__main__":
    main()