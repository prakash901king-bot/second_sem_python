try:
    number=int(input("enter a number "))
    index=int(input("enter a index "))
    numbers=[10,20,30]
    devi=100/number
    print("devision is ",devi)
    print("index value is ",numbers[index])
except ZeroDivisionError:
    print("cannot divide by zero")

except ValueError:
    print("invalid input")

except IndexError:
    print("index out of range")
    