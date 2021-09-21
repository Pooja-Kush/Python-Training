print('------------ Class Object ------------')


class MyClass:
    a, b = 100, 200

    def __init__(self):
        print("I am a MyClass Constructor")

    def fun_add(self, a):
        print(a, self.b)


class MyClass2(MyClass):
    a, b = 0, 9

    def __init__(self):
        super().__init__()
        print("I am a MyClass2 Constructor")


# obj1 = MyClass2()
# obj1.fun_add(10)


class MulLev:
    def func_add(self):
        print("Multilevel Inheritance 1")
        print("Addition of", self.a, "and", self.b, "is :", (self.a + self.b), "\n")


class MulLev2(MulLev):
    def func_subtract(self):
        print("Multilevel Inheritance 2")
        print("Subtraction of", self.a, "and", self.b, "is :", (self.a - self.b), "\n")


class MulLev3(MulLev2):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("I am here : MulLev3")

    def func_multiply(self):
        print("Multilevel Inheritance 3")
        print("Multiplication of", self.a, "and", self.b, "is :", (self.a * self.b), "\n")


# a1 = eval(input("Enter 1st number : "))
# b1 = eval(input("Enter 2nd number : "))
# mulLev_obj = MulLev3(a1, b1)
# mulLev_obj.func_add()
# mulLev_obj.func_subtract()
# mulLev_obj.func_multiply()


class Multiple1:
    def func_add(self):
        print("Multiple Inheritance 1")
        print("Addition of", self.a, "and", self.b, "is :", (self.a + self.b), "\n")


class Multiple2:
    def func_subtract(self):
        print("Multiple Inheritance 2")
        print("Subtraction of", self.a, "and", self.b, "is :", (self.a - self.b), "\n")


class Multiple3(Multiple1, Multiple2):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().func_add()
        super().func_subtract()


# a1 = eval(input("Enter 1st number : "))
# b1 = eval(input("Enter 2nd number : "))
# multiple_obj = Multiple3(a1, b1)


class Hierarchy1:
    def __init__(self):
        a1 = eval(input("Enter 1st number : "))
        b1 = eval(input("Enter 2nd number : "))
        self.a = a1
        self.b = b1


class Hierarchy2(Hierarchy1):
    def func_subtract(self):
        print("Hierarchical Inheritance 2")
        print("Subtraction of", self.a, "and", self.b, "is :", (self.a - self.b), "\n")


class Hierarchy3(Hierarchy1):
    def func_add(self):
        print("Hierarchical Inheritance 3")
        print("Addition of", self.a, "and", self.b, "is :", (self.a + self.b), "\n")


# h2_obj = Hierarchy2()
# h2_obj.func_subtract()
#
# h3_obj = Hierarchy3()
# h3_obj.func_add()


class HybridInherit(Multiple3, MulLev3):
    def __init__(self):
        a1 = eval(input("Enter 1st number : "))
        b1 = eval(input("Enter 2nd number : "))
        self.a = a1
        self.b = b1
        MulLev3(self.a, self.b).func_subtract()


# hybrid_obj = HybridInherit()
# hybrid_obj.func_add()


a = eval(input("Enter 1st global number : "))
b = eval(input("Enter 2nd global number : "))
name = "XYZ"


class SingleInherit1:
    a, b = 10, 20


class SingleInherit2(SingleInherit1):
    a, b = 2, 3

    def __init__(self, i, j):
        print(i + j)
        print(self.a + self.b)
        print(super().a + super().b)
        print(globals()['a'] + globals()['b'])
        print(name)

    def __str__(self):
        return 'Learning Python is very Easy'

    def __del__(self):
        print('Object Destroyed')


# singleInherit_obj = SingleInherit2(1, 5)
# print(singleInherit_obj)
# del singleInherit_obj
# # print(singleInherit_obj)


from abc import ABC, abstractmethod


class MyClass1w(ABC):
    @abstractmethod
    def m1(self):
        pass

    def __init__(self):
        # taking global variable values a and b
        print("Add :", a + b)
        self.func_subtract()

    def func_subtract(self):
        print("Sub :", a - b)


class MyClass2w(MyClass1w):
    def m1(self):
        print('Abstraction')


b = MyClass2w()
b.m1()

