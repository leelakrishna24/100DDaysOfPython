count = 0
with open("/Users/saikrishna/Downloads/strings86.txt","r") as read_string:
    urls = read_string.readlines()
    for row in urls:

        word = "http"

        if row.find(word) != -1:
            print(row.find(word))
            count += 1
            print(count ,'line Number:', urls.index(row), row,end='')



