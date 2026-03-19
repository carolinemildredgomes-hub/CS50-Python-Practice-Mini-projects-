def main():
    height = get_height()
    print_pyramid(height)

def get_height():
    while True:
        try:
            n = int(input("Enter pyramid height (1-8): "))
            if 1 <= n <= 8:
                return n
            else:
                print("Height must be between 1 and 8")
        except ValueError:
            print("Please enter a number.")

def print_pyramid(height):
    for row in range(1, height + 1):
        print(" " * (height - row) + "#" * row)

if __name__ == "__main__":
    main()
