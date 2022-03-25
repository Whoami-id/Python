# *args = tuble
# **kwargs = dictionary

def func(**args):
    print(args)


func(key="value", key2="value2")


def g(key, key2):
    print(key)
    print(key2)


d = {"key": "value1", "key2": "value2"}

g(key=d["key"], key2=d["key2"])
g(**d)

print("------------------------------")


def my_function(a, *args, **kwargs):
    print(*args, type(args))
    print(kwargs, type(kwargs))
    print("a: {}, args: {}, kwargs: {}".format(a, args, kwargs))


my_function(1, 3, 4, b=False, c=30, d=40)
