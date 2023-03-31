#take input string from user
statement = input("input")

#choose and declare the characters to be replaces
replace_string = {"a","e","i","o","u","A","E","I","O","U"}

#initiate for loop to replace characters with space from user given statement

for char in replace_string:
     statement = statement.replace(char,"")

#print replaced statement
print(statement)

