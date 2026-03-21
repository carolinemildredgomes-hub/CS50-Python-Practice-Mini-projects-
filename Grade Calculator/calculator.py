scores = []

while True:
    try:
        score = input("Score: ")

        if score == "":
            break

        score = float(score)
        scores.append(score)

    except ValueError:
        print("Invalid score.")

if len(scores) > 0:
    avg = sum(scores) / len(scores)

    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"

    print("Average:", avg)
    print("Grade:", grade)
