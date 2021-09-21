print("----------- Modules -----------")
# try:
#     num = int(input("Enter a positive integer: "))
#     if num <= 0:
#         # we can pass the message in the raise statement
#         raise ValueError("That is  a negative number!")
# except ValueError as e:
#     print(e)


import mymodule
import platform as plt
from my_new_module import person1, arith_func, multi_try, try_else_func

mymodule.greeting("Python")

a = mymodule.person1["age"]
print(a)

print(person1["age"])
arith_func()
multi_try()
try_else_func()

x = plt.system()
print(x)

y = dir(plt)
# print(y)


print("------------- Include another folder module -------------")
import sys
sys.path.append('E:\\python-training\\python-module')
print(sys.path)


import new_mod

a = new_mod.person1["name"]
print(a)

val = [2, 3, 1, 8]
new_mod.func_mod(val)
new_mod.rand_func()
new_mod.m1()


print("------------- Math Function -------------")
from math import sqrt, pi

print(sqrt(25))
print(pi)


print("------------- Keyword Function -------------")
import keyword as k

print(dir(k))
print(k.kwlist)

