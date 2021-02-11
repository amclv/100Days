# Comparison Operators
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to

# water_level = 50
 
# if water_level > 80:
#     print("Drain water")
# else:
#     print("Continue filling the bathtub")

# print("Check that number!\n")
# num = float(input("What is the number you want to check?\n"))

# if num % 2 == 0:
#     print("this is even!")
# else:
#     print("this is not even!")

# print("Welcoime to the rollercoaster!\n")
# height = int(input("What is your height in inches?: "))

# if height >= 65:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?: "))
#     if age <= 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you are too short for this ride.") 

# print("BMI Calculator 2.0\n")
# height = float(input("Enter your height: "))
# weight = float(input("Entr your weight: "))
# bmi = round(weight / height ** 2)

# if bmi < 18.5:
#     print(f"Underweight BMI: {bmi}")
# elif bmi < 25:
#     print(f"Normal Weight BMI: {bmi}")
# elif bmi < 30:
#     print(f"Overweight BMI: {bmi}")
# elif bmi < 35:
#     print(f"Obese BMI: {bmi}")
# else: 
#     print(f"Clinically Obese BMI: {bmi}")

# print("Leap Year! \n")

# year = int(input("Which ytear do you want to check?: "))

# if year & 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap year!")
#         else:
#             print("Not a leap year"
#     else:              
#         print("leap year")
# else:
#     print("Not a leap year")

# print("Welcome to Python Pizza\n")

# size = input("What size pizza do you want? S, M, or L\n")
# add_pepperoni = input("Do you want to add Pepperoni? Y or N?\n")
# extra_cheese = input("Do you want to add extra cheese? Y or N\n")
# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
    
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: {bill}")

# if 4 or 4 % 2 == 0:
#     print("True")
# else:
#     print("false")

# print("Love Calculator\n")

# name1 = input("What is your name?\n")
# name2 = input("What is their name?\n")

# combined_name = name1 + name2
# lowercased_names = combined_name.lower()

# t = lowercased_names.count("t")
# r = lowercased_names.count("r")
# u = lowercased_names.count("u")
# e = lowercased_names.count("e")

# true = t + r + u + e

# l = lowercased_names.count("l")
# o = lowercased_names.count("o")
# v = lowercased_names.count("v")
# e = lowercased_names.count("e")

# love = l + o + v + e

# love_score = int(str(true) + str(love))

# if (love_score < 10) or (love_score > 90):
#     print(f"Your score {love_score}, you go together like code and menthos")
# elif love_score >= 40 and love_score <= 50:
#     print(f"Your score is {love_score}, you are alright together")
# else:
#     print(f"Your score is {love_score}")