person1 = {
  "name": "new_mod John",
  "age": "new_mod  39",
  "country": "new_mod Norway"
}

import random


def func_mod(*n):
    print('------------------')
    print(n)
    for n1 in n:
        for i in n1:
            if i == 1:
                break
            print('i : ', i)


def rand_func():
    print('------------------')
    print("Random : ", random.random())
    print("RandInt : ", random.randint(999, 10000))
    print("Uniform : ", random.uniform(19, 1900))


def m1():
    print('------------------')
    print(__name__)
    if __name__ == '__main__':
        print("The code is executed as a program")
    else:
        print("The code executed as a module from some other program")
