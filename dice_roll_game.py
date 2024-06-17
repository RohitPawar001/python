from random import randint

def roll():
    min_value = 1
    max_value = 6
    return randint(min_value, max_value)

players = {}
try:
    player_no = int(input("How many players are playing (2-4)? "))
    dice_roll_time = int(input("Enter the number of iterations: "))
    if 2 <= player_no <= 4:
        for player in range(player_no):
            players[player] = 0  # Initialize player scores
            for _ in range(dice_roll_time):
                roll_dice = input("Do you want to roll the dice (y/n)? ").lower()
                if roll_dice == "y":
                    value = roll()
                    players[player] += value
                else:
                    break
            print(f"Player {player} has rolled all dice.")
        print("Game over! Final scores:")
        for i, score in players.items():
            print(f"Player {i}: {score}")
    else:
        print("Please enter a valid number of players (2-4).")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
