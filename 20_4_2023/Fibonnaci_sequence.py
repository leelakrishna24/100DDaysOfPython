# write a python program for fibonacci sequence

num = int(input("Enter the number till which you want to find the fibonacci sequence"))

# Define a function as fibonacci and loop
def fibonacci(num):
    if num <= -1:
        print("Enter positive number")
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

