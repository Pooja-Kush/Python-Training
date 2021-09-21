# for printing the triangle pattern
def triangle_pattern():
    print("triangle_pattern : ")
    val = int(input("Enter number of columns(Note-It should be a odd number) : "))
    row = 0
    col = 0
    row_count = val//2
    print("Here is your triangle pattern : ")

    for row in range(1, row_count+2):
        pattern = ''
        for col in range(1, val+1):
            if row+col > row_count+1 and col-row <= row_count:
                pattern += ' * '
            else:
                pattern += '   '

        print(pattern, '\n')


# For getting the count of vowels in word or sentence
def count_vowels():
    vowel = 0
    word = str(input("Enter any word/sentence : "))
    for w in word:
        if w in 'aeiouAEIOU':
            vowel += 1

    print("Number of vowels are ", vowel)


# For removing vowels from word or sentence
def remove_vowels():
    new_word = ''
    word = str(input("Enter any word/sentence : "))
    for w in word:
        if w not in 'aeiouAEIOU':
            new_word += w

    print("After removing vowels : ", new_word)


# For reversing the string
def reverse_str():
    word = str(input("Enter any word/sentence : "))
    new_word = word[::-1]
    new_list = word.split(' ')

    new_sentence = ''
    new_sen = new_list[::-1]
    for w in new_sen:
        new_sentence += w
        new_sentence += ' '

    print("After reversing string : \n", new_word, "\n", new_sentence)


# Simple Work Flow
VIEW = """
    CHOOSE ANY OPTION : 
    1) Programs
    2) Login 
    3) Signup
    100) Exit
"""
print(VIEW)

choice = int(input("Press any one option number : "))

if choice == 1:
    PRO_VIEW = """
        CHOOSE ANY OPTION : 
        1) Leap year 
        2) Palindrome Number
        3) Armstrong Number
        4) Prime Number
        5) Triangle Pattern
        6) Count Number of Vowels
        7) Remove Vowels
        8) Reverse String
        100) Exit
    """
    print(PRO_VIEW)
    pro_choice = int(input("Press any one option number : "))

    if pro_choice == 8:
        reverse_str()

    if pro_choice == 7:
        remove_vowels()

    if pro_choice == 6:
        count_vowels()

    if pro_choice == 5:
        triangle_pattern()

    if pro_choice == 4:
        # Prime Number Program
        num = int(input("Enter the number : "))
        i = 2
        m = num // 2
        flag = 0

        while i <= m:
            i = i + 1
            if num % i == 0:
                print("Number is not prime")
                flag = 1
                break

        if flag == 0:
            print("Number is Prime")

    if pro_choice == 3:
        # Armstrong Number Program (153, 370, 371)
        num = int(input("Enter the number : "))
        temp = num
        sum_num = 0

        while num > 0:
            rem = num % 10
            sum_num = (rem ** 3) + sum_num
            num = num // 10
            print(rem)

        if temp == sum_num:
            output = "Number '{}' is Armstrong"
        else:
            output = "Number '{}' is not Armstrong"

        print(output.format(temp))

    if pro_choice == 2:
        # Palindrome Number Program
        num = int(input("Enter the number : "))
        temp = num
        sum_num = 0

        while num > 0:
            rem = num % 10
            sum_num = (sum_num * 10) + rem
            num = num // 10

        if temp == sum_num:
            output = "Number '{}' is Palindrome"
        else:
            output = "Number '{}' is not Palindrome"

        print(output.format(temp))

    if pro_choice == 1:
        # Leap Year Program
        year = int(input("Enter the year : "))

        if year < 1960:
            output = "You enter : {}, but year should be greater or equal to '1960'"
            print(output.format(year))
        else:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                print('Year is leap')
            else:
                print('Year is not leap')

elif choice == 2:
    print("Your choice is login!")
    username = str(input("Enter Username : "))
    password = str(input("Enter Password : "))

    if username != '' and password != '':
        message = "***** Logged In Successfully! ***** \nUsername is '{}' and \nPassword is '{}'"
        print(message.format(username, password))
    else:
        print("***** Fail to Login! ***** \nUsername or password is missing..")

elif choice == 3:
    print("Your choice is Signup!")


