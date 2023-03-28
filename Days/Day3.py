print('''
*******************************************************************************
      - ______ \ - ______ \ / _____   //.  .  ._______/
     / /     / // /     / //_/     / // ___   /
    / /     / // /     / /       .-'//_/|_/,-'
   / /     / // /     / /     .-'.-'
  / /     / // /     / /     / /
 / /     / // /     / /     / /
/ /_____/ // /_____/ /     / /
\________- \________-     /_/
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

Choose_Left_or_Right = input("You're at a cross road. please enter whether you want to go left or right")
print(Choose_Left_or_Right)
if Choose_Left_or_Right == "right":
    Choose_Swim_or_Wait = input("Choose whether you want to wait or swim to travel to treasure island")
    print(Choose_Swim_or_Wait)
    if Choose_Swim_or_Wait == "wait":
        Choose_Door_Colour = input("Choose which colour door you want to enter into")
        if Choose_Door_Colour == "yellow":
            print("You win!")
        elif Choose_Door_Colour == "red":
            print("Burned by fire Game Over.")
        elif Choose_Door_Colour == "blue":
            print("Eaten by beasts Game Over.")
        else:
            print("Game Over")
    elif Choose_Left_or_Right == "swim":
        print("Attacked by trout Game Over.")
    else:
        print("Attacked by trout Game Over.")
else:
    print("Fall into a hole Game Over.")