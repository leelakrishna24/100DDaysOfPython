import sys

# print("Hello, my name is",sys.argv[1])

if len(sys.argv) < 2:
    sys.exit("Too many arguments")

for arg in sys.argv[1:-1]:
    print("Hello, my name is",arg)

# print("Hello my name is",sys.argv[1])


