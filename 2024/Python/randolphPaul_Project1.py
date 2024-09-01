# Randolph Paul 4/10/2024 randolphPaul_Project1
# The purpose of this program is to calculate the cost of a tea order.

# Sets constants
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

# Explain what the program does to the user
print("\nWelcome to the World’s Best Tea Shop\n")

# Tea type menu
print("1 –", PLAIN_TEA)
print("2 –", BLACK_TEA)
print("3 –", GREEN_TEA)
print("4 –", WHITE_TEA)

# Get the user's input on their tea choice
tea_choice = int(input("\nEnter choice of Tea: "))

# Validate the tea choice
if tea_choice not in range(TEA_RANGE_START, TEA_RANGE_END):
    print("\nERROR: INVALID MENU CHOICE. PROGRAM WILL TERMINATE.")
    exit()

# Display the tea size menu
print(f"\n1 – {SMALL_TEA}")
print(f"2 – {MEDIUM_TEA}")
print(f"3 – {LARGE_TEA}")

# Get the user's input on the tea size
size_choice = int(input("\nEnter choice of size: "))

# Validate the size choice
if size_choice not in range(SIZE_RANGE_START, SIZE_RANGE_END):
    print("\nERROR: INVALID MENU CHOICE. PROGRAM WILL TERMINATE.")
    exit()

# Get the customer's name
customer_name = input("Enter the name of the customer: ")

# Calculate the cost of tea
if tea_choice == FIRST_CHOICE:
    tea_name = PLAIN_TEA
    tea_cost_per_ounce = PLAIN_TEA_COST
elif tea_choice == SECOND_CHOICE:
    tea_name = BLACK_TEA
    tea_cost_per_ounce = BLACK_TEA_COST
elif tea_choice == THIRD_CHOICE:
    tea_name = GREEN_TEA
    tea_cost_per_ounce = GREEN_TEA_COST
else:
    tea_name = WHITE_TEA
    tea_cost_per_ounce = WHITE_TEA_COST

if size_choice == FIRST_CHOICE:
    tea_size = SMALL_TEA
    tea_ounces = SMALL_OZ
elif size_choice == SECOND_CHOICE:
    tea_size = MEDIUM_TEA
    tea_ounces = MEDIUM_OZ
else:
    tea_size = LARGE_TEA
    tea_ounces = LARGE_OZ

tea_cost = tea_cost_per_ounce * tea_ounces
sales_tax = tea_cost * SALES_TAX_RATE
total_cost = tea_cost + sales_tax

# Display the customer's bill
print(f"\n{customer_name}")
print(f"\nPrice of Tea: ${tea_cost:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total Amount Owed: ${total_cost:.2f}")
