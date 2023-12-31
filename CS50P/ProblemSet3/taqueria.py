def main():
    taqueriaMenu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    orderTotal = 0.00

    while True:
        try:
            userInput = input("Item: ")
            menuItem = userInput.title()
            if menuItem in taqueriaMenu:
                orderTotal += taqueriaMenu[menuItem]
                print(f"Total: ${orderTotal:.2f}")
            else:
                pass
        except EOFError:
            break

    print("\n", end="")

main()
