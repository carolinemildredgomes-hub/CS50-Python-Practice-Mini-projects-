while True:
    try:
        number = int(input("Number: "))
        print("Valid integer:" , number)
        break
    except ValueError:
        print("Inavild input , please enter an integer.")
