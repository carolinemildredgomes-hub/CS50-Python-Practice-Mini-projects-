def generate_username(full_name):
    names = full_name.split()  # split first and last names
    if len(names) < 2:
        return full_name.lower()

    first_name = names[0][:3]   # first 3 letters of first name
    last_name = names[1][:3]    # first 3 letters of last name

    username = (first_name + last_name).lower()
    return username

full_name = input("Enter your full name (first and last): ")
username = generate_username(full_name)
print("Your unique username is:", username)
