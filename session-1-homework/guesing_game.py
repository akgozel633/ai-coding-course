import random

def guessing_game():
    print("--- Guessing Game ---")
    print("I'm thinking of a number between 1 and 100.")
    
    # The computer picks a random number
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = input("Enter your guess (or 'exit' to quit): ")
            
            if guess.lower() == 'exit':
                print(f"Game over. The number was {secret_number}.")
                break
            
            guess = int(guess)
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You found it in {attempts} attempts!")
                break
                
        except ValueError:
            print("Please enter a valid whole number.")

if __name__ == "__main__":
    guessing_game()
