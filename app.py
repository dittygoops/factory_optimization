def initialize_factory():
    while True:
        try:
            factory_hours = float(input("Total Available Factory Hours: "))
            if factory_hours < 0:
                raise ValueError("The number of hours cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input. Please enter a valid number.")

    while True:
        try:
            factory_budget = float(input("Total Factory Budget ($): "))
            if factory_budget < 0:
                raise ValueError("The budget cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input. Please enter a valid number.")

    print("\n")

    return {"factory_hours": factory_hours, "factory_budget": factory_budget}

def initialize_item():
    # Get the name of the item
    name = input("Item Name: ")

    # Get the time to produce the item
    while True:
        try:
            time = float(input("Time to produce the item (hours): "))
            if time < 0:
                raise ValueError("The time cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input. Please enter a valid number.")

    # Get the cost of the item
    while True:
        try:
            cost = float(input("Cost to produce the item ($): "))
            if cost < 0:
                raise ValueError("The cost cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input. Please enter a valid number.")

    # Get the price to sell the item
    while True:
        try:
            price = float(input("Price to sell the item ($): "))
            if price < 0:
                raise ValueError("The price cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input. Please enter a valid number.")

    return {"name": name, "time": time, "cost": cost, "price": price}

def initialize_items():
    while True:
        try:
            num_of_products = int(input("Number of Unique Products: "))
            if num_of_products < 0:
                raise ValueError("The number of unique products cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input. Please enter a valid number.")

    items = []

    for i in range(num_of_products):
        print(f"Enter Product {i + 1} Info:")
        item = initialize_item()
        items.append(item)

        print("\n")

    return items

def main():
    factory = initialize_factory()
    items = initialize_items()


if __name__ == "__main__":
    main()