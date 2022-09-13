"""Final wordle console edition"""

__author__ = "730579095"


def contains_char(target_string: str, target_char: str) -> bool:
    """This function returns a boolean based on whether a given character is in a given string. This function loops
       through the string to see whether the character exists in the string. If so, it returns true, elase it returns false."""
    assert len(target_char) == 1
    loop_counter: int = 0
    while loop_counter < len(target_string):
        if target_string[loop_counter] == target_char:
            return True
        loop_counter += 1
    return False

def emojified(guess_string: str, secret_string: str) -> str:
    """This function returns a emoji version of the wordle game we coded in the last exercise."""
    assert len(guess_string) == len(secret_string)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    current_index: int = 0
    final_wordle_output: str = ""
    while current_index < len(secret_string):
        temporary_counter: int = 0
        letter_count: int = 0
        if guess_string[current_index] == secret_string[current_index]:
            final_wordle_output += f"{GREEN_BOX}"
        elif contains_char(secret_string, guess_string[current_index]):
            final_wordle_output += f"{YELLOW_BOX}"
        else:
            final_wordle_output += f"{WHITE_BOX}"
        current_index += 1
    return final_wordle_output

def input_guess(word_len: int) -> str:
    """This function prompts a user for a word of desired length. If they input a word of different length, they are prompted continuously"""
    guessed_word: str = input(f"What is your {word_len}-letter guess? ")
    while len(guessed_word) != word_len:
        guessed_word = input(f"That was not {word_len} letters! Try again: ")
    return guessed_word

def main() -> None:
    """The entrypoint of the program and main game loop."""
    user_attempts: int = 0
    guessed_string: str = ""
    while user_attempts < 6:
        print(f"=== Turn {user_attempts+1}/6 ===")
        guessed_string = input_guess(5)
        print(emojified(guessed_string, "codes"))
        if guessed_string == "codes":
            print(f"You won in {user_attempts+1}/6 turns!")
            return None
        user_attempts += 1
    print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()

