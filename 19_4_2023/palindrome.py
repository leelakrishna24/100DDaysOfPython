# program too check whether a giver string is palindrome or not

my_str = input("Enter a string to verify whether it is palindrome or not: ")

len_str = len(my_str)

# def palindrome(n):
#     if my_str[0:] == my_str[-1:]:
#         print("palindrome")
#     else:
#         print("not a palindrome")
#
# palindrome(my_str)

# print(my_str[0:])
# print(my_str[::-1])
# for i in my_str:
#     print(i, end='')
#
# print()
# for i in my_str[::-1]:
#     print(i, end='')
#
# print()


def palindrome(n):
    if my_str[0:] == my_str[::-1]:
        return "palindrome"
    else:
        return "not a palindrome"


palindrome(my_str)
print(palindrome(my_str))
