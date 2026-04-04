def main():
    message = input("Enter your greeting: ")
    print(reward(message))


def reward(message):
    """Return 0 if starts with 'welcome', 20 if starts with 'w', else 100."""
    message_lower = message.lower()
    if message_lower.startswith("welcome"):
        return 0
    elif message_lower.startswith("w"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
