# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
#Write your code below this line 👇

print(size)
print(type(size))
print(add_pepperoni)
print(type(add_pepperoni))
print(extra_cheese)
print(type(extra_cheese))
#bill = pizza_price(size) + pepperoni(add_pepperoni) + cheese(extra_cheese)
#def pizza_price(size) + pepperoni(add_pepperoni) + cheese(extra_cheese)
def pizza_price(size):
    if size == "S":
        return 15
    elif size == "M":
        return 20
    elif size == "L":
        return 25
def pepperoni_price(add_pepperoni):
    if add_pepperoni == "Y" and size == "S":
        return 2
    elif add_pepperoni == "Y" and size == ("M" or "L"):
        return 3
    else:
        return 0
def cheese_price(extra_cheese):
    if extra_cheese == "Y":
        return 1
    elif extra_cheese == "N":
        return 0
bill = pizza_price(size) + pepperoni_price(add_pepperoni) + cheese_price(extra_cheese)
print('$',bill,sep='')

