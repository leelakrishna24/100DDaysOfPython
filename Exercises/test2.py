plate = input("Enter vanity plate number: ")
length_plate = len(plate)
s_plate = 0
i_plate = 0

for i in range(0,length_plate):
    if plate[i].isdigit():
        i_plate += 1
       # print(plate[i])

    elif not plate[i].isdigit():
        s_plate += 1
    i = 1+1

print("integer: ", i_plate)
print("characters: ", s_plate)
print(type(i_plate))

for i in range(0,i_plate):
    print(plate[i])
