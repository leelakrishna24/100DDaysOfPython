# i = 0
# for i in range(1,11):
#     if i != 3 and i != 5:
#         print(i)
#     i = i + 1


lang_list=[{"Name":'Python',"Type":'Compiled'},{"Name":'Java',"Type":'Compiled'},{"Name":'C',"Type":'Compiled'}]

user_input = input()

for char in lang_list:
    if char != 'user_input':
        print(char.get("Name"))