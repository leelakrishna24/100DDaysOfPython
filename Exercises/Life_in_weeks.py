# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#consider days, weeks, months in a year are 365, 52 adn 12 respectively
rem_years = 90 - int(age)
rem_days = rem_years*365
rem_weeks = rem_years*52
rem_months = rem_years*12

print(f"You have {rem_days} days, {rem_weeks} weeks, and {rem_months} months left.")