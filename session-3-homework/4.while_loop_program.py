# Program B: Number Guessing Game
# Logic: We use 'while' because we don't know how many tries the user will take.

secret_number = 7
guess = 0

print("I'm thinking of a number between 1 and 10. Can you guess it?")

# The loop continues as long as the guess is NOT equal to the secret number
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You found it!")

# Why a while loop? 
# It's perfect when the number of repetitions depends on a condition (the correct answer), not a fixed count.