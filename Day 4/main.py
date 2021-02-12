import random
print("ROCK, PAPER, SCISSORS!\n")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

p1_choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors\n"))
comp_ans = random.randint(0, 2)

print(comp_ans)
print(p1_choice)

if p1_choice >= 3 or p1_choice < 0:
    print("You typed an invalid number, you lose")
elif p1_choice == 0 and comp_ans == 2:
    print("You win")
elif comp_ans == 0 and p1_choice == 2:
    print("You lose")
elif comp_ans > p1_choice:
    print("You lose")
elif p1_choice > comp_ans:
    print("You win")
elif comp_ans == p1_choice:
    print("Its a draw")