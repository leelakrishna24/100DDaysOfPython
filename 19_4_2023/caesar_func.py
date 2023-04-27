small_alphabets = "abcdefghijklmnopqrstuvwxyz"
a2z = []
for i in small_alphabets:
    a2z.append(i)
# print(a2z)

cap_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
A2Z = []
for i in cap_alphabets:
    A2Z.append(i)
# print(A2Z)



def encode(x):
    cipher_value = ''
    for char in raw_string:
        if char in small_alphabets:
            j = a2z.index(char) + shift
            cipher_value = ''.join([cipher_value, a2z[j]])
        elif i in cap_alphabets:
            j = A2Z.index(char) + shift
            cipher_value = ''.join([cipher_value, A2Z[j]])

    print(f"Cipher text = '{cipher_value}'")


def decode(x):
    raw_value = ''
    for char in cipher_string:
        if char in small_alphabets:
            j = a2z.index(char) - shift
            raw_value = ''.join([raw_value, a2z[j]])
        elif i in cap_alphabets:
            j = A2Z.index(char) - shift
            raw_value = ''.join([raw_value, A2Z[j]])

    print(f"Raw text = '{raw_value}'")


while True:
    # ask user whether to decode or encode
    choice = input("Choose whether you want to : \n" "1.Encode\n"  "2.Decode\n"  "3.Exit\n")
    if choice == "1":
        # take the input text from user
        raw_string = input("Enter text to Encode: ")
        # take the shift value from user
        shift = int(input("Enter the Shift: "))
        encode(raw_string)
    elif choice == "2":
        # take the encoded text from user
        cipher_string = input("Enter text to Decode: ")
        # take the shift value from user
        shift = int(input("Enter the Shift: "))
        decode(cipher_string)
    elif choice == "3":
        print("bye 👋")
        break
    else:
        print("Improper choice , please choose a proper choice")
