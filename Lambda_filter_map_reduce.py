#  lambdas : i we have to create one liners without using def

square = lambda x : x*x
cube = lambda y : y*y*y
power = lambda x,y : x**y
even = lambda x : not x & 1

print(even(2))


# map : apply function to each element  : (similar to for_each function in cpp)

num_list = [1,2,3,4]
print(list(map(square , num_list)))
print(list(map(cube , num_list)))
print(list(map(lambda x : x**2 , num_list)))


# filter : keeping elements that only satify conditions

num_list2 = list(range(1,10))
print(list(filter(lambda x : x & 1 , num_list2)))


# reduce is used to accumulate values
from functools import reduce
num_list3 = list(range(10,15))
print(f"product of num_list3 : {reduce(lambda x,y : x*y , num_list3)}")
print(f"Sum of num_list3 : {reduce(lambda x,y : x+y , num_list3)}")
