import random

# Function 1: Gets the computer's choice randomly
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function 2: Gets and validates player input
def get_player_choice():
    # Loop inside function to keep asking until input is valid
    while True:
        choice = input("Enter rock, paper, or scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please try again.")

# Function 3: Decides the winner of a single round
def determine_winner(player, computer):
    # If/Else logic to determine the result
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

# Function 4: Manages the game flow and score
def play_tournament():
    player_score = 0
    computer_score = 0
    rounds_to_win = 3
    
    print(f"Welcome to the Tournament! First to {rounds_to_win} wins!")

    # Loop that calls other functions
    while player_score < rounds_to_win and computer_score < rounds_to_win:
        p_choice = get_player_choice()
        c_choice = get_computer_choice()
        
        print(f"Computer chose: {c_choice}")
        
        result = determine_winner(p_choice, c_choice)
        
        if result == "player":
            player_score += 1
            print(f"You win this round! Score: You {player_score} - {computer_score} AI")
        elif result == "computer":
            computer_score += 1
            print(f"AI wins this round! Score: You {player_score} - {computer_score} AI")
        else:
            print(f"It's a tie! Score remains: {player_score} - {computer_score}")
    
    # Final Result
    if player_score == rounds_to_win:
        print("\nCONGRATULATIONS! You won the tournament!")
    else:
        print("\nGAME OVER. The AI won the tournament.")

# Main program - clean and simple
if __name__ == "__main__":
    play_tournament()