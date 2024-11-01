import random
print("Welcome to number guessing game : ")
choice = random.randint(1,100)

def check_answer(guess,choice,turns):
    if guess>choice:
        print("Too High!!")
        return turns-1
    elif guess<choice:
        print("Too Low!!")
        return turns-1
    else:
        print(f"You have got it.The answer is {choice}")

def set_difficulty():
    choice = input("Choose a difficulty.Type 'easy' or 'hard' : ")
    if choice=="easy":
        print("You have 10 attempts remaining")
        return 10
    else:
        print("You have 5 attempts remaining")
        return 5

def game():
    turns = set_difficulty()
    guess = 0
    while guess!=choice:
        guess = int(input("Make a Guess : "))
        turns = check_answer(guess,choice,turns)
        if turns==0:
            print("You have run out of guesses,you lose")
            return
        elif guess!=choice:
            print(f"You have {turns} remaining ")
            print("Guess again")
game()