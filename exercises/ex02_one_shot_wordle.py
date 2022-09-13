"""An advancement of the previous try to wordle!"""

__author__ = "730579095"

"""These are the stored constants available for the ease of concatenation to the final string output"""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

"""Variable that stores the secret word"""
secret_word: str = "python"

"""Variable that stores the guess of the user that will be compared to the secret word"""
guessed_word: str = input(f"What is your {len(secret_word)}-letter guess? ")

"""This while loop allows us to keep requesting the user to change their word to a word that is the same length to the secret word"""
while len(guessed_word) != len(secret_word):
    guessed_word = input(f"That was not {len(secret_word)} letters! Try again: ")

"""current_index is the variable name that I will use to loop through the string"""
current_index: int = 0

"""final_wordle_output is the variable name that I will use to store the final output of emojis"""
final_wordle_output: str = ""

"""I am using this variable to see whether the user got it correct or not"""
correct_green_count: int = 0

"""This while loop is responsible for concatenating the specific emojis based off the rules of wordle"""
while current_index < len(secret_word):
    """temporary_counter is the variable that will be responsible for looping through
       the secret word over again. I needed a independent loop variable other than the 
       over encompassing loop counter current_index. temporary_counter helps me add the 
       yellow emojis to the final output."""
    temporary_counter: int = 0
    """I will explain the specific uses of this variable in the below nested while loop. 
       I use this variable to store the count of the number of letters found in
       the secret word"""
    letter_count: int = 0
    """This if statment simply just checks if the index we are checking currently is equal to the corresponding index in the secret word"""
    if guessed_word[current_index] == secret_word[current_index]:
        final_wordle_output += f"{GREEN_BOX}"
        correct_green_count += 1
    else:
        """This while loops utilizes a new counter and loop variable. We do this to check if the 
           current index in our guessed word has more than one occurrence in the secret word. We
           loop through the established secret word and for every occurrence we add one to letter_count"""
        while temporary_counter < len(secret_word):
            if guessed_word[current_index] == secret_word[temporary_counter]:
                letter_count += 1
            temporary_counter += 1
        """If letter count is greater than one, we add a yellow box at this specific point in the 6 letters"""
        if letter_count >= 1:
            final_wordle_output += f"{YELLOW_BOX}"
        else:
            """If the letter count is less than one, we add a white box."""
            final_wordle_output += f"{WHITE_BOX}"
    current_index += 1

print(final_wordle_output)
if correct_green_count == 6:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")