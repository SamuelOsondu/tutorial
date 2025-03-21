# Quiz questions stored in a list of dictionaries
quiz = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ("A) func", "B) def", "C) function", "D) define"),
        "answer": "B"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ("A) List", "B) Dictionary", "C) Tuple", "D) Set"),
        "answer": "C"
    },
    {
        "question": "How do you insert an element at the end of a list?",
        "options": ("A) append()", "B) insert()", "C) add()", "D) push()"),
        "answer": "A"
    },
    {
        "question": "What is the output of 2 ** 3 in Python?",
        "options": ("A) 6", "B) 8", "C) 9", "D) 12"),
        "answer": "B"
    },
    {
        "question": "Which of these is used to handle exceptions in Python?",
        "options": ("A) try-except", "B) if-else", "C) for-while", "D) switch-case"),
        "answer": "A"
    }
]


# Function to conduct the quiz
def start_quiz():
    score = 0
    print("🧠 Welcome to the Python Quiz! 🧠\n")

    # Loop through each question
    for i, q in enumerate(quiz, start=1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(option)

        # Get user's answer
        answer = input("Your answer (A, B, C, or D): ").strip().upper()

        # Check if the answer is correct
        if answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was {q['answer']}.\n")

    # Display final score
    print(f"Your final score is {score} out of {len(quiz)}")
    if score >= 4:
        print("🎉 Excellent! You're a Python pro! 🎉")
    elif score >= 2:
        print("😊 Good job! Keep learning. 😊")
    else:
        print("😔 Don't worry, practice makes perfect! 😔")


# Run the quiz
start_quiz()
