import random  # Imports the random library for generating random numbers

# Initialize variables
count = 0  # Keeps track of the player's score
game = False  # Tracks if the current game is over
go_again = False  # Tracks if the user wants to play another game

# Open data file and import celebrity data
f1 = open("H_L_game_data.py", 'r')
from H_L_game_data import data  

# Open art file and import game art
f2 = open("H_L_game_art.py", 'r')
from H_L_game_art import logo, vs  # Logo and separator used in the game

# Main game loop
while not go_again:

    win = False  # Tracks if the player guessed correctly in the current round

    # Print the game logo
    print(logo)

    # Game loop for each round
    while not game:

        if not win:
            # Choose a random celebrity (avoid duplicates in consecutive rounds)
            current_celebrity = random.randint(0, 49)
            win = False  # Reset win flag for the new round

            # Display information about the chosen celebrity (celebrity A)
            print(f"Who do you think has more followers on Instagram?")
            print(f"A - {data[current_celebrity]['name']}, a {data[current_celebrity]['description']}, from {data[current_celebrity]['country']}.")

            # Display separator between celebrities
            print(vs)

            # Choose another random celebrity (avoid celebrity A and duplicates)
            other_celebrity = random.randint(0, 49)
            if other_celebrity == current_celebrity:
                other_celebrity += 1  # Ensure it's a different celebrity

            # Display information about the second celebrity (celebrity B)
            print(f"B - {data[other_celebrity]['name']}, a {data[other_celebrity]['description']}, from {data[other_celebrity]['country']}.")

            # Get user's guess (A or B)
            user_guess = input("Type 'A' or 'B': ").lower()

        # Check user's guess
        if user_guess == "a":
            # Check if celebrity A has more followers
            if data[current_celebrity]["follower_count"] > data[other_celebrity]["follower_count"]:
                count += 1  # Increase score if guess is correct
                print(f"Correct! Your current score is {count}")
                current_celebrity = other_celebrity  # Update current celebrity for next round
                win = True  # Set win flag for the round
            else:
                game = True  # End the game if guess is wrong

        elif user_guess == "b":
            # Check if celebrity B has more followers
            if data[other_celebrity]["follower_count"] > data[current_celebrity]["follower_count"]:
                count += 1  # Increase score if guess is correct
                print(f"Correct! Your current score is {count}")
                current_celebrity = other_celebrity  # Update current celebrity for next round
                win = True  # Set win flag for the round
            else:
                game = True  # End the game if guess is wrong

        else:
            game = True  # End the game if invalid input

    # Display message for wrong guess and final score
    print("Wrong!")
    print(f"Your final score: {count}")

    # Ask user if they want to play again
    play_again = input("Want to play again? Type 'y' for yes and 'n' for no: ").lower()
    if play_again == "y":
        count = 0  # Reset score for new game
        game = False  # Reset game state
        print("\033[H\033[J")  # Clear the screen for a new game
    elif play_again == "n":
        go_again = True  # Exit the main game loop
