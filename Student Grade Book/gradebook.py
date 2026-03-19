def main():
    students = get_students()
    print_gradebook(students)
    print(f"Average grade: {average_grade(students):.2f}")
    print(f"Top student: {top_student(students)}")

def get_students():
    students = {}
    n = int(input("How many students? "))
    for _ in range(n):
        name = input("Student name: ")
        while True:
            try:
                grade = int(input(f"Grade for {name}: "))
                if 0 <= grade <= 100:
                    students[name] = grade
                    break
                else:
                    print("0-100 only")
            except ValueError:
                print("Enter number")
    return students

def print_gradebook(students):
    for student, grade in students.items():
        print(f"{student}: {grade}")

def average_grade(students):
    return sum(students.values()) / len(students)

def top_student(students):
    return max(students, key=students.get)

if __name__ == "__main__":
    main()
