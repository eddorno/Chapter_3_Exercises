# Write the pseudocode for a program where the player and the computer trade places in 
# the number guessing game. That is, the player picks a random number between 1 and 100 
# that the computer has to guess. Before you start, think about how you guess. If all goes 
# well, try coding the game. 

# 1. prompt user for integer input between 1 and 100
# 2. use the random method to assign a number from 1 to 100 and compare to the users number
# 3. if the number is higher or lower, computer selects new number accordingly

import random

# set the initial values
the_number = int(input("Choose a number between 1 and 100: "))
guess = random.randint(1, 100)
tries = 1

# guessing loop
while guess != the_number:

    if guess > the_number:
        print("The guess was", guess)
        print("Lower...")
        guess = random.randint(1, guess)
    else:
        print("The guess was", guess)
        print("Higher...")
        guess = random.randint(guess, 100)
            
    tries += 1

print("You guessed it!  The number was", the_number)
print("And it only took you", tries, "tries!\n")

input("\n\nPress the enter key to exit.")