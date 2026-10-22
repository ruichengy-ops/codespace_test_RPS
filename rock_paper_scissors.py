import random


CHOICES = ("rock", "paper", "scissors")


def get_result(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"

    winning_pairs = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }
    if winning_pairs[player_choice] == computer_choice:
        return "win"
    return "lose"


def main():
    print("Rock, Paper, Scissors")
    print("Choose rock, paper, or scissors. Enter q to quit.\n")

    wins = 0
    losses = 0
    ties = 0

    while True:
        player_choice = input("Your choice: ").strip().lower()

        if player_choice in ("q", "quit"):
            break
        if player_choice not in CHOICES:
            print("Please enter rock, paper, scissors, or q.\n")
            continue

        computer_choice = random.choice(CHOICES)
        result = get_result(player_choice, computer_choice)

        print(f"Computer chose {computer_choice}.")
        if result == "win":
            wins += 1
            print("You win!")
        elif result == "lose":
            losses += 1
            print("You lose!")
        else:
            ties += 1
            print("It's a tie!")

        print(f"Score: {wins} wins, {losses} losses, {ties} ties\n")

    print(f"Final score: {wins} wins, {losses} losses, {ties} ties.")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()