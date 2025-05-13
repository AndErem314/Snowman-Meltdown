import random
from ascii_art import STAGES
from snowman import WORDS

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the snowman stage for the current number of mistakes."""
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word, "\n")


def play_game():
    """The main function using the gameplay loop"""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word,guessed_letters)

        # Check if player has won
        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You saved the snowman!")
            print(f"The word was: {secret_word}")
            return

        # Input validation loop
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1:
                print("Please enter only one character.")
            elif not guess.isalpha():
                print("Please enter a letter (a-z).")
            elif guess in guessed_letters:
                print("You have already guessed this letter. Try again.")
            else:
                break # exit the loop with valid input

        guessed_letters.append(guess)

        # Check guess
        if guess not in secret_word:
            mistakes += 1
            print("Incorrect! Snowman melts...")
        else:
            print("Correct!")

    # the condition if player lost
    display_game_state(mistakes, secret_word, guessed_letters)
    print("Oh no! The snowman melted completely!")
    print(f"The word was: {secret_word}")


