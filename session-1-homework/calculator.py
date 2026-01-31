def calculator():
    print("--- Simple Python Calculator ---")
    print("Available operations: +, -, *, /")
    print("Type 'exit' to close the program.")

    while True:
        try:
            # Get user input
            user_input = input("\nEnter expression (e.g., 10 + 5) or 'exit': ").lower()
            
            if user_input == 'exit':
                print("Goodbye!")
                break

            # Split the input into parts (number1, operator, number2)
            parts = user_input.split()
            
            if len(parts) != 3:
                print("Error! Please use spaces: 10 + 5")
                continue

            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])

            # Calculation logic
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    continue
                result = num1 / num2
            else:
                print("Error: Unknown operator!")
                continue

            # Check if result is a whole number to keep output clean
            if result.is_integer():
                print(f"Result: {int(result)}")
            else:
                print(f"Result: {result}")

        except ValueError:
            print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
