from array import *

vals = array("i", [1,2,3,4,5])

print(vals.buffer_info())
print(vals.typecode)
vals.reverse()
print(vals)
print(vals[0])

for i in range(len(vals)):
    print(vals[i])


for e in vals:
    print(e)