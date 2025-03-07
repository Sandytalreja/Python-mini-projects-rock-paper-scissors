import random

# Define emojis for choices
emoji = {'rock': '🪨', 'paper': '📃', 'scissors': '✂️'}
choices = ('rock', 'paper', 'scissors')


# Function to determine the winner
def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie!"
    elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'scissors' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You Win!"
    else:
        return "You Lose!"


# Function to play a single round
def play_round(user_choice):
    if user_choice not in choices:
        return {"error": "Invalid choice. Please select rock, paper, or scissors."}

    computer_choice = random.choice(choices)
    result = get_winner(user_choice, computer_choice)
    return {
        "user": emoji[user_choice],
        "computer": computer_choice,
        "result": result
    }


# Function for testing in terminal (Not needed for Flask)
def play_game():
    while True:
        user_choice = input("Rock, Paper, or Scissors? (rock/paper/scissors): ").lower()
        if user_choice not in choices:
            print("Invalid choice. Try again.")
            continue

        # Play a round
        round_result = play_round(user_choice)

        # Display result
        print(f"You chose {round_result['user']}")
        print(f"Computer chose {round_result['computer']}")
        print(round_result['result'])

        # Ask if the user wants to play again
        should_continue = input("Play again? (y/n): ").lower()
        if should_continue == 'n':
            break

# Uncomment the line below only if testing in terminal (not for Flask)
# play_game()
