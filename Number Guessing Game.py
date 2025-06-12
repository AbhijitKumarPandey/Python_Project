import random
import time
import os

print("🎯 Welcome to the Number Guessing Game Pro!")
name = input("Enter your name: ")

# Define level settings
levels = {
    "1": {"name": "Easy", "range": 20, "attempts": 5},
    "2": {"name": "Medium", "range": 100, "attempts": 7},
    "3": {"name": "Hard", "range": 1000, "attempts": 10}
}

# Level selection
print("\nSelect Difficulty Level:")
print("1. Easy (1-20)     [5 attempts]")
print("2. Medium (1-100)  [7 attempts]")
print("3. Hard (1-1000)   [10 attempts]")
level_choice = input("Enter level (1/2/3): ")

if level_choice not in levels:
    print("❌ Invalid level selected. Exiting.")
    exit()

level_data = levels[level_choice]
number = random.randint(1, level_data["range"])
max_attempts = level_data["attempts"]
attempts = 0

print(f"\n{name}, I'm thinking of a number between 1 and {level_data['range']}")
print(f"You have {max_attempts} attempts. Good luck!")

start_time = time.time()

while attempts < max_attempts:
    try:
        guess = int(input(f"\nAttempt {attempts + 1}: Enter your guess: "))
        attempts += 1

        if guess < number:
            print("📉 Too low!")
        elif guess > number:
            print("📈 Too high!")
        else:
            print(f"\n🎉 Correct! You guessed the number in {attempts} attempts.")
            break
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

end_time = time.time()
time_taken = round(end_time - start_time, 2)

# Check if player lost
if guess != number:
    print(f"\n😢 You've used all {max_attempts} attempts. The number was {number}.")

# Save result
with open("guess_score.txt", "a") as file:
    file.write(f"{name} | Level: {level_data['name']} | Attempts: {attempts} | Time: {time_taken}s\n")

print(f"\n📝 Your result has been saved in 'guess_score.txt'")
print(f"⏱️ Time taken: {time_taken} seconds")
 
print("\n🏆 Leaderboard (Top Scores):")
if os.path.exists("guess_score.txt"):
    with open("guess_score.txt", "r") as file:
        scores = file.readlines()

    def extract_score(line):
        parts = line.strip().split("|")
        attempts = int(parts[2].split(":")[1].strip())
        time_part = float(parts[3].split(":")[1].strip().replace("s", ""))
        return (attempts, time_part)

    top_scores = sorted(scores, key=extract_score)[:5]

    for idx, line in enumerate(top_scores, start=1):
        print(f"{idx}. {line.strip()}")
else:
    print("No leaderboard data found.")
