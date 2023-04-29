def find_missingnum(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1,n[-1]):
        if i not in numbers:
            print(f"missing number is {i}",end= ", ")
            output.append(i)
    return output

list_of_numbers = []
for i in range(1,20):
    if i % 3 == 0:
        list_of_numbers.append(i)
print(f"list of numbers = {list_of_numbers}")

print(find_missingnum((list_of_numbers)))
