import pulp

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

    # Get maximum quantity of the item
    while True:
        try:
            max_quantity = int(input("Maximum Quantity of the Item: "))
            if max_quantity < 0:
                raise ValueError("The maximum quantity cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input. Please enter a valid number.")

    return {"name": name, "time": time, "cost": cost, "price": price, "max_quantity": max_quantity}

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

def solve(factory, items):
    p = pulp.LpProblem("Factory Problem", pulp.LpMaximize)
    pulp.LpSolverDefault.msg = 0

    products = [pulp.LpVariable(f"{i["name"]}", lowBound=0, upBound=i["max_quantity"], cat=pulp.LpInteger) for i in items]

    obj_func = pulp.lpSum((items[i]["price"] - items[i]["cost"]) * products[i] for i in range(len(items)))
    p += obj_func

    time_constraint = pulp.lpSum(items[i]["time"] * products[i] for i in range(len(items))) <= factory["factory_hours"]
    p += time_constraint

    budget_constraint = pulp.lpSum(items[i]["cost"] * products[i] for i in range(len(items))) <= factory["factory_budget"]
    p += budget_constraint

    p.solve()

    print("\n--- Optimization Results ---")
    print(f"Status: {pulp.LpStatus[p.status]}")

    # If an optimal solution is found
    if pulp.LpStatus[p.status] == "Optimal":
        print("\nOptimal Production Quantities:")
        total_profit = 0
        total_hours = 0
        total_cost = 0

        for i, var in enumerate(products):
            quantity = var.varValue
            if quantity > 0:
                profit = (items[i]['price'] - items[i]['cost']) * quantity
                print(f"{items[i]['name']}: {quantity:.2f} units")
                print(f"  Profit per unit: ${items[i]['price'] - items[i]['cost']:.2f}")
                print(f"  Total Profit for this Product: ${profit:.2f}")
                
                total_profit += profit
                total_hours += items[i]['time'] * quantity
                total_cost += items[i]['cost'] * quantity

        print(f"\nTotal Production Hours: {total_hours:.2f}")
        print(f"Total Production Cost: ${total_cost:.2f}")
        print(f"Total Profit: ${total_profit:.2f}")
    else:
        print("No optimal solution found.")

def main():
    factory = initialize_factory()
    items = initialize_items()

    solve(factory, items)

if __name__ == "__main__":
    main()