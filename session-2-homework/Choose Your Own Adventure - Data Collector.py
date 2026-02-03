import random
from datetime import datetime

# 1. Setup Data
quotes = [
    "Believe you can and you're halfway there.",
    "Don't stop until you're proud.",
    "Small steps lead to big results.",
    "Focus on being productive, not busy."
]

goals = []

# 2. Collect Data
print("--- 📝 Weekly Goals Tracker ---")
print("Enter 3 goals for your week:")

for i in range(1, 4):
    goal = input(f"Goal {i}: ")
    goals.append(goal)

# 3. Get metadata
today = datetime.now().strftime("%B %d, %Y")
motivational_quote = random.choice(quotes)

# 4. Prepare File Content
file_name = "weekly_goals.txt"

with open(file_name, "w", encoding="utf-8") as file:
    # Header
    file.write("========================================\n")
    file.write(f"      WEEKLY GOALS - {today}\n")
    file.write("========================================\n")
    file.write(f"Quote of the week: \"{motivational_quote}\"\n\n")
    
    # Loop through the list to add checkboxes
    file.write("YOUR TASKS:\n")
    for item in goals:
        file.write(f" ☐ {item}\n")
    
    file.write("\n========================================\n")

print(f"\nSuccess! Your goals have been saved to {file_name}")