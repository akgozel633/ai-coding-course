# Decision Maker: Study Method Selector

print("Welcome to the Study Method Selector!")
print("Answer a few questions, and I will tell you how to study today.")

# Requirement: Ask at least 3 questions
# We use .lower() to make sure the program understands "Yes" or "yes"
subject_type = input("Is the subject technical (math/science) or creative (art/writing)? ").lower()
time_available = int(input("How many minutes do you have? (Enter a number): "))
energy_level = input("Is your energy level high, medium, or low? ").lower()

# Requirement: Include at least one if, one elif, and one else
# Logic: Recommending a method based on energy and time
if energy_level == "high" and subject_type == "technical":
    # If energy is high and it's a hard subject, do the hardest task first
    result = "Use the 'Eat the Frog' method: Tackle your hardest math/science problems right now!"

elif energy_level == "low" or time_available < 30:
    # If energy is low OR time is short, use a quick burst method
    result = "Use the 'Pomodoro' technique: Study for 25 minutes, then take a 5-minute break."

else:
    # For all other cases (e.g., medium energy or creative subjects)
    result = "Try 'Active Recall': Quiz yourself or explain the topic to an imaginary friend."

# Final Output: Use the user's answers to give a result
print("\n--- Recommendation ---")
print(f"Based on your situation, here is my advice: {result}")