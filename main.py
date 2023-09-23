import os
def clear_screen():
    os.system('cls')

import random
end_of_game = False

from Hangman_words import word_list

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

# This will count the number of letters and print the same number of blanks
length = len(chosen_word)

# Create a variable called 'lives' to keep track of the number of lives left. 
# Set 'lives' to equal 6.
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
from Hangman_art import logo
print (logo)

# To import the stages
from Hangman_art import stages

# Create blanks
display = []
for _ in range(length):
    display += "_"

# To give user option to input till blanks are left
while not end_of_game:
    
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()
    
    clear_screen()
    
    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    # Loop through each position in the chosen_word;
    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for position in range(length):
        letter = chosen_word[position]
        # print(f"Current positon: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    
    #Check if user is wrong.
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    
    # If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1. 
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
            
    # Join all the elements in the list and trun it into a Sring.
    print(f"{' '.join(display)}")
    
    # To check if _ are over to end the game
    if "_" not in display:
        end_of_game = True
        print("\nYou win!")
    
    # Print the ASCII art from 'Stage' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

# Solution
print(f'Pssst, the word is {chosen_word}.')