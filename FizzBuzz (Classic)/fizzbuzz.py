def main():
    start, end = get_range()
    fizzbuzz(start, end)

def get_range():
    while True:
        try:
            start = int(input("Start number: "))
            end = int(input("End number: "))
            if start < end:
                return start, end
            else:
                print("End must be greater than start")
        except ValueError:
            print("Enter numbers only")

def fizzbuzz(start, end):
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    main()
