#int objects uses a variable number of bis
import sys
import math


my_value = 42
print("Ineteger Size: ", sys.getsizeof(my_value))
# 0 = 24byte + 0Byte

my_value2 = 0
print("Ineteger Size: ", sys.getsizeof(my_value2))
#42 = 24byte + 4Byte

my_value3 = 2**64
print("Ineteger Size: ", sys.getsizeof(my_value3))




my_flot = 2.7
print(math.floor(my_flot))
print(math.ceil(my_flot))


#Integer bases

my_decimal = int("42", base=10)
print(my_decimal)