while True:
    try:
        filename = input("Enter filename: ")

        with open(filename, "r") as file:
            content = file.read()

            if content == "":
                raise ValueError("File is empty.")

            print(content)
            break

    except FileNotFoundError:
        print("File not found.")

    except ValueError as e:
        print("Error:", e)
