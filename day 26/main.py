import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter:row.code for (index,row) in data.iterrows()}
s = input().upper()
try :
    result = [new_dict[letter] for letter in s ]
except KeyError:
    print("Sorry, Enter only alphabets in english")
else:
    print(result)