# Randolph Paul 4/22/2024 randolphPaul_lab15
"""The purpose of this program is to write random numbers to a file
and display information about the numbers written to the file."""

# Import random module
import random


# Write numbers to file
def write_random_numbers(file_name, count):
    with open(file_name, 'w') as file:
        file.close()
    with open(file_name, 'w') as file:
        for _ in range(count):
            number = random.randint(1, 500)
            file.write(str(number) + '\n')
    file.close()


# Read file and display numbers
def read_and_display_numbers(file_name):
    total = 0
    count = 0
    with open(file_name, 'r') as file:
        for line in file:
            try:
                number = int(line.strip())
                print(number)
                total += number
                count += 1
            except ValueError:
                pass
    file.close()
    print(f'Total: {total:,}')
    print(f'\nNumber of random numbers read: {count:,}')


# Calculate the average of the numbers in the file
def calculate_average(file_name):
    total = 0
    count = 0
    with open(file_name, 'r') as file:
        for line in file:
            try:
                number = int(line.strip())
                total += number
                count += 1
            except ValueError:
                pass
    if count > 0:
        average = total / count
        return average
    else:
        return None
    file.close()


# Find the highest and lowest number in a file
def find_highest_and_lowest(file_name):
    highest = float('-inf')
    lowest = float('inf')
    with open(file_name, 'r') as file:
        for line in file:
            try:
                number = int(line.strip())
                if number > highest:
                    highest = number
                if number < lowest:
                    lowest = number
            except ValueError:
                pass
    return highest, lowest
    file.close()


# Run the main program
def main():
    print("""\nThis program writes random numbers to a file and displays
information about the numbers written to the file.""")
    file_name = 'randomNumbers.txt'
    count = int(input('\nEnter the number of random numbers to generate: '))
    write_random_numbers(file_name, count)
    print(f'{count:,} random numbers have been written to {file_name}')
    print('\nRandom numbers:')
    read_and_display_numbers(file_name)
    average = calculate_average(file_name)
    if average is not None:
        print(f'Average of numbers read: {average:,.0f}')
    else:
        print(f'No valid numbers found in {file_name}')
    highest, lowest = find_highest_and_lowest(file_name)
    print(f'Highest number: {highest}')
    print(f'Lowest number: {lowest}')


# Entry point of the program
if __name__ == "__main__":
    main()
