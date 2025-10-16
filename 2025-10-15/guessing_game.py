'''
Exercise: Number Guessing Game

Write function templates for a number guessing game:

- guessing_game: This is the main function. It should set a secret number and manage the game loop, asking the user for guesses until the correct number is guessed.
- get_user_guess: This function should ask the user for a guess and return it as an integer.
- check_guess: This function should take the user's guess and the secret number, and return feedback as a string ("low", "high", or "correct").
'''

def guessing_game():
    secret_number = 26 # You can randomize later if needed.
    feedback = None
    while feedback != "Correct":
        guess = get_user_guess()
        feedback = check_guess(guess, secret_number)
        print(feedback)
    print(f"Congratulations! The number was indeed {secret_number}!")

def get_user_guess():
    n = int(input("Enter an integer: "))
    return n

def check_guess(guess, secret_number):
    if guess < secret_number:
        return "Low"
    elif guess > secret_number:
        return "High"
    else:
        return "Correct"