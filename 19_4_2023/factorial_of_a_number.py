n = int(input("Enter the number to which you want to find the factorial: "))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factorial(n)
print(factorial(n))
