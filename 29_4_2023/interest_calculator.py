principal = int(input("Enter the principal amount : "))
inst = float(input("enter the interest rate : "))
years = int(input("Enter the duration span : "))

def inst_calc(n,i):
    inst = round((n * 6.5)/ 100 , 2)
    print(f"interest for {i} year is {inst} and ",end = " ")
    return inst

for i in range(1,years + 1):
    principal = round(principal + inst_calc(principal,i),2)
    print(f"principal is {principal}",end = "\n")