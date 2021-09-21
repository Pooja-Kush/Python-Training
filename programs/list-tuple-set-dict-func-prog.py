# print("----------------------\n LIST FUNCTIONALITIES\n----------------------")
#
# print("List Comprehension")
# fruits = ['apple', 'mango', 'orange']
# new_list = [x.capitalize() for x in fruits if x != "apple"]
# print(fruits)
# print(new_list)
#
# num_list = [x for x in range(10) if x < 5]
# print(num_list)

# print("----------------------\n TUPLE FUNCTIONALITIES\n----------------------")

# fruits = ('apple', 'mango', 'orange', 10, 30)
# new_list = [x for x in fruits if x != "apple"]
# print(fruits)
# print(new_list)
#
# this_dict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x, y in this_dict.items():
#     print(x, y)

class MyClass:
    x = 5


p1 = MyClass()


# print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(self.name, self.age)

    @staticmethod
    def sum_avg():
        var_tup = eval(input("Enter Tuple of Numbers : "))
        # var_tup = (10, 20, 30, 40, 50)
        var_sum = 0
        for x in var_tup:
            var_sum = var_sum + x

        var_avg = var_sum / len(var_tup)
        print('Average : ', var_avg)

    @staticmethod
    def sets_func():
        """ SETS """
        st = {}
        print(type(st))
        st = set()
        print(type(st))

        st = {'1', '2', '3', '4'}
        print(st)
        st.add('6')
        print(st)


class Student(Person):
    def __init__(self, f_name, l_name, year):
        Person.__init__(self, f_name, l_name)
        print(f_name, l_name, year)

    @staticmethod
    def intersection_func():
        word = input('Enter any word : ')
        set_word = set(word)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        new_word = vowels.intersection(set_word)
        print('Vowels present : ', new_word)

    @staticmethod
    def difference_func():
        set_word = {'a', 'b', 'c', 'd', 'e'}
        print("Set 1 : ", set_word)

        vowels = {'a', 'e', 'i', 'o', 'u'}
        print("Set 2 : ", vowels)

        new_word = set_word.difference(vowels)
        print('Diff letters present : ', new_word)


P1 = Student('XYZ', '20', 2020)
# P1.print_name()
# print(P1.age)
# P1.sum_avg()
# P1.intersection_func()
# P1.difference_func()
# P1.sets_func()


# print('---------- DICTIONARIES ----------')
# var_dict = {
#     'A': 'aa',
#     'B': 'bb',
#     'C': 'cc'
# }
#
# for x in var_dict:
#     if "A" in x:
#         var_dict.update({"B": 2020})
#         print("Yes, 'model' is one of the keys in the var_dict dictionary")
#         print(var_dict.get(x), ' = ', var_dict[x])
#
# print(var_dict.keys())
# var_dict.popitem()
# print(var_dict.values())
# var_dict.clear()
# print(var_dict.items())
# var_dict.setdefault("color", "white")
# var_dict = var_dict.copy()
# print(var_dict.items())
# print(type(var_dict))


# def add_func(a, b):
#     return a+b, a-b
#
#
# print(add_func(10, 20))


# n = int(input('Enter number for factorial:'))
#
# def factorial(n1):
#     if n1 == 0:
#         result = 1
#     else:
#         result = n1 * factorial(n1 - 1)
#     return result
#
#
# print(factorial(n))


"""def wish(name):
    print("Good Morning:", name)


greeting = wish
print(id(wish))
print(id(greeting))
greeting('Sandy')
wish('Sandeep')"""


import functools

# initializing list
lis = [1, 3, 5, 6, 2, 9]
lis1 = [11, 31, 51, 6, 2, 9]

# using reduce to compute sum of list
print("Reduce : The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))

# to filter out elements from two lists
flt = list(filter(lambda x: x % 2 != 0, lis1))
print('Filter : ', flt)

# to change values in one list or current list
map1 = list(map(lambda x: x * x, lis1))
print('Map : ', map1)


"""
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
"""
