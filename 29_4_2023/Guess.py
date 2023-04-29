import random

n = random.randrange(1, 10)
guess = int(input("Enter a number : "))
while n != guess:
    if guess < n:
        print("Too Low")
        guess = int(input("Enter a number : "))
    elif guess > n:
        print("Too High")
        guess = int(input("Enter a number : "))
    else:
        break

print(f"your guessed number is right !! ")