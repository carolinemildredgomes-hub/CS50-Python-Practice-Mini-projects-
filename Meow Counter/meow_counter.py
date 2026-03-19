def main():
    meow(get_number())

def get_number():
    while True:
        try:
            n = int(input("Number of meows: "))
            if n > 0:
                return n
            else:
                print("Enter a positive number")
        except ValueError:
            print("Enter a number")

def meow(n):
    for _ in range(n):
        print("meow")

if __name__ == "__main__":
    main()
