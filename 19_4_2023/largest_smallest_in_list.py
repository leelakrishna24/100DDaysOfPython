# program for finding largest and smallest number in a list
my_list = [8,2,4,12,6,0,10]

# print(min(my_list))
# print(max(my_list))

# initialise variables for small and large
largest_number = my_list[0]
smallest_number = my_list[0]

# loop through list of numbers to find smallest and largest number
for num in my_list:
    if num > largest_number:
        largest_number = num
    elif num < smallest_number:
        smallest_number = num

print(largest_number)
print(smallest_number)
