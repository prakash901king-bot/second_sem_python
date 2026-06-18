#write a dictionary comprehension that takes a list of numbers [1,2,3,4,5] and creats a dictionary where each number ket, and its square (number multiplied by itself) is the value.
numbers =[1,2,3,4,5]
val={value: value**2 for value in numbers}
print(val)