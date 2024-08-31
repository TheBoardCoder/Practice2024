#Randolph Paul 3/19/2024 randolphPaul_lab02
#The purpose of the program is to calculate the amount of money in an account at the end of a period using the compound interest formula.

#Set constants to be used later
one = 1
oneHundred = 100

#Inform the user of the purpose of this program
print("\nThis program calculates the amount of money in an account at the end of a period using the compound interest formula.")

# Get the user's input
principal = float(input("\nPlease enter the amount of money originally deposited into the account: "))
rate = float(input("Please enter the annual interest rate paid (as a decimal): "))
timesCompounded = float(input("Please enter the number of times per year the interest is compounded (e.g., monthly=12, quarterly=4): "))
years = float(input("Please enter the number of years the account will earn interest: "))

# Calculate the amount of money at the end of the period
amount = principal * (one + rate/timesCompounded)**(timesCompounded*years)

# Display the results
print("\nResults:")
print(f"Original deposit: ${principal:,.2f}")
print(f"Annual interest rate: {rate*oneHundred:,.2f}%")
print(f"Amount of money at end of the period: ${amount:,.2f}")
