user_input = input("Please, write a word: ")
user_input = user_input.upper() 
#print(user_input.upper())
 #A, E, I, O, U 
 


 
"""for capital_letter in user_input:
    if capital_letter == "A" or capital_letter == "E" or capital_letter == "I" or capital_letter == "O" or capital_letter == "U":
        continue
    print(capital_letter)"""
    
    
    
    
 #Druga wersja
 
"""forbidden_letters = ["A", "E", "I", "O", "U"]
for capital_letter in user_input:
    if capital_letter in forbidden_letters:
        continue
    print(capital_letter)"""


#trzecia wersja z if, else, elif

forbidden_letters = ["A", "E", "I", "O", "U"]
for capital_letter in user_input:
    if capital_letter in forbidden_letters:
        continue
    else:
        print(capital_letter)    
    
    
    
    