s = input("Enter vanity plate ID: ")
length_s = int(len(s))
# print(length_s)
if len(s) <= 6 and len(s) > 2:
    print("perfect sized number plate first print")
    i = 0

    for length_s in s:
        if not s[0:1].isdigit() :
            print("starts with two letters ")
            if s[-1].isdigit():
                print("ends with number")
            else:
                print("not ends with number")
        else:
            print("not starts with two letters ")
else:
    print("not a perfect sized dnumber")