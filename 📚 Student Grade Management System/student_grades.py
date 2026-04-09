students = {}


def add_student():
    name = input("Enter student name: ")
    marks = []

    for i in range(3):
        mark = int(input(f"Enter mark {i + 1}: "))
        marks.append(mark)

    students[name] = marks
    print("Student added successfully.\n")


def show_grade():
    name = input("Enter student name: ")

    if name not in students:
        print("Student not found.\n")
        return

    avg = sum(students[name]) / len(students[name])

    if avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "F"

    print(f"{name} - Average: {avg:.2f}, Grade: {grade}\n")


def main():
    while True:
        print("1. Add Student")
        print("2. Show Grade")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_grade()
        elif choice == "3":
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
