
# Task 3: Improving the Question Bank

teachers = [
    {"id": "T01", "name": "Ayesha Khan", "subject": "Mathematics"},
    {"id": "T02", "name": "Rohan Sharma", "subject": "Python"},
    {"id": "T03", "name": "Sana Mir", "subject": "AI"}
]


questions = []


# Add question submitted by teacher

def add_question():

    tid = input("Enter teacher ID: ")

    selected_teacher = None

    for teacher in teachers:
        if teacher["id"] == tid:
            selected_teacher = teacher
            break

    if selected_teacher is None:
        print("Teacher not found.")
        return

    qid = input("Enter question ID: ")

    for q in questions:
        if q["id"] == qid:
            print("Question ID already exists.")
            return

    question = input("Enter question: ")

    try:
        marks = int(input("Enter marks: "))

        if marks <= 0:
            print("Marks must be greater than zero.")
            return

    except ValueError:
        print("Invalid marks.")
        return

    new_question = {
        "id": qid,
        "teacher_id": tid,
        "subject": selected_teacher["subject"],
        "question": question,
        "marks": marks
    }

    questions.append(new_question)

    print("Question added under", selected_teacher["subject"])


# Display question bank

def display_questions():

    print("\n--- Question Bank ---")

    for q in questions:
        print(q)


# Display questions by subject

def search_questions():

    subject = input("Enter subject: ").lower()
    found = False

    for q in questions:
        if q["subject"].lower() == subject:
            print(q)
            found = True

    if not found:
        print("No questions available.")


# Main programme

while True:

    print("\n1. Add question")
    print("2. Display questions")
    print("3. Search questions by subject")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_question()

    elif choice == "2":
        display_questions()

    elif choice == "3":
        search_questions()

    elif choice == "0":
        break

    else:
        print("Invalid choice.")
