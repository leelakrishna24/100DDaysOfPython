def sum(n):
    # Write code here
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return n+ sum(n-1)

n = int(input())
print(sum(n))