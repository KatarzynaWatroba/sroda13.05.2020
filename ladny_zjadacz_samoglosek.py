user_input = input("Please, write a word: ")
user_input = user_input.upper() 
forbidden_letters = ["A", "E", "I", "O", "U"]
polaczone = ""
for capital_letter in user_input:
    if capital_letter in forbidden_letters:
        continue
    polaczone = polaczone + capital_letter
print(polaczone)

    
    
    
    
    
# pierwsze = "dupa"



# for litera in pierwsze:
    # locze poszczeglne
    
    
# wyswietlam poloczone