
# Task 1: Python Data Structures

# Creating a list of teachers using dictionaries

teachers = [
    {
        "id": "T01",
        "name": "Ayesha Khan",
        "subject": "Mathematics",
        "email": "ayesha@gmail.com"
    },
    {
        "id": "T02",
        "name": "Rohan Sharma",
        "subject": "Python",
        "email": "rohan@gmail.com"
    },
    {
        "id": "T03",
        "name": "Sana Mir",
        "subject": "AI",
        "email": "sana@gmail.com"
    },
    {
        "id": "T04",
        "name": "Imran Ahmad",
        "subject": "Mathematics",
        "email": "imran@gmail.com"
    },
    {
        "id": "T05",
        "name": "Neha Gupta",
        "subject": "Python",
        "email": "neha@gmail.com"
    }
]


# Display all teachers

def display_teachers():
    print("\n--- All Teachers ---")

    for teacher in teachers:
        print(teacher)


# Search teacher using ID

def search_teacher():
    tid = input("Enter teacher ID: ")

    for teacher in teachers:
        if teacher["id"] == tid:
            print("Teacher found:")
            print(teacher)
            return

    print("Teacher not found.")


# Display teachers by subject

def teachers_by_subject():
    subject = input("Enter subject: ").lower()

    for teacher in teachers:
        if teacher["subject"].lower() == subject:
            print(teacher)


# Tuple example

subjects = ("Mathematics", "Python", "AI")


# Set example

unique_subjects = {"Mathematics", "Python", "AI", "Python"}


# Main programme

print("1. Display all teachers")
print("2. Search teacher")
print("3. Display teachers by subject")
print("4. Show tuple")
print("5. Show set")

choice = input("Enter your choice: ")

if choice == "1":
    display_teachers()

elif choice == "2":
    search_teacher()

elif choice == "3":
    teachers_by_subject()

elif choice == "4":
    print(subjects)

elif choice == "5":
    print(unique_subjects)

else:
    print("Invalid choice.")
