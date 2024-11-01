import random

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculated_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Its a draw"
    elif computer_score==0:
        return "You lose!!"
    elif user_score==0:
        return "You Win!!"
    elif user_score>21:
        return "You lose!!"
    elif computer_score>21:
        return "You Win!!"
    elif user_score>computer_score:
        return "You Win!!"
    elif user_score<computer_score:
        return "You lose!!"

def play_game():
    user_cards = []
    computer_cards = []
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())
    is_game_over = False
    while not is_game_over:
        user_score = calculated_score(user_cards)
        computer_score = calculated_score(computer_cards)
        print(f"Your cards : {user_cards} , your score : {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
            choice = input("Type 'y' to get a card or type 'n' to pass")
            if choice == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculated_score(computer_cards)
    print(f"Your final cards : {user_cards}, Your final score : {user_score}")
    print(f"Computer final cards : {computer_cards}, computer final score : {computer_score}.")
    print(compare(user_score, computer_score))


while input("Type 'yes' if you want to play the game or type 'no' to pass") == "yes":
    play_game()

