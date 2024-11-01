print("Welcome to py password generator!")
import random
l = int(input("Enter number of letters you wouls like in password:"))
s = int(input("Enteer number of symbols you would like in password:"))
n = int(input("Enter nummber of numbers you would like in password:"))
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = [';','@','#','$','%','&','*','(',')','+']
password = []
for i in range(1,l+1):
    password.append(random.choice(letters))
for i in range(1,s+1):
    #password += random.choice(symbols)
    password.append(random.choice(symbols))
for i in range(1,n+1):
    #password+=random.choice(numbers)
    password.append(random.choice(numbers))
random.shuffle(password)
final = ""
for i in password:
    final = final+i
print("Password : ",final)