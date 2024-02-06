def minimum(array):
    min_num = array[0]
    for num in array:
        if num < min_num:
            min_num = num
    

def maximum(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    return max_num

# Test the functions
numbers = [4, 6, 2, 1, 9, 6, 18, -45]
print("Minimum number:", minimum(numbers))
print("Maximum number:", maximum(numbers))



def maximum(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    return max_num

# Test the functions
numbers = [4, 6, 2, 1, 9, 6, 18, -45]
print("Minimum number:", minimum(numbers))
print("Maximum number:", maximum(numbers))


