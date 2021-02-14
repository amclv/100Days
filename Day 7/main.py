import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]
random_word = random.choice(word_list)
word_length = len(random_word)
lives = word_length
end_game = False

print(f"Chosen word is: {random_word}") 
display = []

for _ in range(word_length):
    display += "_"
print(display)

while not end_game:
    letter_choice = input("Guess a letter: ").lower()
    for position in range(word_length):
        char = random_word[position]
        if char == letter_choice:
            display[position] = char
    
    if letter_choice not in random_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose.")
    
    print(display)
            
    if "_" not in display:
        end_game = True
        print("You win.")
        
    print(stages[lives])