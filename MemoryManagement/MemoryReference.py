

def print_momory_address(var):
    print(hex(id(var)))


#int, bool, non
my_value = 10
print_momory_address(my_value)

my_int1 = 42
my_int2 = 42
my_int3 = 42

print_momory_address(my_int1)
print_momory_address(my_int2)
print_momory_address(my_int3)


my_float1 = 42.0
my_float2 = 42.0

print_momory_address(my_float1)
print_momory_address(my_float2)


my_list1 = [2,3]
my_list2 = [2,3]
print_momory_address(my_list1)
print_momory_address(my_list2)


