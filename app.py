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

def initialize_supply():
    # Get the name of the supply
    name = input("Supply Name: ")

    # Get the cost of the supply
    while True:
        try:
            cost = float(input("Cost of the Supply ($): "))
            if cost < 0:
                raise ValueError("The cost cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input. Please enter a valid number.")

    # Get max quantity of the supply
    while True:
        try:
            max_quantity = int(input("Maximum Quantity of the Supply: "))
            if max_quantity < 0:
                raise ValueError("The maximum quantity cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input. Please enter a valid number.")
    
    return {"name": name, "cost": cost, "max_quantity": max_quantity}

def initialize_supplies():
    while True:
        try:
            num_of_supplies = int(input("Number of Unique Supplies: "))
            if num_of_supplies < 0:
                raise ValueError("The number of unique supplies cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input. Please enter a valid number.")

    supplies = []

    for i in range(num_of_supplies):
        print(f"Enter Supply {i + 1} Info:")
        supply = initialize_supply()
        supplies.append(supply)

        print("\n")

    return supplies

def initialize_item(supplies):
    # Get the name of the item
    name = input("Item Name: ")

    # Get the recipe for the item
    recipe = {}
    recipe_cost = 0
    for supply in supplies:
        while True:
            try:
                quantity = float(input(f"Quantity of {supply['name']} needed: "))
                if quantity < 0:
                    raise ValueError("The quantity cannot be negative.")
                break
            except ValueError as e:
                print(f"Invalid input. Please enter a valid number.")
        
        recipe[supply["name"]] = quantity
        recipe_cost += quantity * supply["cost"]

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

    return {"name": name, "recipe": recipe, "recipe_cost": recipe_cost, "time": time, "cost": cost, "price": price}

def initialize_items(supplies):
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
        item = initialize_item(supplies)
        items.append(item)

        print("\n")

    return items

def solve(factory, supplies, items):
    p = pulp.LpProblem("Factory Problem", pulp.LpMaximize)
    pulp.LpSolverDefault.msg = 0

    supply_variables = [pulp.LpVariable(f"{i['name']}", lowBound=0, upBound=i["max_quantity"], cat=pulp.LpInteger) for i in supplies]

    # ToDo: Add constraints including supplies
    products = [pulp.LpVariable(f"{i['name']}", lowBound=0,cat=pulp.LpInteger) for i in items]

    obj_func = pulp.lpSum((items[i]["price"] - items[i]["cost"] - items[i]["recipe_cost"]) * products[i] for i in range(len(items)))
    p += obj_func

    time_constraint = pulp.lpSum(items[i]["time"] * products[i] for i in range(len(items))) <= factory["factory_hours"]
    p += time_constraint

    budget_constraint = pulp.lpSum((items[i]["cost"] + items[i]["recipe_cost"]) * products[i] for i in range(len(items))) <= factory["factory_budget"]
    p += budget_constraint

    # ToDo: Add supply constraints
    for supply in supplies:
        supply_used = pulp.lpSum(
            items[i]['recipe'].get(supply['name'], 0) * products[i]
            for i in range(len(items))
        )
        p += supply_used <= supply["max_quantity"]

    p.solve()

    print("\n--- Optimization Results ---")
    print(f"Status: {pulp.LpStatus[p.status]}")

    # If an optimal solution is found
    if pulp.LpStatus[p.status] == "Optimal":
        print("\nOptimal Production Quantities:")
        total_profit = 0
        total_hours = 0
        total_cost = 0

        print("\nSupply Usage:")
        for j, supply in enumerate(supplies):
            supply_used = sum(
                items[i]['recipe'].get(supply['name'], 0) * products[i].varValue 
                for i in range(len(items))
            )
            print(f"{supply['name']}: {supply_used:.2f}/{supply['max_quantity']} used")
            print(f"  Total Cost: ${supply['cost'] * supply_used:.2f}")

        print("\nProduct Production:")

        for i, var in enumerate(products):
            quantity = var.varValue
            if quantity > 0:
                total_cost_per_product = (items[i]['cost'] + items[i]['recipe_cost']) * quantity
                total_hours_per_product = items[i]['time'] * quantity
                total_revenue = items[i]['price'] * quantity
                profit = total_revenue - total_cost_per_product

                print(f"{items[i]['name']}: {quantity:.2f} units")
                print(f"  Total Cost: ${total_cost_per_product:.2f}")
                print(f"  Total Hours: {total_hours_per_product:.2f}")
                print(f"  Total Revenue: ${total_revenue:.2f}")
                print(f"  Total Profit: ${profit:.2f}")
                
                total_profit += profit
                total_hours += total_hours_per_product
                total_cost += total_cost_per_product

        print(f"\nTotal Production Hours: {total_hours:.2f}")
        print(f"Total Production Cost: ${total_cost:.2f}")
        print(f"Total Profit: ${total_profit:.2f}")
    else:
        print("No optimal solution found.")

def main():
    factory = initialize_factory()
    supplies = initialize_supplies()
    items = initialize_items(supplies)

    # print(items)

    solve(factory, supplies, items)

if __name__ == "__main__":
    main()