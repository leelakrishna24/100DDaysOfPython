#  median of a given list

list1 = [10,20,30,40,50,60,70,80,90,100]

if len(list1) % 2 != 0:
    median = list1[len(list1)//2]
else :
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2 - 1]
    median = (m1+m2) // 2

print(median)
