nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
result=[value for row in nested_list for value in row]
print (result)