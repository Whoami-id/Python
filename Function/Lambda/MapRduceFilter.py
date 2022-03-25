import functools

# Map function takes: mapping from N values to N values
#   1. a function (callable)
#   2. variable number of iterables

vct1 = [1,3,4]
vct2 = [2,3,5]
result = list(map(lambda x, y: x * y, vct1, vct2))
print(result)



# Reduce function takes: Mapping from N values to a values
#   1. a function (callable)
#   2. variable number of iterables

my_list = [10, -2, 5, 6, 45, 67]
print(functools.reduce(lambda x, y: x if x > y else y, my_list))



my_list2 = [10, -2, 5, 6, 45, 67]
my_list2_filtered = list(filter(lambda x: True if x >= 0 else False, my_list2))
print(my_list2_filtered)