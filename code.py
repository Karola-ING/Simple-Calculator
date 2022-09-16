def is_a_number(real_number):
    try:
        float(real_number)
        return True
    except:
        return False


def ask_for_a_number(real_number): 
    if is_a_number(real_number) == False:
        print('\nThis ain\'t a number, mate. Try again.')


def is_valid_operator(operator):
    return operator == '*' or operator == '/' or operator == '+' or operator == '-' or operator == '%'


def ask_for_an_operator(operator):
    if is_valid_operator(operator) == False:
        print('\nOy mate, it ain\'t an operator. Try again.')


def calc(operator, a, b):
    a = float(a)
    b = float(b)
    if is_valid_operator:
        if operator == '*':
            print(a*b)
        if operator == '/' and b != '0':
            print(a/b)
        if operator == '+':
            print(a+b)
        if operator == '-':
            print(a-b)
        if operator == '%':
            print(a%b)


def calculate_again():
    loop = True
    while loop:
        answer = input('\nDo you want to calculate something else? [Yes / No]: ')
        if answer.upper() == 'YES' or answer.upper() == 'Y':
            calculate = True
            loop = False
            return calculate
        if answer.upper() == 'NO' or answer.upper() == 'N':
            calculate = False
            loop = False
            return calculate
        else:
            print('\nMate, you have to choose between Yes or No. Try Again.')


def simple_calculator():
    print('\nThis is a simple calculator you can use for same quick calculations.\nDon\'t expect too much, mate, just have fun.\n')
    print('You can use different operators to:\n[+] sum numbers,\n[-] substract them,\n[*] multiply,\n[/] divide,\n[%] or even determinate a modulo.')
    calculate = True
    while calculate:
        a = input('\nChoose your first number: ')
        real_number = a
        if is_a_number(real_number) == False:
            ask_for_a_number(real_number)
        else:
            operator = input('Which operator do you want to use?: ')
            if is_valid_operator(operator) == False:
                ask_for_an_operator(operator)
            else:
                b = input('Choose your second number: ')
                real_number = b
                if is_a_number(real_number) == False:
                    ask_for_a_number(real_number)
                else:
                    if operator == '/' and b == '0':
                        print('\nMate, dividing by 0 ain\'t a thing. Try again.')
                    else:
                        print('\nYour result is: ')
                        calc(operator, a, b)
                        again = calculate_again()
                        if again == False:
                            print('\nThanks mate. See ya!')
                            calculate = False

           
simple_calculator()
