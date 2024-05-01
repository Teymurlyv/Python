def Is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number)):
        if number % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if Is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")