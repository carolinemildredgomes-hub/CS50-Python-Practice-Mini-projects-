def main():
    secret = random.randint(1, 10)
    attempts = 0
    while True:
        guess = get_guess()
        attempts += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You guessed in {attempts} attempts.")
            break

def get_guess():
    while True:
        try:
            n = int(input("Your guess (1-10): "))
            if 1 <= n <= 10:
                return n
            else:
                print("Enter number 1-10")
        except ValueError:
            print("Enter a valid number")

if __name__ == "__main__":
    main()
