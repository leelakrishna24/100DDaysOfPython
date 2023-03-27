# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#
# def divfour(a):
#     return a % 4
#
# def divhun(a):
#     return int(a) % 100
#
# def divfourhun(a):
#     return int(a) % 400


# if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#     print("Leap year.")
# else:
#     print("Not leap year.")

if ((year % 400 == 0) or (year % 100 != 0) and (year % 4) == 0):
    print("Leap year.")
else:
    print("Not leap year.")

