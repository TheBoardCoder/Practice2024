# Randolph Paul 4/29/2024 randolphPaul_Project2
# The purpose of this program is to calculate the cost of a tea order.

import random

# Constants for the first code
SMALL_TEA = "Small (8 oz)"
MEDIUM_TEA = "Medium (16 oz)"
LARGE_TEA = "Large (24 oz)"
PLAIN_TEA = "Plain Tea"
BLACK_TEA = "Black Tea"
GREEN_TEA = "Green Tea"
WHITE_TEA = "White Tea"
PLAIN_TEA_COST = 0.43
BLACK_TEA_COST = 0.53
GREEN_TEA_COST = 0.65
WHITE_TEA_COST = 0.78
SALES_TAX_RATE = 0.045
FIRST_CHOICE = 1
SECOND_CHOICE = 2
THIRD_CHOICE = 3
SMALL_OZ = 8
MEDIUM_OZ = 16
LARGE_OZ = 24
TEA_RANGE_START = 1
TEA_RANGE_END = 5
SIZE_RANGE_START = 1
SIZE_RANGE_END = 4

# Constants for the second code
TEA_NAMES = ["Green Tea", "Black Tea", "Herbal Tea", "Oolong Tea", "White Tea"]
TEA_PRICES = [2.50, 3.00, 2.75, 3.25, 3.50]
TEA_SIZES = ["Small", "Medium", "Large"]
SALES_TAX_RATE = 0.06


# Display the menu
def display_start_menu():
    print("\nWelcome to the Tea Shop!")
    print("1. Process a single tea order")
    print("2. Process multiple tea orders")
    print("3. Quit")
    return int(input("Enter your choice: "))


# Determine cost
def determine_cost_per_oz(tea_choice):
    return TEA_PRICES[tea_choice]


# Determine the tea size
def determine_tea_size(size_choice):
    return TEA_SIZES[size_choice]


# Calculate the tea price
def calculate_price_tea(price_per_oz, size_oz):
    return price_per_oz * size_oz


# Calculate the sales tax
def calculate_sales_tax(price):
    return price * SALES_TAX_RATE


# Calculate the bill
def calculate_total_bill(price, tax):
    return price + tax


# Process the order
def process_single_order():
    print("\nProcessing a single tea order...")

    print("Tea type menu:")
    for i, tea_name in enumerate(TEA_NAMES):
        print(f"{i + 1}. {tea_name}")

    tea_choice = int(input("Enter choice of Tea: "))
    if tea_choice not in range(1, len(TEA_NAMES) + 1):
        print("\nERROR: INVALID MENU CHOICE. PROGRAM WILL TERMINATE.")
        exit()

    print("\nTea size menu:")
    for i, tea_size in enumerate(TEA_SIZES):
        print(f"{i + 1}. {tea_size}")

    size_choice = int(input("Enter choice of size: "))
    if size_choice not in range(1, len(TEA_SIZES) + 1):
        print("\nERROR: INVALID MENU CHOICE. PROGRAM WILL TERMINATE.")
        exit()

    customer_name = input("Enter the name of the customer: ")

    tea_cost_per_oz = determine_cost_per_oz(tea_choice - 1)
    tea_size_oz = [8, 16, 24][size_choice - 1]

    tea_cost = calculate_price_tea(tea_cost_per_oz, tea_size_oz)
    sales_tax = calculate_sales_tax(tea_cost)
    total_cost = calculate_total_bill(tea_cost, sales_tax)

    print(f"\n{customer_name}")
    print(f"Tea Type: {TEA_NAMES[tea_choice - 1]}")
    print(f"Tea Size: {TEA_SIZES[size_choice - 1]}")
    print(f"Price of Tea: ${tea_cost:.2f}")
    print(f"Sales Tax: ${sales_tax:.2f}")
    print(f"Total Amount Owed: ${total_cost:.2f}")


# Process the orders
def process_multiple_orders():
    print("\nProcessing multiple tea orders...")
    num_orders = int(input("Enter the number of orders (1-10): "))
    while num_orders < 1 or num_orders > 10:
        num_orders = int(input("Invalid input. Enter a number of orders between 1 and 10: "))

    for i in range(num_orders):
        tea_choice = random.randint(0, len(TEA_NAMES) - 1)
        size_choice = random.randint(0, len(TEA_SIZES) - 1)
        tea_cost_per_oz = determine_cost_per_oz(tea_choice)
        tea_size_oz = [8, 16, 24][size_choice]
        tea_cost = calculate_price_tea(tea_cost_per_oz, tea_size_oz)
        sales_tax = calculate_sales_tax(tea_cost)
        total_cost = calculate_total_bill(tea_cost, sales_tax)

        print(f"\nOrder {i + 1}:")
        print(f"Tea Type: {TEA_NAMES[tea_choice]}")
        print(f"Tea Size: {TEA_SIZES[size_choice]}")
        print(f"Price: ${tea_cost:.2f}")
        print(f"Tax: ${sales_tax:.2f}")
        print(f"Total Cost: ${total_cost:.2f}")


# Run the main program
def main():
    while True:
        choice = display_start_menu()
        if choice == 1:
            process_single_order()
        elif choice == 2:
            process_multiple_orders()
        elif choice == 3:
            print("\nExiting program...")
            break
        else:
            print("\nInvalid choice. Please enter a valid menu option.")


# Start program
if __name__ == "__main__":
    main()
