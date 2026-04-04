def main():
    fraction = input("Enter liquid level as X/Y: ")
    try:
        percent = convert(fraction)
        print(display(percent))
    except ValueError:
        print("Invalid fraction")
    except ZeroDivisionError:
        print("Division by zero not allowed")


def convert(fraction):
    """Convert X/Y string into percentage (0-100)."""
    try:
        x_str, y_str = fraction.split("/")
        x = int(x_str)
        y = int(y_str)
    except ValueError:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError
    if x < 0 or y < 0:
        raise ValueError
    if x > y:
        raise ValueError

    return round(x / y * 100)


def display(percentage):
    """Return fuel display string based on percentage."""
    if percentage <= 1:
        return "LOW"
    elif percentage >= 99:
        return "FULL"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
