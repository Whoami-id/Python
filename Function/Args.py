def f(a, b, c):
    print(a)
    print(b)
    print(c)

l = [1,2,3]
f(l[0], l[1], l[2])
f(*l)


def calculate_max(*params):
    current_max = params[0]
    for i in params:
        if i > current_max:
            current_max = i
    return current_max

print(calculate_max(1,2,3,4,5,7))
print(calculate_max(*l))






