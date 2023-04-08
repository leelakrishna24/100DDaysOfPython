# Write a Python program to convert temperatures from Celsius to Fahrenheit and vice versa

Temperature = input("Enter the temperature including the scale name : ")

print(Temperature)

temperature = Temperature.replace("C" or "F","")
print(temperature)


def Conversion(n):
    if "C" in Temperature:
        print("It is Celsius value")
        return (((int(n)*9)/5)+32)

    elif "F" in Temperature:
        print("it is Farenheit Value")
        return (((int(n)-32)*5)/9)

Conversion(temperature)
print(Conversion(temperature))
