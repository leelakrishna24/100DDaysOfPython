# take the input text from user
raw_string = input("enter text to cipher: ")
# take the shift value from user
shift = int(input("Enter the shift: "))

small_alphabets = "abcdefghijklmnopqrstuvwxyz"
a2z = []
for i in small_alphabets:
    a2z.append(i)

cap_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
A2Z = []
for i in cap_alphabets:
    A2Z.append(i)

# print(a2z)
# print(A2Z)
cipher_value = ''
j = ''
for i in raw_string:
    if i in small_alphabets:
        #  print("small_alphabet")
        #print(a2z[a2z.index(i) + shift],end='')
        j = a2z.index(i) + shift
        cipher_value = ''.join([cipher_value,a2z[j]])
    elif i in cap_alphabets:
        #  print("capital_alphabet")
        #print(A2Z[A2Z.index(i) + shift],end='')
        j = A2Z.index(i) + shift
        cipher_value = ''.join([cipher_value,A2Z[j]])

print(cipher_value)