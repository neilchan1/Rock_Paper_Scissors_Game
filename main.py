import random
from ascii_art import ROCK, PAPER, SCISSORS

GESTURES = {
    0: ('Rock', ROCK),
    1: ('Paper', PAPER),
    2: ('Scissors', SCISSORS)
}

def introduction():
    print("Welcome to Rock, Paper, Scissors!\n")
    print("################# RULES #################")
    print("- Rock crushes scissors (rock wins).\n- Scissors cuts paper (scissors wins).\n- Paper covers rock (paper wins).\n")
    print("Your options: 0 = Rock, 1 = Paper, 3 = Scissors\n")

def main():
    introduction()

    try:
        player_choice = int(input("What do you choose?\n"))

        if player_choice not in GESTURES:
            raise ValueError("Invalid choice.")
        
        computer_choice = random.randint(0, 2)

        reveal_player_choice('PLAYER', player_choice)
        reveal_player_choice('COMPUTER', computer_choice)

        result = determine_winner(player_choice, computer_choice)

        return_outcome(result)
        print("\nThanks for playing!")
    except ValueError as e:
        print(f"{e}\nPlease enter 0, 1, or 2, next time!")

def reveal_player_choice(player, choice):
    gesture, art = GESTURES[choice]

    print(f"{player} chose {gesture}:\n{art}")

def determine_winner(player, computer):
    if player == computer:
        return "DRAW"
    elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
        return "WIN"
    else:
        return "LOSE"
    
def return_outcome(result):
    if result == "DRAW":
        print("It's a DRAW!")
    elif result == "WIN":
        print("You WIN!")
    else:
        print("You LOSE!\nBetter luck next time.")

if __name__ == "__main__":
    main()