import random;

choice_options = ["rock", "paper", "scissors"]

def get_player_choice():
    print("Enter your choice: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            return "rock"
        if choice == "2":
            return "paper"
        if choice == "3":
            return "scissors"
        print("Invalid choice. Please enter 1, 2 or 3.")

def get_computer_choice():
    return random.choice(choice_options)


def get_choices():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    return {
        "player_choice": player_choice,
        "computer_choice": computer_choice,
    }

def get_winner(choices):
    player_choice = choices["player_choice"]
    computer_choice = choices["computer_choice"]

    print(f"Player choice: {player_choice}")
    print(f"Computer choice: {computer_choice}")

    if player_choice == computer_choice:
        return "It's a tie!"

    if player_choice == "rock":
        if computer_choice == "scissors":
            return "Player wins!"
        return "Computer wins!"

    if player_choice == "paper":
        if computer_choice == "rock":
            return "Player wins!"
        return "Computer wins!"

    if player_choice == "scissors":
        if computer_choice == "paper":
            return "Player wins!"
        return "Computer wins!"

print("The winner is: ", get_winner(get_choices()))



