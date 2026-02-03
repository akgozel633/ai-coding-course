from datetime import datetime

# 1. Get current timestamp
# %I:%M %p gives time like 03:45 PM
now = datetime.now()
timestamp = now.strftime("%b %d, %Y - %I:%M %p")

# 2. Get numbers from the user
print("--- Python Calculator with Memory ---")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# 3. Perform calculations
add = num1 + num2
sub = num1 - num2
mul = num1 * num2

# Handle division by zero just in case
if num2 != 0:
    div = num1 / num2
    div_text = f"{num1} ÷ {num2} = {div:.2f}"
else:
    div_text = f"{num1} ÷ {num2} = Error (Division by zero)"

# 4. Format results for display and file
history_entry = f"""
[{timestamp}]
{num1} + {num2} = {add}
{num1} - {num2} = {sub}
{num1} × {num2} = {mul}
{div_text}
---"""

# 5. Print results to console
print(history_entry)

# 6. Save to file (Append mode 'a')
with open("calculator_history.txt", "a", encoding="utf-8") as file:
    file.write(history_entry + "\n")

print("\nCalculation saved to calculator_history.txt")