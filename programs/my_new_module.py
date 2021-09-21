person1 = {
  "name": "John",
  "age": 30,
  "country": "Norway"
}


def arith_func():
    print('--------- Arithmetic ---------')
    try:
        num1 = int(input("Enter number one : "))
        num2 = int(input("Enter number two : "))
        a = num1 / num2
        print("try-except : ", a)
    except ArithmeticError:
        print("try-except : Error...", ArithmeticError)


def multi_try():
    print('--------- Multiple Try ---------')
    try:
        a = int(input("enter 1st number of arithmetic operations: "))
        b = int(input("enter 2nd number of arithmetic operations: "))
        print(a / b)
        num = [1, 2, 3]
        print(num[10])
    except ArithmeticError as ex1:
        print("Arithmetic error...", ex1)
    except IndexError as ex2:
        print("Index error...", ex2)


def try_else_func():
    print('-------- TRY ELSE ----------')
    a = int(input("enter 1st number of arithmetic operations: "))
    b = int(input("enter 2nd number of arithmetic operations: "))
    try:
        if b <= 0:
            raise Exception("Sorry, no numbers below zero")
        else:
            c = a / b
    except ArithmeticError:
        print('Math Error')
        print('I have done ex handling')
    except Exception as e:
        print("Raise Exception : ", e)
    else:
        print(c)
        print('hello i am in else block')
    finally:
        print('Hey, I am always here for you.. You are in finally!')
