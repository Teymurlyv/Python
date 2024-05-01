def Even_nums(list):
    even_numbers = []
    for num in list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Even numbers:", Even_nums(sample_list))