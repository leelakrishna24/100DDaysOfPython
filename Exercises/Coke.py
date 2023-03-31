#variable value to keep track
amount_due = 50

#loop for calculating the balance amount
while amount_due > 0:
    print("Amount Due: ", amount_due)
    coin = int(input(""))
    # print amount due by removing the nearest coin value
    if coin in [25, 10, 5]:
        amount_due = amount_due - coin


# change_owed = abs(amount_due)
change_owed = abs(amount_due)
# print("change owed", change_owed)
print("Change_owed:" ,change_owed)