# write a python program for fibonacci sequence

num = int(input("Enter the number till which you want to find the fibonacci sequence"))


def fibonacci(num):
    if num <= -1:
        print("Enter positive number")
    elif num == 0:
        return 0
    elif num == 1:
        return 1

# yet to be completed
