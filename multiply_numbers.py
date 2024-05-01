def Multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

list = [8, 2, 3, -1, 7]

result = Multiply_numbers(list)
print(result)