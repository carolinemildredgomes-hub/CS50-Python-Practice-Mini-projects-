while True:
    try:
        num1 = float(input("First number: "))
        operator = input("Operator (+, -, *, /): ")
        num2 = float(input("Second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        else:
            print("Invalid operator!")
            continue

        print("Result:", result)
        break

    except ValueError:
        print("Invalid number. Please enter numeric values.")

    except ZeroDivisionError:
        print("Cannot divide by zero!")
