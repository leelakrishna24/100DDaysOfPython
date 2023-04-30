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


letters = ["a", "b", "c", "d", "e"]
# print(letters.upper())

location = letters.index("d")
print(location)

print((4, 6) not in [(4, 7), (5, 6), "hello"])

list1 = [0, 3, 4, 1, 2]
list1[2:5]=[8,9]
print(list1)

list1=[3,4,6,1,2]
list2=list1
list1[0]=9
print(list2)

classroom = [
    ["sam","max","joe","annie"],
    ["sofie","lisa","tim","sasha"],
    ["claire","sara","leo","kim"],
    ["zoe","guy","anna","eva"]
]
for i in range(0,4):
    for j in range(0,4):
        print(classroom[i][j])
    print(f"{i+1}nd line")

a = []
for i in range(2):
    a.append([])
    for j in range(2):
        a[i].append(j)

print(a)

matrix = [[j for j in range(4)] for i in range(4)]
print(matrix)

matrix = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

matrix2 = []

for submatrix in matrix:
    for val in submatrix:
        matrix2.append(val)

print(matrix2)

countries = [['Egypt', 'USA', 'India'], ['Dubai', 'America', 'Spain'], ['London', 'England', 'France']]
countries2  = [country for sublist in countries for country in sublist if len(country) < 4]
print(countries2)
countries3 = []
for sublist in countries:
    for country in sublist:
        if len(country) < 4:
            countries3.append(country)

print(countries3)

num = [[1,2,3],[4,5,6,7],[8,9]]
print(num)
num2 = [[1,2,3],[4,5,6,],[7,8,9]]
print(num2)


for i in range(3):
    matrix.append([i])
    for j in range(3):
        matrix[i].append([j])

print(matrix)

matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)