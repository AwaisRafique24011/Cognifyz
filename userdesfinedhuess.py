import random

def number_guesser():
    play_again = True

    print("Welcome to the Number Guesser!")

    while play_again:
        while True:
            try:
                lower_bound = int(input("Enter the lower bound of the range: "))
                upper_bound = int(input("Enter the upper bound of the range: "))

                if lower_bound >= upper_bound:
                    print("Invalid range! The upper bound must be greater than the lower bound.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter valid integers for the range.")

        number_to_guess = random.randint(lower_bound, upper_bound)
        attempts = 0

        print(f"I'm thinking of a number between {lower_bound} and {upper_bound}. Can you guess what it is?")

        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                # Check if the guess is within the specified range
                if guess < lower_bound or guess > upper_bound:
                    print(f"Your guess is out of range! Please enter a number between {lower_bound} and {upper_bound}.")
                elif guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                    break
            except ValueError:
                print(f"Invalid input! Please enter a number between {lower_bound} and {upper_bound}.")

        while True:
            replay = input("Do you want to play again? (yes/no): ").strip().lower()
            if replay == "yes":
                break
            elif replay == "no":
                play_again = False
                print("Thanks for playing! Goodbye.")
                break
            else:
                print("Invalid input! Please type 'yes' or 'no'.")

number_guesser()
