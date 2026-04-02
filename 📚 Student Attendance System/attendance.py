def check_attendance(name):
    attendance = {
        "Caroline": "Present",
        "David": "Absent",
        "Sarah": "Late",
        "John": "Present",
        "Emma": "Absent"
    }

    return attendance.get(name, "Student not found")


student_name = input("Enter student name: ")
result = check_attendance(student_name)

print("Attendance:", result)
