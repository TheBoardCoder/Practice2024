# Randolph Paul 3/26/2024 randolphPaul_lab04
"""The purpose of this program is to calculate the number of hot dog packages
and hot dog bun packages needed for a cookout with the least amount of leftovers."""

# Declare constants
hot_dogs_per_package = 10
buns_per_package = 8
one = 1

# Get user input for number of people and hot dogs per person
print('''\nThis program calculates the number of hot dog packages and hot dog bun
packages needed for a cookout with the least amount of leftovers.''')

num_people = int(input("\nPlease enter the number of people attending the cookout: "))
hot_dogs_per_person = int(input("\nPlease enter the number of hot dogs each person will be given: "))

# Calculate number of hot dogs and packages needed
total_hot_dogs_needed = num_people * hot_dogs_per_person
total_hot_dog_packages_needed = (total_hot_dogs_needed + hot_dogs_per_package - one) // hot_dogs_per_package

# Calculate number of buns and packages needed
total_buns_needed = num_people * hot_dogs_per_person
total_bun_packages_needed = (total_buns_needed + buns_per_package - one) // buns_per_package

# Calculate leftovers
hot_dogs_leftover = total_hot_dog_packages_needed * hot_dogs_per_package - total_hot_dogs_needed
buns_leftover = total_bun_packages_needed * buns_per_package - total_buns_needed

# Print the results
print(f"\nMinimum number of hot dog packages required: {total_hot_dog_packages_needed:,}")
print(f"Minimum number of bun packages required: {total_bun_packages_needed:,}")
print("Number of hot dogs left over: ", hot_dogs_leftover)
print("Number of buns left over: ", buns_leftover)
