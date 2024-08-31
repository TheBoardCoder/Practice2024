# Randolph Paul 4/23/2024 randolphPaul_lab18
# The purpose of this program is to experiment with exception handling

# Calculate the average number in the file
def calculate_average(file_name):
    try:
        with open(file_name, 'r') as file:
            numbers = []
            for line in file:
                try:
                    number = float(line.strip())
                    numbers.append(number)
                except ValueError:
                    print(f"\nError: '{line.strip()}' is not a valid number.")
            if numbers:
                average = int(sum(numbers) / len(numbers))
                return average
            else:
                print("\nNo valid numbers found in the file.")
                return None
    except IOError:
        print(f"\nError: File '{file_name}' not found.")
        return None


# Run the main program
def main():
    file_name = "exceptionNumbers.txt"
    average = calculate_average(file_name)
    if average is not None:
        print(f"\nThe average of the numbers in '{file_name}' is: {average:,}")


# Entry point of the program
if __name__ == "__main__":
    main()
