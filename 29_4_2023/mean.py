# mean of list

from time import time
start = time()

list1 = [10,20,30,40,50,60,70,80,90,100]
mean = sum(list1)//len(list1)
print(mean)

end = time()
execution_time = end - start
print(execution_time)
print(execution_time * 60 * 60 * 60 )