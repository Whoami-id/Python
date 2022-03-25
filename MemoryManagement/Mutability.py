

def print_momory_address(var):
    print(hex(id(var)))



#Imutable types = int, float, boo, str, tuple
#mutabl types = list, dict, set, etc


my_int = 22
print_momory_address(my_int)
my_int = 40
print_momory_address(my_int)


my_list = [1,3,4]
print_momory_address(my_list)
my_list.append(33)
print_momory_address(my_list)


