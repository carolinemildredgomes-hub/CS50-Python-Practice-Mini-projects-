questions = {
    "2+2": "4",
    "3+5": "8",
    "10-2": "8"
}

score = 0

for q in questions:
    try:
        answer = input(f"{q}: ")

        if answer != questions[q]:
            raise ValueError("Wrong answer.")

        score += 1

    except ValueError as e:
        print(e)

print("Final Score:", score)
