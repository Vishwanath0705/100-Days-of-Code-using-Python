print("caesar cipher")
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def ceasar(txt,dir,shift_n):
    end_text = ""
    for i in txt:
        if i in alphabet:
            position = alphabet.index(i)
            if dir=="encode":
                new_position = position+shift_n
            else:
                new_position = position-shift_n
            end_text+=alphabet[new_position]
        else:
            end_text+=i
    print(f"The {dir}d text is: {end_text}")

end_of_game = False
while not end_of_game:
    direction = input("Enter 'encode' to encode and 'decode' to decode : ")
    shift = int(input("Enter shift number : "))
    text = input("Enter the message : ").lower()
    shift = shift%26
    ceasar(text,direction,shift)
    result = input("type 'yes' to continue the game ,type'no' to stop the game : ")
    if result=="no":
        end_of_game=True
        print("Game Over!!")