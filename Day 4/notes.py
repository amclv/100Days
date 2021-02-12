import random

# random_int =  random.randint(1, 10)
# print(random_int)


#0.00000000 - 0.9999999....
# random_float = random.random()
# print(random_float)

# # 0.00000000 - 4.999999....
# num = random_float * 5
# print(num)

# love_score = random.randint(1, 100)
# print(love_score)

# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")


# Python Lists

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# # You can add a single item to the list or a group of a list.
# states_of_america.append("Ezraland")
# states_of_america.extend(["Aaronland", "Yeniferland"])

# print(states_of_america)

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# names_string = input("Give me everybody\'s names, seperated by a comma.\n")

# names = names_string.split(", ")
# print(names)

# rand_names = random.choice(names)
# print(f"{rand_names} is a bastard")

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?: ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")