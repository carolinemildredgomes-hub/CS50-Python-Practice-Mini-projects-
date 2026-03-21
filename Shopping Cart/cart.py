menu = {
    "apple": 2,
    "banana": 1,
    "milk": 5
}

cart = {}
total = 0

while True:
    try:
        item = input("Item: ").lower()

        if item == "done":
            break

        if item not in menu:
            raise ValueError("Item not available.")

        cart[item] = cart.get(item, 0) + 1
        total += menu[item]

        print(f"Added {item}. Total = {total}")

    except ValueError as e:
        print("Error:", e)
