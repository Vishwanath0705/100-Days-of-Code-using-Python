print("Welcome to treasure hunt!!")
print("Your mission is to find the treasure!!")
dir = input("Where you want to go ?Type 'left' or 'right' : ").lower()
if dir=="left":
    isl = input("You have come to a lake. There is an island in the middle of the lake type 'wait' to wait for th eboat or type 'swim' to swim through the lake: ")
    if isl=="wait":
        door = input("You have arrived at the island unharmed.There is house with 3 doors yellow,blue and red type which door you want to open : ")
        if door=="yellow":
            print("you have found the treasure")
        elif door == "red":
            print("It is a house full of fire. Game Over!!")
        else:
            print("You enterd a room of beasts.Game over!!")
    else:
        print("You are attacked by a hungry shark.Game Over!!")
else:
    print("You fell in a hole.GameOver!!")