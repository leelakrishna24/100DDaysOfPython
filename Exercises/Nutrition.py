#take the fruit name from user
fruit_name = input("Item: ").lower()

#make a dictionary of all the fruits and calorie values respectively
Fruit_Nutrition = {'apple': '130', 'avocado': '50', 'kiwifruit': '90', 'pear': '100', 'sweet cherries': '100'}

# use condition to check whether fruit is in our dictionary or not
if fruit_name in Fruit_Nutrition:
     print(Fruit_Nutrition.get(fruit_name))
#if user fruit is not in our dictionary print ""
else:
     print("")