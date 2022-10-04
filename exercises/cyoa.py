"""This game simulates you playing rock,paper,scissors"""

__author__ = "730579095"

import random

ROCK_EMOJI = "\U0001F44A"
PAPER_EMOJI = "\U0001F91A"
SCISSOR_EMOJI = "\U0001F596"
player: str = ""
points: int
CHOICES: list[str] = ["Rock", "Paper", "Scissors"]

def greet() -> None:
    global player
    player = input("Nice to meet you! What's your name?: ")
    print(f"Hey {player} how are you? Let's play play rock{ROCK_EMOJI}, paper{PAPER_EMOJI}, scissors{SCISSOR_EMOJI}")

import random


def play_rps() -> None:
    global points
    player_choice: str = input(f"Thanks for choosing to play rock, paper, scissors with me {player}! What do you choose? ('Rock' {ROCK_EMOJI}, 'Paper' {PAPER_EMOJI}, 'Scissors' {SCISSOR_EMOJI}): ")
    points += 1
    while player_choice not in "RockPaperScissors":
        player_choice = input(f"Please choose 'Rock', 'Paper', or 'Scissors': ")
    computer_choice: str = random.choice(CHOICES)
    while player_choice == computer_choice:
        player_choice = input(f"NOO, we picked the same thing, will you pick again?: ('Rock' {ROCK_EMOJI}, 'Paper' {PAPER_EMOJI}, 'Scissors' {SCISSOR_EMOJI}): ")
        computer_choice = random.choice(CHOICES)  
    if player_choice == "Rock" and computer_choice == "Scissors":
        print(f";( you won, I chose {computer_choice}")
        points += 5
    elif player_choice == "Paper" and computer_choice == "Rock":
        print(f";( you won, I chose {computer_choice}")
        points += 5
    elif player_choice == "Scissors" and computer_choice == "Paper":
        print(f";( you won, I chose {computer_choice}")
        points += 5
    elif computer_choice == "Rock" and player_choice == "Scissors":
        print(f";( I won, I chose {computer_choice}")
        points -= 5
    elif computer_choice == "Paper" and player_choice == "Rock":
        print(f";( I won, I chose {computer_choice}")
        points -= 5
    elif computer_choice == "Scissors" and player_choice == "Paper":
        print(f";( I won, I chose {computer_choice}")
        points -= 5

def gamble_rps(gamble_amount: int) -> int:
    computer_gamble = gamble_amount + random.randint(10,100)
    print(f"Great, I will raise your gamble myself and bet {computer_gamble} points")
    player_choice: str = input(f"Thanks for gambling with me {player}! What do you choose? ('Rock' {ROCK_EMOJI}, 'Paper' {PAPER_EMOJI}, 'Scissors' {SCISSOR_EMOJI}): ")
    while player_choice not in "RockPaperScissors":
        player_choice = input(f"Please choose 'Rock', 'Paper', or 'Scissors': ")
    computer_choice: str = random.choice(CHOICES)
    while player_choice == computer_choice:
        player_choice = input(f"NOO, this is stressful, we picked the same thing, will you pick again?: ('Rock' {ROCK_EMOJI}, 'Paper' {PAPER_EMOJI}, 'Scissors' {SCISSOR_EMOJI}): ")
        computer_choice = random.choice(CHOICES)  
    if player_choice == "Rock" and computer_choice == "Scissors":
        print(f";( you won, I chose {computer_choice}")
        return computer_gamble
    elif player_choice == "Paper" and computer_choice == "Rock":
        print(f";( you won, I chose {computer_choice}")
        return computer_gamble
    elif player_choice == "Scissors" and computer_choice == "Paper":
        print(f";( you won, I chose {computer_choice}")
        return computer_gamble
    elif computer_choice == "Rock" and player_choice == "Scissors":
        print(f";( I won, I chose {computer_choice}")
        return -1*gamble_amount
    elif computer_choice == "Paper" and player_choice == "Rock":
        print(f";( I won, I chose {computer_choice}")
        return -1*gamble_amount
    elif computer_choice == "Scissors" and player_choice == "Paper":
        print(f";( I won, I chose {computer_choice}")
        return -1*gamble_amount


def main() -> None:
    global points
    points = 0
    greet()
    print("_____________________________")
    continue_choice = '1'
    while continue_choice in '12':
        print(f"Option 1: Play a normal game of rock{ROCK_EMOJI}, paper{PAPER_EMOJI}, scissors{SCISSOR_EMOJI}")
        print(f"Option 2: Gamble with rock{ROCK_EMOJI}, paper{PAPER_EMOJI}, scissors{SCISSOR_EMOJI}")
        print(f"Option 3: Exit and see how many adventure points you earned?")
        continue_choice = input(f"Would you like to play rock{ROCK_EMOJI}, paper{PAPER_EMOJI}, scissors{SCISSOR_EMOJI}? Choose an option from below ('1','2','3'): ")
        print("_____________________________")
        while continue_choice not in "123":
            continue_choice = input("Please chose '1', '2','3'")
            print("_____________________________")
        if continue_choice == "1":
            play_rps()
            print("_____________________________")
        elif continue_choice == "2":
            points += gamble_rps(int(input(f"How much will you gamble to me {player}?: ")))
            print("_____________________________")
        print(f"Number of points: {points}")
        print("_____________________________")
    print(f"You have earned {points} points, great job!")
    print("_____________________________")


if __name__ == "__main__":
  main()




