"""print("Welcome to band name generator!!")
city = input("Enter city name ? ")
pet = input("Enter your pet name ? ")
print(f"Your Band name is : {city}{pet}")"""

#Band name generator
print("Welcome to band name generator")

#intialize the variables to empty strings
city = ""
pet = ""

#simple check whether the user had entered something

while True:
    city = input("Enter the city you grew up in : ")
    if city == "":
        print("You haven't entered anything .Please try again")
    else:
        break
#simple check whether the user has entered something in place of pet
while True:
    pet = input("Enter your pet name : ")
    if pet == "":
        print("You haven't entered anything .Please Try again")
    else:
        break

print(f"Your band name is {city}{pet}")
