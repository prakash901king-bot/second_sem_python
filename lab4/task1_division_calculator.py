try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    devide= first_number / second_number
    print("your devision is=",devide)
except ZeroDivisionError:
    print('cannot divide by zero')