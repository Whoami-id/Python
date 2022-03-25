def multi_print(name):
    print(name)


multi_print("Hallo Welt")


def multi_print2(name, count):
    for i in range(0, count):
        print(name)


multi_print2("Hallo", 3)


def maximum(a, b):
    if a < b:
        return b
    else:
        return a


print(maximum(4, 5))

print("----------------------------------")


def position_only_arg(a, /):
    print(a)
position_only_arg(1)



def kwd_only_arg(*,a):
    print(a)
kwd_only_arg(a = 3)


