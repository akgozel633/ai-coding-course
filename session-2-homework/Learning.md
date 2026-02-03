# Python Learning Journey: Session 2 Homework

## 1. Reflections and Emotions
  The moment the program successfully generated a real `.txt` file on my desktop, I felt a  sense of accomplishment It’s exciting to see how code can interact with the computer's file system to save information . I really enjoyed the creative part of designing the "Time Capsule" layout and making the calculator look professional.

## 2. Coding Challenges & Bugs
* **The Date Format Trap:** I initially tried to hardcode the year inside the `strftime` function, which caused a `ValueError`. I learned that Python uses specific placeholders like `%Y` for years and `%B` for months.
* **Data Type Confusion:** In the Calculator task, I forgot that `input()` returns a string. I had to learn to wrap it in `float()` so the program could actually perform math instead of just joining text together.
* **Overwrite vs. Append:** I accidentally wiped my history file several times using the `'w'` mode. Switching to `'a'` (append) was a "Eureka!" moment for keeping a continuous log of my calculations.

## 3. Skills Mastered
* Using the `datetime` library to fetch and format system time.
* Implementing `f-strings` for advanced text alignment and limiting decimals using `:.2f`.
* Managing file I/O operations (Writing, Appending, and using `with` blocks).
* Working with **Lists** and **Dictionaries** to organize user data.
* Using the `random` module to add dynamic content.

---

## 4. AI Prompts Used for These Tasks

### Homework 1: Personal Time Capsule
* **English:** "Write a Python program that asks the user 5 personal questions and saves the answers to a file named 'time_capsule_2026.txt'. Use ASCII borders, f-strings for formatting, and include the current date using the datetime module."


### Homework 2: Calculator with Memory
* **English:** "Create a Python calculator that takes two numbers and displays the results of addition, subtraction, multiplication, and division. The program must append each calculation to a file named 'calculator_history.txt' including a timestamp for each entry."


### Homework 3: Choose Your Own Adventure (Goals Tracker)
* **English:** "Write a Python program that asks the user for 3 weekly goals, stores them in a list, and saves them to a file with checkboxes [ ]. Add a random motivational quote at the top of the file using the random module."
