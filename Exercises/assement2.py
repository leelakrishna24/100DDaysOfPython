filepath = '/Users/saikrishna/PycharmProjects/python.txt'
cn = open(filepath,'w')
cn.write(input())
cn.close()
cn = open(filepath).read()
print(cn)