# Randolph Paul 4/9/2024 randolphPaul_lab12
# The purpose of this program is to calculate the cost of painting multiple rooms.

# Set constants
MIN_ROOM = 1
MIN_SQ_FT = 0
MIN_PRICE = 10
COUNTER = 1
LABOR_COST = 35
WALL_AMT = 225
LABOR_HOURS = 4

# Explain what the program does to the user
print("\nThis program calculates the cost of painting multiple rooms.")


# Runs the main function to carry out the programs purpose
def main():
    square_footages = get_num_rooms()
    price_per_gallon = get_paint_price()
    gallons_required, hours_required, paint_cost, labor_cost, total_cost = calculate_costs(square_footages, price_per_gallon)
    print_results(gallons_required, hours_required, paint_cost, labor_cost, total_cost)


# Requests user input for the number of rooms to be painted and square footage
def get_num_rooms():
    while True:
        try:
            num_rooms = int(input("\nEnter the number of rooms to be painted: "))
            if num_rooms < MIN_ROOM:
                raise ValueError
            square_footages = []
            for i in range(num_rooms):
                while True:
                    try:
                        square_footage = int(input(f"Enter the square footage of room {i + COUNTER}: "))
                        if square_footage < MIN_SQ_FT:
                            raise ValueError
                        square_footages.append(square_footage)
                        break
                    except ValueError:
                        print("Square footage must be a non-negative integer. Please try again.")
            return square_footages
        except ValueError:
            print("Number of rooms must be a positive integer. Please try again.")


# Requests user input for the paint's price
def get_paint_price():
    while True:
        try:
            price_per_gallon = float(input("Enter the price per gallon of paint (minimum $10.00): "))
            if price_per_gallon < MIN_PRICE:
                raise ValueError
            return price_per_gallon
        except ValueError:
            print("Price per gallon must be at least $10.00. Please try again.")


# Calculates the gallons
def calculate_costs(square_footages, price_per_gallon):
    total_square_footage = sum(square_footages)
    gallons_required = total_square_footage / WALL_AMT
    hours_required = gallons_required * LABOR_HOURS
    paint_cost = gallons_required * price_per_gallon
    labor_cost = hours_required * LABOR_COST
    total_cost = paint_cost + labor_cost
    return gallons_required, hours_required, paint_cost, labor_cost, total_cost


# Displays the results of the calculations
def print_results(gallons_required, hours_required, paint_cost, labor_cost, total_cost):
    print("\nResults:")
    print(f"Gallons of paint required: {gallons_required:,.2f}")
    print(f"Hours of labor required: {hours_required:,.2f}")
    print(f"Cost of paint: ${paint_cost:,.2f}")
    print(f"Labor cost: ${labor_cost:,.2f}")
    print(f"Total cost of the job: ${total_cost:,.2f}")


# Entry point of the program
if __name__ == "__main__":
    main()
