"""EX01 - Chardle - An attempt at Wordle."""

__author__ = "730579095"

"""five_character_word variable is used to store and hold the string that the user inputs to begin the program that will be compared with the single character"""
five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
"""the single_character variable stores the character that will be compared with all the characters in the variable five_character_word"""
single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()
"""the number_matches variable is used to store the number of instances where the character stored in single_character
is same as any of the characters in the five_character_word variable."""
number_matches: int = 0

print("Searching for " + single_character + " in " + five_character_word)

"""this if-then statment block manages the comparison of the character stored in the variable single_character to every single index character
#stored in the five_character_word"""
if single_character == five_character_word[0]:
    print(single_character + " found at index 0")
    number_matches += 1
if single_character == five_character_word[1]:
    print(single_character + " found at index 1")
    number_matches += 1
if single_character == five_character_word[2]:
    print(single_character + " found at index 2")
    number_matches += 1
if single_character == five_character_word[3]:
    print(single_character + " found at index 3")
    number_matches += 1
if single_character == five_character_word[4]:
    print(single_character + " found at index 4")
    number_matches += 1

"""this if-then statement block manages the printing the number_matches variable if there are any."""
if number_matches == 0:
    print("No instances of " + single_character + " found in " + five_character_word)
elif number_matches == 1:
    print(str(number_matches) + " instance of " + single_character + " found in " + five_character_word)
elif number_matches >= 2:
    print(str(number_matches))
