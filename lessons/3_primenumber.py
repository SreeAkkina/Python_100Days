def prime_number_check(num):
    for i in range(2,num - 1):
        if num % i == 0:
            return "not prime"
    return "prime"

num = int(input("Please enter a number to check >>> "))
prime = prime_number_check(num = num)
print(prime)