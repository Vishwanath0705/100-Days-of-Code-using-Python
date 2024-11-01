print("Hangman ")
import random
stages = ['''
  +---+
  |   |
  O   |
 |||  |
 |  | |
      |
=========
''', '''
  +---+
  |   |
  O   |
 |||  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|  |
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

words = ['ardvark','baboon','camel']
choice = random.choice(words)
length = len(choice)
string=[]
for i in range(length):
    string.append("-")
print(f"{''.join(string)}")
lives = 7
end_of_game = False
while not end_of_game:
    n = input("Enter a letter : ")
    if n in string:
        print("You have already entered the letter")
    for i in range(0,length):
        letter = choice[i]
        if letter == n:
            string[i] = n
    print(f"{''.join(string)}")
    if n not in choice:
        lives-=1
        print(stages[lives])
        print("Lives left : ",lives)
        if lives==0:
            print("You lose")
            end_of_game=True
    if "-" not in string:
        print("You win")
        end_of_game=True
