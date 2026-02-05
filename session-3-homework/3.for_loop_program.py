# Program A: Multiplication Table Generator
# Logic: We use a 'for' loop because we know exactly how many steps we need (1 to 10).

number = int(input("Enter a number to see its multiplication table: "))

print(f"\nMultiplication Table for {number}:")

# The range(1, 11) generates numbers from 1 to 10
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

# Why a for loop? 
# It's best here because we have a fixed range of numbers to go through.