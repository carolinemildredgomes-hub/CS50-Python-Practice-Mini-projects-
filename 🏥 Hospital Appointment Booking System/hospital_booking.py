appointments = []


def book():
    patient = input("Enter patient name: ")
    doctor = input("Enter doctor name: ")
    time = input("Enter appointment time: ")

    appointments.append({
        "patient": patient,
        "doctor": doctor,
        "time": time
    })

    print("Appointment booked successfully.\n")


def view():
    if not appointments:
        print("No appointments found.\n")
        return

    for app in appointments:
        print(app)
    print()


def cancel():
    patient = input("Enter patient name to cancel: ")

    for app in appointments:
        if app["patient"] == patient:
            appointments.remove(app)
            print("Appointment cancelled.\n")
            return

    print("Appointment not found.\n")


def main():
    while True:
        print("1. Book Appointment")
        print("2. View Appointments")
        print("3. Cancel Appointment")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            book()
        elif choice == "2":
            view()
        elif choice == "3":
            cancel()
        elif choice == "4":
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
