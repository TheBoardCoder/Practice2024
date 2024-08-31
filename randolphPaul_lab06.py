#Randolph Paul 4/2/2024 randolphPaul_lab06
'''The purpose of this program is to calculate the price of software
packages that cost $77 for an amount of packages specified from a user
and display the quantity purchased, the cost without the discount,
the discount, and the final cost.'''

# Set constants and variables
PACKAGE_PRICE = 77
discount_rate = 0
DISCOUNT_RANGES = [
    (9, 23, 0.085),
    (24, 41, 0.225),
    (42, 88, 0.325),
    (89, float('inf'), 0.395)]

# Get user input
print("""\nThis program calculates the price of software packages that cost $77 and displays the 
quantity purchased, the cost without the discount, the discount, and the final cost.""")
while True:
    try:
        num_packages = int((input("\nPlease enter the number of software packages purchased as a whole number: ")))
        break
    except ValueError:
        print("Error: Please enter a valid integer.")

# Calculate discount
for min_quantity, max_quantity, rate in DISCOUNT_RANGES:
    if min_quantity <= num_packages <= max_quantity:
        discount_rate = rate
        break

# Calculate costs
cost_without_discount = num_packages * PACKAGE_PRICE
discount_amount = cost_without_discount * discount_rate
final_cost = cost_without_discount - discount_amount

# Display results
print(f"\nQuantity purchased: {num_packages:,}")
print(f"Cost without discount: ${cost_without_discount:,.2f}")
print(f"Discount rate: {discount_rate:.2%}")
print(f"Discount amount: ${discount_amount:,.2f}")
print(f"Final cost: ${final_cost:,.2f}")