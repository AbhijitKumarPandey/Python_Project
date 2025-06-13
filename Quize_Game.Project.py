import time

# Define questions level-wise: Python, Java, DSA
quiz = {
    "easy": {
        "1. What is the keyword to define a function in Python?": {
            "options": ["A. func", "B. define", "C. def", "D. function"],
            "answer": "C"
        },
        "2. Which of these is a valid Python data type?": {
            "options": ["A. int", "B. decimal", "C. number", "D. real"],
            "answer": "A"
        },
        "3. How do you write a comment in Python?": {
            "options": ["A. //", "B. <!-- -->", "C. #", "D. /**/"],
            "answer": "C"
        },
        "4. What does the `len()` function do?": {
            "options": ["A. Find length", "B. Convert to integer", "C. Print value", "D. Create list"],
            "answer": "A"
        },
        "5. Which of the following is used to import modules in Python?": {
            "options": ["A. using", "B. include", "C. import", "D. load"],
            "answer": "C"
        }
    },
    "medium": {
        "1. Which keyword is used to create a class in Java?": {
            "options": ["A. define", "B. new", "C. class", "D. struct"],
            "answer": "C"
        },
        "2. Which method is the entry point of a Java program?": {
            "options": ["A. start()", "B. main()", "C. run()", "D. init()"],
            "answer": "B"
        },
        "3. What is the extension of Java bytecode files?": {
            "options": ["A. .java", "B. .class", "C. .exe", "D. .byte"],
            "answer": "B"
        },
        "4. Which of these is not a primitive data type in Java?": {
            "options": ["A. int", "B. boolean", "C. String", "D. float"],
            "answer": "C"
        },
        "5. What is the size of `int` in Java?": {
            "options": ["A. 2 bytes", "B. 4 bytes", "C. 8 bytes", "D. Depends on system"],
            "answer": "B"
        }
    },
    "hard": {
        "1. Which data structure uses FIFO order?": {
            "options": ["A. Stack", "B. Queue", "C. Tree", "D. Graph"],
            "answer": "B"
        },
        "2. What is the time complexity of binary search in a sorted array?": {
            "options": ["A. O(n)", "B. O(log n)", "C. O(n log n)", "D. O(1)"],
            "answer": "B"
        },
        "3. Which sorting algorithm is fastest on average?": {
            "options": ["A. Bubble Sort", "B. Insertion Sort", "C. Merge Sort", "D. Quick Sort"],
            "answer": "D"
        },
        "4. Which data structure uses LIFO?": {
            "options": ["A. Queue", "B. Stack", "C. Tree", "D. Graph"],
            "answer": "B"
        },
        "5. What is the height of a balanced binary tree with n nodes?": {
            "options": ["A. O(n)", "B. O(log n)", "C. O(1)", "D. O(n log n)"],
            "answer": "B"
        }
    }
}

# Start Quiz
print("===== Welcome to the Programming Quiz Game =====")
name = input("Enter your name: ")

print("\nChoose Level:\n1. Easy (Python)\n2. Medium (Java)\n3. Hard (DSA)")
level_choice = input("Enter level number (1/2/3): ")

# Map input to level
levels = {"1": "easy", "2": "medium", "3": "hard"}
level = levels.get(level_choice)

if not level:
    print("Invalid level selected. Exiting.")
    exit()

questions = quiz[level]
score = 0
start_time = time.time()

# Ask questions
for q, data in questions.items():
    print("\n" + q)
    for opt in data["options"]:
        print(opt)
    user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

    if user_answer == data["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f" Wrong! Correct answer: {data['answer']}")

end_time = time.time()
total_time = round(end_time - start_time, 2)

# Save to file
with open("score.txt", "a") as file:
    file.write(f"Name: {name} | Level: {level.title()} | Score: {score}/{len(questions)} | Time: {total_time}s\n")

# Show result
print(f"\n🎯 {name}, your score in {level.title()} level is {score}/{len(questions)}")
print(f"⏱️ Time taken: {total_time} seconds")
print("📝 Your result has been saved in 'score.txt'")

# Feedback
if score == len(questions):
    print("🏆 Brilliant! Full marks!")
elif score >= 3:
    print("👍 Good job!")
else:
    print("📘 Keep practicing!")
