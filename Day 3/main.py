print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice_1 = input("You are at a crossroad, where do you want to go? Type 'Left' or 'Right'\n").lower()

if choice_1 == "left":
    choice_2 = input("You came to a sudden stop, as a rope is dangling on a tree unsure of stableness over a river!. Do you want to 'Swim' or 'Rope'\n").lower()
    if choice_2 == "rope":
        choice_3 = input("You swinged across the river on the rope! You are presented with three doors. Which door do you want to take? 'Red', 'Blue' or 'Yellow'\n").lower()
        if choice_3 == "yellow":
            print("YOU WIN! YOU FOUND THE TREASURE! HERE IS YOUR ALL THE GOLD IN THE WORLD!")
        elif choice_3 == "blue":
            print("Game Over, eaten by beasts? That sucks man!")
        elif choice_3 == "red":
            print("Game Over, burned by fire! I bet you could go jump in that river now huh?")
        else:
            print("Game Over!")
    else:
        print("Game Over, you got attacked by an angry TROUT! ")
else:
    print("Game Over, you fell into a hole that has deadly poison spikes! OUCH!")