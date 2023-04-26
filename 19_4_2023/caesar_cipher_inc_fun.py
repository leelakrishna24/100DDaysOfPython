# take the input text from user
raw_string = input("enter text to cipher: ")

# take the shift value from user
shift = int(input("Enter the shift: "))
# print(len(raw_string))

# ord(" ") returns ascii value of text , chr(" ") returns
print("cipher_string",end=' = ')
for i in raw_string:
    # print(ord(i))
    # print(ord(i) + shift)
    if ord(i) in range(65,90) or range(97,122):
        print(chr(ord(i) + shift), end='')
    else:
        print("please input text only")