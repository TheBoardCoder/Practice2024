# Randolph Paul 4/30/2024 randolphPaul_lab20
"""The purpose of this program is to determine whether a range of numbers
up to a user's input is prime or composite"""


# Determine if prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Test numbers
def test_numbers_up_to(num):
    numbers = list(range(2, num + 1))
    for n in numbers:
        if is_prime(n):
            print(f"{n:,} is a prime number.")
        else:
            print(f"{n:,} is a composite number.")


# Run the main program
def main():
    print("""\nThis program determines whether a range of numbers 
up to a user's input is prime or composite""")
    while True:
        try:
            num = int(input("\nPlease enter a positive integer greater than 1 (enter a negative number to quit): "))
            if num < 0:
                break
            if num <= 1:
                print("Please enter a number greater than 1.")
                continue
            test_numbers_up_to(num)
        except ValueError:
            print("\nError: Not a valid number")


# Start the main program
if __name__ == "__main__":
    main()
