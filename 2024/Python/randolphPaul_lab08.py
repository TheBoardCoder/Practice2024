# Randolph Paul 4/3/2024 randolphPaul_lab08
"""The purpose of this program is to produces a bar chart showing the population growth of
Dustyville, a small town in the midwest, at 20 year intervals from 1900 to 2000.
The program accepts keyboard input for the 6 census years."""

# Set variables, constants, and create list
ONE = 1
YEAR_RANGE = 6
ASTERISK = 1000
MAX_YEAR = 9999
populations = [2035, 4300, 5230, 9890, 14220, 18350, 19900]


# Explain what the program does to the user
print("""\nThis program produces a bar chart showing the population growth of Dustyville, 
a small town in the midwest, at 20 year intervals from 1900 to 2000. 
Note: The program accepts keyboard inputs for the 6 census years.\n""")

# Initialize an empty list to store years
years = []

# Prompt the user to input census years and append them to the list
for i in range(YEAR_RANGE):
    while True:
        try:
            year = int(input(f"Enter the census year {i+ONE}: "))
            if year > MAX_YEAR:
                raise ValueError
            years.append(year)
            break
        except ValueError:
            print("Error: Please enter a valid year")

# Display the title of the chart
print("\nDustyville Population Growth\n(each * represents 1,000 people)\n")

# Calculate and display the number of asterisks for each year from the user
for year, population in zip(years, populations):
    bars = population // ASTERISK
    print(f"{year} {'*' * bars}")
