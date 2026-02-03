from datetime import datetime

# 1. Get current date
today = datetime.now()
date_string = today.strftime("%b %d, %Y")

# 2. Calculate future date (Challenge: 10 years later)
future_year = today.year + 10

# 3. Ask the questions
print("--- Creating Your Personal Time Capsule ---")
age = input("How old are you? ")
song = input("What is your current favorite song? ")
goal = input("What is your biggest goal for this year? ")
friend = input("Who is your best friend? ")
feeling = input("Describe your current mood in one word: ")

# 4. Format the content using f-strings
header = f"""
        ╔════════════════════════════════════╗
        ║         TIME CAPSULE - 2026        ║
        ║        Created: {date_string}        ║
        ╚════════════════════════════════════╝
"""

content = f"""
Current Age: {age}
Favorite Song: {song}
Biggest Goal: {goal}
Best Friend: {friend}
Current Vibe: {feeling}

--------------------------------------
To be opened in: {future_year}
"""

# 5. Save to file
file_name = "time_capsule_2026.txt"
with open(file_name, "w", encoding="utf-8") as file:
    file.write(header)
    file.write(content)

print(f"\nSuccess! Your time capsule has been saved to {file_name}")