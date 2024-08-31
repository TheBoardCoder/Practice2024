# Randolph Paul 4/22/2024 randolphPaul_lab17
# The purpose of this program is experiment with using the try keyword


# Check to see if the user's input is a number
def is_number(input_string):
    try:
        float(input_string)
        return True
    except ValueError:
        return False


# Run the main program
def main():
    print("\nThis program checks if a value that a user inputs is a number.")
    while True:
        input_string = input("\nEnter a value (press Enter to exit): ")
        if not input_string:
            print("Exiting the program")
            break
        if is_number(input_string):
            print(f"'{input_string}' is a valid number.")
        else:
            print(f"'{input_string}' is not a valid number.")


# Entry point of the program
if __name__ == "__main__":
    main()
