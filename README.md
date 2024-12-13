# Factory Production Optimization Tool

## Overview

This Python application provides a linear programming solution for optimizing factory production. It helps businesses determine the most profitable mix of products while respecting constraints such as total available factory hours and budget.

## Features

- Interactive input for factory constraints
- Flexible product configuration
- Maximum quantity constraints for each product
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
3. Specify number of unique products
4. For each product, provide:
   - Product name
   - Time to produce (hours)
   - Production cost
   - Selling price
   - Maximum production quantity

### Example Scenario

```
Factory Production Optimization
-------------------------------
Total Available Factory Hours: 1000
Total Factory Budget ($): 50000

Number of Unique Products: 2

Enter Product 1 Info:
Item Name: Laptop
Time to produce the item (hours): 2
Cost to produce the item ($): 500
Price to sell the item ($): 1200
Maximum Quantity of this item that can be produced: 250

Enter Product 2 Info:
Item Name: Smartphone
Time to produce the item (hours): 1.5
Cost to produce the item ($): 300
Price to sell the item ($): 800
Maximum Quantity of this item that can be produced: 300
```

## How It Works

The tool uses linear programming to:
- Maximize total profit
- Respect factory hour constraints
- Respect budget constraints
- Adhere to maximum production quantities

## Optimization Constraints

1. Factory Hours Limitation
2. Budget Limitation
3. Maximum Product Quantity

## Output

The program provides:
- Optimal production quantities for each product
- Total profit
- Total production hours
- Total production cost

## Customization

You can easily modify the script to:
- Add more complex constraints
- Change optimization objectives
- Integrate with existing production systems
