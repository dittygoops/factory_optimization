# Factory Production Optimization Tool

## Overview

This Python application provides a linear programming solution for optimizing factory production. It helps businesses determine the most profitable mix of products and resources while respecting constraints such as total available factory hours and budget.

## Features

- Interactive input for factory constraints
- Flexible product and recipe configuration
- Maximum quantity restraints for each supply
- Optimization of total profit
- Detailed output of optimal production strategy

## Prerequisites

- Python 3.7+
- PuLP Library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/factory-optimization.git
cd factory-optimization
```

2. Install required dependencies:
```bash
python -m venv .venv (Optional -- if you want to create a Python virtual environment)
.\.venv\Scripts\activate (Optional -- if you want to create a Python virtual environment)
pip install pulp
```

## Usage

Run the script and follow the interactive prompts:

```bash
python factory_optimization.py
```

### Input Process

1. Enter total available factory hours
2. Enter total factory budget
3. Specify number of unique supplies
4. For each supply, provide:
   - Supply name
   - Unit cost
   - Maximum quantity
4. Specify number of unique products
5. For each product, provide:
   - Product name
   - Recipe
   - Time to produce (hours)
   - Additional production cost
   - Selling price
   
### Example Scenario

```
Factory Production Optimization
-------------------------------
Total Available Factory Hours: 500
Total Factory Budget ($): 10000


Number of Unique Supplies: 2
Enter Supply 1 Info:
Supply Name: Wire
Cost of the Supply ($): 5
Maximum Quantity of the Supply: 200


Enter Supply 2 Info:
Supply Name: Aluminum
Cost of the Supply ($): 10
Maximum Quantity of the Supply: 150


Number of Unique Products: 2
Enter Product 1 Info:
Item Name: iPhone
Quantity of Wire needed: 3
Quantity of Aluminum needed: 2
Time to produce the item (hours): 2
Cost to produce the item ($): 50
Price to sell the item ($): 400


Enter Product 2 Info:
Item Name: Macbook
Quantity of Wire needed: 5
Quantity of Aluminum needed: 8
Time to produce the item (hours): 5
Cost to produce the item ($): 200
Price to sell the item ($): 1500
```

## How It Works

The tool uses linear programming to:
- Maximize total profit
- Respect factory hour constraints
- Respect budget constraints
- Adhere to user-specified recipes

## Optimization Constraints

1. Factory Hours Limitation
2. Budget Limitation
3. Maximum Supply Quantity
4. Product Recipes

## Output

The program provides:
- Optimal purchase levels for each supply
- Optimal production quantities for each product
- Total production cost
- Total production hours
- Total production revenue
- Total production profit

## Customization

You can easily modify the script to:
- Add more complex constraints
- Change optimization objectives
- Integrate with existing production systems