import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    play_again = True

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    while play_again:
        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                    break
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 100.")

        while True:
            replay = input("Do you want to play again? (yes/no): ").strip().lower()
            if replay == "yes":
                number_to_guess = random.randint(1, 100)
                attempts = 0
                break
            elif replay == "no":
                play_again = False
                print("Thanks for playing! Goodbye.")
                break
            else:
                print("Invalid input! Please type 'yes' or 'no'.")

guessing_game()
