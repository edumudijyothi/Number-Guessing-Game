import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guess = None

    # Debug print to verify the secret number
    print(f"Debug: The secret number is {secret_number}")

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    # Ask the player for the maximum number of attempts
    while True:
        try:
            max_attempts = int(input("Enter the maximum number of attempts: "))
            if max_attempts <= 0:
                print("The number of attempts must be a positive integer. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Loop until the correct guess or until the maximum number of attempts is reached
    while guess != secret_number and attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                print("Great job! Your perseverance and analytical skills paid off!")
                return  # Exit the function after the correct guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # If the maximum number of attempts is reached without a correct guess
    if guess != secret_number:
        print(f"Sorry, you've reached the maximum number of attempts. The number was {secret_number}.")
        print("Don't be discouraged! Every attempt is a step towards success. Keep trying, and you'll get there!")

# Start the game
number_guessing_game()
