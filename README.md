# Coffee Shop Simulator

An interactive, Python-based command-line interface (CLI) application that simulates the internal logic of a digital coffee vending machine. The system manages stateful ingredient inventory, processes multi-denomination coin inputs, handles exact change transactions, and tracks profit logs.

## Features

- **Dynamic Inventory Management**: Keeps real-time track of critical resources (Water, Milk, Coffee). The system dynamically evaluates ingredient requirements before accepting payment and alerts the user if resources are insufficient.
- **Multi-Denomination Coin Processor**: Simulates physical coin slots by accepting and calculating totals from Quarters ($0.25), Dimes ($0.10), Nickels ($0.05), and Pennies ($0.01).
- **Automated Transaction Logic**: Checks if the inserted cash covers the selected beverage cost. It automatically dispenses the exact change or issues a full refund if the funds are inadequate.
- **Admin & Maintenance Modes**: Built-in hidden console commands allow operators to check current ingredient/revenue statuses or safely power down the simulation.

## Menu & Pricing Matrix

| Beverage | Water | Milk | Coffee | Cost |
| :--- | :--- | :--- | :--- | :--- |
| **Espresso** | 50ml | 0ml | 18g | $1.50 |
| **Latte** | 200ml | 150ml | 24g | $2.50 |
| **Capuccinno** | 250ml | 100ml | 24g | $3.00 |
| **Cold Coffee** | 250ml | 100ml | 24g | $4.50 |
| **Hot Coffee** | 250ml | 100ml | 24g | $5.50 |

## System Commands

While the machine prompts you for a beverage choice, you can enter these maintenance keywords:
- `report`: Displays a breakdown of remaining ingredients in the inventory and total revenue collected.
- `off`: Shuts down the machine execution loop.

## How to Run

1. **Prerequisites**: Ensure you have Python 3.x installed on your machine.
2. **Clone the Repository**:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/coffee-shop-simulator.git](https://github.com/YOUR_USERNAME/coffee-shop-simulator.git)
   cd coffee-shop-simulator
