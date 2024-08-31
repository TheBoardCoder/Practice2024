# Randolph Paul 4/29/2024 randolphPaul_Project2
# The purpose of this program is to calculate the cost of tea orders.

import random

# Global constants
TEA_NAMES = ["Plain Tea", "Black Tea", "Green Tea", "White Tea"]
TEA_PRICES = [0.43, 0.53, 0.65, 0.78]
TEA_SIZES = ["Small (8 oz)", "Medium (16 oz)", "Large (24 oz)"]
SALES_TAX_RATE = 0.045


# Display the menu
def display_start_menu():
    print("\nWelcome to the Tea Shop!")
    print("1. Process a single tea order")
    print("2. Process multiple tea orders")
    print("3. Quit\n")
    return int(input("Please enter your choice: "))


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
    print("\nTea type menu:")
    for i, tea_name in enumerate(TEA_NAMES):
        print(f"{i + 1}. {tea_name}")

    tea_choice = int(input("\nPlease enter choice of Tea: "))
    if tea_choice not in range(1, len(TEA_NAMES) + 1):
        print("\nERROR: INVALID MENU CHOICE. PROGRAM WILL TERMINATE.")
        exit()

    print("\nTea size menu:")
    for i, tea_size in enumerate(TEA_SIZES):
        print(f"{i + 1}. {tea_size}")

    size_choice = int(input("Please enter choice of size: "))
    if size_choice not in range(1, len(TEA_SIZES) + 1):
        print("\nERROR: INVALID MENU CHOICE. PROGRAM WILL TERMINATE.")
        exit()

    customer_name = input("Please enter the name of the customer: ")

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
    num_orders = int(input("\nPlease enter the number of orders (1-10): "))
    while num_orders <= 0 or num_orders >= 11:
        num_orders = int(input("Invalid input. Please enter a number of orders between 1 and 10: "))

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
