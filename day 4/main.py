print("Rock,Paper,Scissors")
import random
choice = int(input("What do you choose? Type 0 for rock 1 for paper 2 for scissors"))
random = random.randint(0,2)
print("Your choice : ",choice)
if(choice==0):
    print("Rock")
elif(choice == 1):
    print("Paper")
elif(choice==2):
    print("Scissors")
print("Computer choice : ",random)
if(random==0):
    print("Rock")
elif(random==1):
    print("Paper")
elif(random==2):
    print("Scissors")

if(choice==0 and random==2):
    print("You win")
elif(choice==1 and random==0):
    print("You win")
elif(choice==2 and random==0):
    print("You lose")
elif(choice>random):
    print("You win")
elif(choice<random):
    print("You lose")
elif(choice==random):
    print("It's a draw")