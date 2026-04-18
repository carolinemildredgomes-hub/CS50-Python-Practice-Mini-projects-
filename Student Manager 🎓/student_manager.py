class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        if house not in ["Red", "Blue", "Green"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    print(student)


if __name__ == "__main__":
    main()
