filepath = '/python.txt'


contents = open(filepath)
print(contents.readlines())
contents.close()

with open(filepath) as f:
    cn = f.readlines()
print(cn)