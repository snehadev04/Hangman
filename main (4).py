# Import the random module to generate a random word
import random

# Import the clear function from the replit module to clear the console screen
from replit import clear

# Import the ASCII art representations of hangman stages
from hangman_art import stages

# Import the word list for the game
from hangman_words import words

# Import the ASCII art representation of the game's logo
from hangman_art import logo

# Print the game's logo
print(logo)

# Choose a random word from the word list
choosen_word = random.choice(words)
print(choosen_word)

# Initialize the number of lives the player has
lives = 6

# Initialize an empty list to store the blanked version of the word
blanked_word = []

# Loop through the length of the chosen word to create the initial blanked word
for char in range(len(choosen_word)):
  blanked_word += "_"

# Initialize the end of the game flag
end_of_game = False

# Start the main game loop
while not end_of_game:

  # Prompt the player to guess a letter and convert it to lowercase
  guess_letter = input("Guess the letter: ").lower()

  # Clear the console screen
  clear()

  # Check if the guessed letter has already been guessed
  if guess_letter in blanked_word:
    print("You have already guessed it!")

  # Loop through the word to check if the guessed letter is correct
  for position in range(len(choosen_word)):  
    if choosen_word[position] == guess_letter:
      # If the guessed letter is correct, update the blanked word
      blanked_word[position] = choosen_word[position]

  # If the guessed letter is not in the word, decrement lives and check for game over
  if guess_letter not in choosen_word:
    print("Your guessed letter is not in the word. You lost a life!")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("Game over!")

  # Print the current state of the word with blanks
  print(" ".join(blanked_word))

  # Check if all letters have been guessed
  if "_" not in blanked_word:
    end_of_game = True
    print("You win!")

  # Print the current hangman stage based on remaining lives
  print(stages[lives])