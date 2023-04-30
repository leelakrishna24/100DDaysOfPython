a = []
for i in range(5):
    a.append([])
    for j in range(5):
        a[i].append(j)

print(a)
print(a[2][3])

matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
print(matrix)

matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

matrix2 = []

for submatrix in matrix:
    for val in submatrix:
        matrix2.append(val)

print(matrix2)