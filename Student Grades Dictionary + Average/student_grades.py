def main():
    students = get_students()
    print_grades(students)
    print(f"Average grade: {average_grade(students):.2f}")

def get_students():
    students = {}
    for _ in range(3):
        name = input("Student name: ")
        while True:
            try:
                grade = int(input(f"Grade for {name}: "))
                if 0 <= grade <= 100:
                    students[name] = grade
                    break
                else:
                    print("Grade must be 0-100")
            except ValueError:
                print("Enter a number")
    return students

def print_grades(students):
    for student in students:
        print(f"{student}: {students[student]}")

def average_grade(students):
    total = sum(students.values())
    return total / len(students)

if __name__ == "__main__":
    main()
