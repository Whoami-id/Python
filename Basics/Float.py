#float = 8Byte
# sing = 1bit
# exponent = 11bits
# significant = 52bits

import  math

print("{:.32f}".format(42.00000000134))
print(42.00000000134)


my_fraction = 1 /10 + 1/10  + 1/10
print("{:.32f}".format(my_fraction))

my_fraction2 = 0.3
print("{:.32f}".format(my_fraction2))

dif = math.fabs(my_fraction - my_fraction2)
print(dif)
epsilon = 1e-20
print(dif < epsilon)

print(math.isclose(my_fraction, my_fraction2, abs_tol=1e-15, rel_tol=1e-09))



