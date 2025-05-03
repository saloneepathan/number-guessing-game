from art import logo
import random


print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")


def generate_random_number():
    """Generates a random number between 1 and 100."""
    return random.randint(1, 100)

def set_difficulty():
    """Sets the difficulty level and returns the number of attempts."""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:   
        print("Invalid input. Please choose 'easy' or 'hard'.")
        exit()
    return attempts

def check_guess(guess, answer, attempts):
    """Checks the user's guess against the answer and returns the number of attempts left."""
    if guess > answer:
        print("Too high.")
        return attempts - 1
    elif guess < answer:
        print("Too low.")
        return attempts - 1
    else:
        print(f"Congratulations! You guessed the number {answer} correctly!")
        return 0

def play_game():
    """Main function to play the number guessing game."""
    answer = generate_random_number()
    attempts = set_difficulty()
    guess = 0

    while guess != answer and attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_guess(guess, answer, attempts)

        if attempts == 0:
            print(f"You've run out of guesses. The number was {answer}.")
            break


if __name__ == "__main__":
    play_game()
    while input("Do you want to play again? Type 'y' or 'n': ").lower() == 'y':
        print("\n" + logo)
        play_game()
# The code is a simple number guessing game where the user has to guess a randomly generated number between 1 and 100.