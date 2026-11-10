
# Task 2: Working with Functions

# Sample question bank

questions = [
    {
        "id": "Q01",
        "subject": "Python",
        "question": "What is Python?",
        "marks": 2
    },
    {
        "id": "Q02",
        "subject": "Mathematics",
        "question": "What is 10 + 20?",
        "marks": 2
    },
    {
        "id": "Q03",
        "subject": "AI",
        "question": "What is Artificial Intelligence?",
        "marks": 3
    }
]


# Add a new question

def add_question():
    qid = input("Enter question ID: ")

    for q in questions:
        if q["id"] == qid:
            print("Question ID already exists.")
            return

    subject = input("Enter subject: ")
    question = input("Enter question: ")

    try:
        marks = int(input("Enter marks: "))
        if marks <= 0:
            print("Marks must be positive.")
            return
    except ValueError:
        print("Please enter valid marks.")
        return

    new_question = {
        "id": qid,
        "subject": subject,
        "question": question,
        "marks": marks
    }

    questions.append(new_question)

    print("Question added successfully.")


# Display all questions

def display_questions():
    for q in questions:
        print(q)


# Search questions by subject

def search_subject():
    subject = input("Enter subject: ").lower()
    found = False

    for q in questions:
        if q["subject"].lower() == subject:
            print(q)
            found = True

    if not found:
        print("No questions found.")


# Count questions for each subject

def count_questions():
    count = {}

    for q in questions:
        subject = q["subject"]

        if subject in count:
            count[subject] += 1
        else:
            count[subject] = 1

    print(count)


# Main menu

while True:

    print("\n--- Question Bank ---")
    print("1. Add question")
    print("2. Display questions")
    print("3. Search by subject")
    print("4. Count questions")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_question()

    elif choice == "2":
        display_questions()

    elif choice == "3":
        search_subject()

    elif choice == "4":
        count_questions()

    elif choice == "0":
        break

    else:
        print("Invalid choice.")
