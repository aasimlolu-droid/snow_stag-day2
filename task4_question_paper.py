
# Task 4: Question Paper Generator

import random

# Sample question bank

questions = [
    {"id": "Q01", "subject": "Mathematics", "question": "What is 10 + 20?", "marks": 2},
    {"id": "Q02", "subject": "Mathematics", "question": "What is 5 x 5?", "marks": 2},
    {"id": "Q03", "subject": "Mathematics", "question": "Find the square root of 64.", "marks": 3},
    {"id": "Q04", "subject": "Mathematics", "question": "Solve 2x + 4 = 10.", "marks": 4},
    {"id": "Q05", "subject": "Mathematics", "question": "Define prime numbers.", "marks": 2},

    {"id": "Q06", "subject": "Python", "question": "What is Python?", "marks": 2},
    {"id": "Q07", "subject": "Python", "question": "What is a variable?", "marks": 2},
    {"id": "Q08", "subject": "Python", "question": "Explain for loop.", "marks": 3},
    {"id": "Q09", "subject": "Python", "question": "What is a list?", "marks": 2},
    {"id": "Q10", "subject": "Python", "question": "What is a function?", "marks": 3},

    {"id": "Q11", "subject": "AI", "question": "What is Artificial Intelligence?", "marks": 2},
    {"id": "Q12", "subject": "AI", "question": "Define Machine Learning.", "marks": 3},
    {"id": "Q13", "subject": "AI", "question": "What is a neural network?", "marks": 4},
    {"id": "Q14", "subject": "AI", "question": "What is an expert system?", "marks": 2},
    {"id": "Q15", "subject": "AI", "question": "Give two applications of AI.", "marks": 3}
]


# Generate question paper

def generate_paper():

    subject = input("Enter subject: ").lower()

    try:
        number = int(input("Enter number of questions: "))

        if number <= 0:
            print("Enter a positive number.")
            return

    except ValueError:
        print("Invalid number.")
        return

    available = []

    for q in questions:
        if q["subject"].lower() == subject:
            available.append(q)

    if len(available) == 0:
        print("No questions available.")
        return

    if number > len(available):
        print("Only", len(available), "questions are available.")
        number = len(available)

    selected = random.sample(available, number)

    print("\n--- QUESTION PAPER ---")
    print("Subject:", selected[0]["subject"])

    total_marks = 0

    for i, q in enumerate(selected, 1):

        print("\n", i, ".", q["question"])
        print("Marks:", q["marks"])

        total_marks += q["marks"]

    print("\nTotal questions:", len(selected))
    print("Total marks:", total_marks)


# Run programme

generate_paper()
