principal = int(input("Enter the principal amount : "))
inst = float(input("enter the interest rate : "))
years = int(input("Enter the duration span : "))

def inst_calc(n,i):
    inst = round((n * 6.5)/ 100)
    print(f"interest for {i} year is {inst}",end = " ")
    return inst

for i in range(1,years + 1):
    principal = principal + inst_calc(principal,i)
    print(f"principal for {i} year is : {principal}",end = "\n")