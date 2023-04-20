# Write a Python program to convert temperatures from Celsius to Fahrenheit and vice versa
#take the temperature measure input
Temperature = input("Enter the temperature including the scale name : ")
print(Temperature)

#Replace the reading scale name with empty
temperature = Temperature.replace("C" or "F","")
print(temperature)

# Convert the value to
def Conversion(n):
    if "C" in Temperature:
        print("It is Celsius value")
        return str(((int(n)*9)/5)+32)+ "F"

    elif "F" in Temperature:
        print("it is Farenheit Value")
        return str(((int(n)-32)*5)/9)+ "C"

Conversion(temperature)
print(Conversion(temperature))
