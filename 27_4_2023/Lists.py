countries = ["US","UK","ITALY"]
del countries[2]
print(countries)
print(countries[::1])

list1 = ["10","11","12","13","14"]
print(list1[::3])

num = [4,4,3,1]
num.insert(2,3)
print(num)

ages = [20,30,40,50,60]
total = 0
for age in ages:
    total += age

print(total//len(ages))

for x in [0,2,1,3]:
    for y in [0,4,1,2]:
        print("*")

for letter in 'KodeKloud':
    if letter == 'u':
        continue
    print('Letter : ' + letter)

list1 = [1, 2, 3, 4]
for i, j in enumerate(list1):
    print(i, j)


letters = ["A", "B", "C", "D", "E"]
print(letters[1:])