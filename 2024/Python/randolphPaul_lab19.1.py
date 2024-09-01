# Randolph Paul 4/30/2024 randolphPaul_lab19
"""The purpose of this program is to determine whether a range of numbers
up to a user's input is prime or composite"""


def read_popular_names(file_name):
    try:
        with open(file_name, 'r') as file:
            names = file.readlines()
            names = [name.strip().lower() for name in names]
        return names
    except FileNotFoundError:
        print("File not found.")
        return []


def search_name(names, name):
    if name in names:
        print(f"{name} is among the most popular names.")
        return True
    else:
        print(f"{name} is not among the most popular names.")
        return False


def main():
    boys_names = read_popular_names("boys_names.txt")
    girls_names = read_popular_names("girls_names.txt")
    boys_tested = 0
    girls_tested = 0
    boys_found = 0
    girls_found = 0

    while True:
        search_input = input("Enter a name to search for (press enter to skip, type 'quit' to exit): ").strip().lower()
        if search_input == 'quit':
            break
        elif search_input == '':
            continue

        is_boy_name = search_input in boys_names
        is_girl_name = search_input in girls_names

        if is_boy_name:
            boys_tested += 1
            if search_name(boys_names, search_input):
                boys_found += 1
        if is_girl_name:
            girls_tested += 1
            if search_name(girls_names, search_input):
                girls_found += 1

    print("\nSearch results:")
    print(f"Boys' names tested: {boys_tested}, found: {boys_found}")
    print(f"Girls' names tested: {girls_tested}, found: {girls_found}")


if __name__ == "__main__":
    main()