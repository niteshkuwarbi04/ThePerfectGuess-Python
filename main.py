'''
A program that generates a random number and asks the user to guess it.
If the player's guess is higher than the actual number, the program displays "Lower number please".
Similarly when player guesses a lower number, the program displays "Higher number please".
When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.
'''

import random
randNumber = random.randint(1, 100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess  = int(input("Enter your guess between 1 and 100: "))
    guesses += 1
    if(userGuess == randNumber):
        print("You guessed the right number.")
    else:
        if(userGuess > randNumber): 
            print(f"You guessed it wrong! Enter a smaller number.")
        else:
            print(f"You guessed it wrong! Enter a larger number.")

print(f"You guesses the number in {guesses} guesses.")

with open("hiscore.txt", "r") as f:
    hiscore =  int(f.read()) 

if guesses < hiscore:
    print("You have broken the highest score!")    
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))

