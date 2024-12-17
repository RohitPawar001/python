from guess_number import user_guess

print("Welcome to the number guessing game")
user_input = input("Do you want to play the game (yes/no): ")

if user_input.lower() == "yes":
    print("hi")
    user_guess.GuessNumber().guess()
else:
    print("Thank you")
    quit()
