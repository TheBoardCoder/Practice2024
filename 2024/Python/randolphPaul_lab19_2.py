# Randolph Paul 4/30/2024 randolphPaul_lab19
"""The purpose of this program is to displays how many
girl or boy names are found in 2 files from user guesses"""


# Open the file
def load_names(file_name):
    with open(file_name, 'r') as file:
        names = [line.strip().lower() for line in file]
    return names


# Search names
def search_names(names, search_name):
    if search_name.lower() in names:
        return True
    return False


# Run the main program
def main():
    print("""\nThis program displays how many girl or boy names are found in 2 files from user guesses.""")
    boy_names = load_names('BoyNames.txt')
    girl_names = load_names('GirlNames.txt')
    girl_names_found = 0
    boy_names_found = 0
    names_tested = 0

    while True:
        search_name = input("\nPlease enter a name to search for (press 0 to exit): ")
        if search_name.replace(" ", "") == '':
            continue
        elif search_name == '0':
            break
        names_tested += 1
        search_name = search_name.lower()
        if search_name in boy_names:
            print(f"{search_name.capitalize()} is among the boy names.")
            boy_names_found += 1
        else:
            print(f"{search_name.capitalize()} is not among the boy names.")

        if search_name in girl_names:
            print(f"{search_name.capitalize()} is among the girl names.")
            girl_names_found += 1
        else:
            print(f"{search_name.capitalize()} is not among the girl names.")
    print(f"Number of boy names found: {boy_names_found:,}")
    print(f"Number of girl names found: {girl_names_found:,}")
    print(f"Number of boy and girl names tested: {names_tested:,}")


# Start the main program
if __name__ == "__main__":
    main()
