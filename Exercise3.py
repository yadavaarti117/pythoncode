
#Exercise3
temperature=int(input("Enter the temperature in celsius:"))

if temperature >= 30:
    print("ts hot! Wear light clothes and stay hydrated")

elif temperature >= 20 and temperature <= 30:
    print("pleasant weather! comfor clothes work well")

elif temperature >= 10 and temperature <= 19:
    print("A bit cool. Wear a light jacket.")

elif temperature <10 :
    print("Iis too cold.")

 #exercise 1

print("Life stage Analyzer")

age = int(input("Enter your age:"))

print("\n-----Analysis Report------\n")

current_year = 2025
birth_year = current_year - age

print("Age:", age)
print("Birth Year:", birth_year)

#life stage classification
if age >= 0 and age <= 12:
    print("Life stage:Child")
elif age >= 13 and age <= 19:
    print("Life_stage:Teenager")
elif age >= 20 and age <= 35:
    print("Life_stage:Young Adult")
elif age >= 36 and age <= 59:
    print("Life_stage:Adult")
else:
    print("life_stage:Senior")

#Generation identification

if birth_year >= 2013:
    print("Generation :Gen Alpha")
elif birth_year >= 1997:
    print("Generation :Gen Z")
elif birth_year >= 1981:
    print("Generation :Millennial")
elif birth_year >= 1965:
    print("Generation :Gen X")
elif birth_year >= 1946:
    print("Generation :Baby Boomer")
else:
    print("Generation :Silent Generation")

#Voting eligibility

if age >= 18:
    print("Can Vote")
else:
    print("Cannot vote yet")

#Driving lisence

if age >=18:
    print("Can get lisence")

else:
    print("Too young to Drive")

#Blood donation eligibility

if age >= 18 and age <= 65:
    print("Can Donate blood")
else:
    print("Cannot donate blood")

#Bank account
if age >= 18:
    print("Can open account independently")
else:
    print(" Needs parent/guardian")

#reterment ststus
if age >= 60:
    print("Retirement age Reached")
else:
    print(" Not yet retired")

#exercise 2

age = int(input("Enter your age: "))
days = """
1: Sunday
2: Monday
3: Tuesday
4: Wednesday
5: Thursday
6: Friday
7: Saturday
"""

print(days)
day_of_the_week = int(input("Enter the day of the week: "))

CHILDREN = 0
CHILDREN_BASE_PRICE = 150
ADULTS = 1
ADULT_BASE_PRICE = 250
SENIORS = 2
SENIOR_BASE_PRICE = 200


if age < 12:
    age_category = CHILDREN
elif 12 <= age <= 59:
    age_category = ADULTS
elif 60 <= age <= 120:
    age_category = SENIORS

# Weekday price calculation
if 2 <= day_of_the_week <= 6:
    if age_category == CHILDREN:
        price = CHILDREN_BASE_PRICE - 0.2 * CHILDREN_BASE_PRICE
    elif age_category == ADULTS:
        price = ADULT_BASE_PRICE
    elif age_category == SENIORS:
        price = SENIOR_BASE_PRICE - 0.3 * SENIOR_BASE_PRICE

else:
    if age_category == CHILDREN:
        price = CHILDREN_BASE_PRICE
    elif age_category == ADULTS:
        price = ADULT_BASE_PRICE
    elif age_category == SENIORS:
        price = SENIOR_BASE_PRICE
    
    if age == 18 or age == 60:
        print("You got a b'day discount of Rs. 50!")
        price = price - 50
        

print(f"Age: {age}\nDay of the Week: {day_of_the_week}\nPrice: {price}")

print("Add")   
    
    
    

    
