"""An advancement of the previous try to wordle"""

__author__ = "730579095"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

"""Variable that stores the secret word"""
secret_word: str = "python"
"""Variable that stores the guess of the user that will be compared to the secret word"""
guessed_word: str = input("What is your 6-letter guess? ")

while len(guessed_word) != 6:
    guessed_word = input("That was not 6 letters! Try again: ")

current_index: int = 0
final_wordle_output: str = ""

while current_index < len(secret_word):
    temporary_counter: int = 0
    letter_count: int = 0
    index_char_exists: bool = False
    if guessed_word[current_index] == secret_word[current_index]:
        final_wordle_output += f"{GREEN_BOX}"
    else:
        while temporary_counter < len(secret_word):
            if guessed_word[current_index] == secret_word[temporary_counter]:
                letter_count += 1
            temporary_counter += 1
        if letter_count >= 1:
            final_wordle_output += f"{YELLOW_BOX}"
        else:
            final_wordle_output += f"{WHITE_BOX}"
    current_index += 1

print(final_wordle_output)