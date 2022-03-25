a = 10
print(id(a))

def func():
     a = 15

     x = globals()["a"]
     print(id(x))
     print(a)
     globals()["a"] = 45



func()

print(a)