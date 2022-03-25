


def outer_func(fn):
    def inner_func():
        fn_result = fn()
        return fn_result
    return inner_func


def print_hallo_world():
    print("Hallo world")

dphw = outer_func(print_hallo_world)
dphw()

print("------------------------------------")


def print_args(a, b , c = None):
    print("A: {}, B: {}, C: {}".format(a, b, c))




def decorator(fn):
    print("start decorator function from: ", fn.__name__)
    def wrapper(*args, **kwargs):
        print("start wrapper function from: ", fn.__name__)
        fn_result = fn(*args, **kwargs)
        print("end wrapper function from: ", fn.__name__)
        return fn_result
    print("end decorator function from: ", fn.__name__)
    return wrapper


@decorator
def print_args2(a, b , c = None):
    print("A: {}, B: {}, C: {}".format(a, b, c))


d = decorator(print_args)
d(a = 1, b = 2, c = 3)


print_args2(a = 1, b = 2, c = 3)

