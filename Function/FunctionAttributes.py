def grow_list(val, my_list = None):
    if my_list:
        my_list.append(val)
    else:
        my_list = [val]
    return my_list


my_func = grow_list

print(my_func, type(my_func))


def print_function_output(fn, **kwargs):
    print(fn(kwargs))

print_function_output(my_func, val=10)


print(grow_list.__defaults__)
print(grow_list.__name__)
print(grow_list.__code__.co_argcount)
print(grow_list.__code__.co_varnames)

