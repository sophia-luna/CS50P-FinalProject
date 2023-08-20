# 7 Lives
## Classic hangman game reimagined
This code is a Python program that implements a game where the player has to guess a word chosen by the Grim Reaper character. The player starts with 7 lives and loses a life each time they guess a wrong letter. If the player guesses the word correctly within the given number of lives, they win the game and can cross the bridge. Otherwise, if the player runs out of lives, it's game over.

The program uses the random module to select a word from predefined lists based on the chosen level of difficulty. It also utilizes the pyfiglet library to create ASCII art for various characters and messages displayed during the game.

The program starts by asking for the player's nickname and then presents an introduction to set the context of the game. It prompts the player to choose whether they want to play or not. If the player chooses to play, they are then asked to select a difficulty level. The game progresses by repeatedly asking the player to guess letters until they either guess the word correctly or run out of lives.

The gameOver() and win() functions handle the game outcomes, displaying appropriate messages and ASCII art. The check() function checks the player's guess against the chosen word and updates the word accordingly. The acceptGuess() and acceptLevel() functions validate the user input for guesses and difficulty level, respectively.

The remaining functions are responsible for displaying ASCII art for various characters and messages.

### CS50P Final Project
CS50's Introduction to Programming with Python