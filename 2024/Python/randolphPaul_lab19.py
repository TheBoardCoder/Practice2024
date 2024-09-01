# Randolph Paul 4/30/2024 randolphPaul_lab19
# The purpose of this program is to determine whether names are in a file.


# Read names from the file
def read_names_from_file(file_name):
    names = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                names.append(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    return names


# Search for name in the list
def search_name_in_list(name, names):
    if name in names:
        return True
    else:
        return False


# Run main program
def main():
    print("""\nThis program checks whether a name is in a list of popular 
names or is in the boy or girl file.""")
    popular_names = read_names_from_file('popular_names.txt')
    boy_names = read_names_from_file('BoyNames.txt')
    girl_names = read_names_from_file('GirlNames.txt')
    pop_names_found = 0
    num_girls_tested = 0
    num_boys_tested = 0
    num_girls_found = 0
    num_boys_found = 0

    while True:
        name = input("\nPlease enter a name (press 0 to quit): ")
        if name == '0':
            break
        elif name.replace(" ", "") == '':
            continue
        else:
            name = name.lower().capitalize()

            if search_name_in_list(name, popular_names):
                print(f"'{name}' was among the most popular names.")
                pop_names_found += 1
            else:
                print(f"'{name}' was not among the most popular names.")

            if search_name_in_list(name, boy_names):
                num_boys_tested += 1
                num_boys_found += 1
            elif search_name_in_list(name, girl_names):
                num_girls_tested += 1
                num_girls_found += 1
            else:
                num_girls_tested += 1
                num_boys_tested += 1

    print("\nSearch Summary:")
    print(f"Total girls names tested: {num_girls_tested:,}")
    print(f"Total boys names tested: {num_boys_tested:,}")
    print(f"Total girls names found in GirlNames file: {num_girls_found:,}")
    print(f"Total boys names found in BoyNames file: {num_boys_found:,}")
    print(f"Total popular names found: {pop_names_found:,}")


# If main call main program
if __name__ == "__main__":
    main()
