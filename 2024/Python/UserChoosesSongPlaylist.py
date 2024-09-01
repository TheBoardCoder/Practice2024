# Randolph Paul 5/5/2024
"""The purpose of this program is to give users the ability
to pick a platform and the number of songs in a playlist."""


# Global constants
JIM_BOB_PRICES = [3.26, 4.78, 7.33]
SUZY_BOB_PRICES = [3.41, 4.99, 7.69]
PLATFORM_CHOICE = [1, 2]
PLAYLIST_CHOICE = [1, 2, 3]
ONE = 1


# Choose the number of playlists to order
def get_playlists():
    while True:
        try:
            num_playlists = int(input("\nPlease enter the number of playlists to order: "))
            if num_playlists < ONE:
                raise ValueError("Error: Invalid number of playlists")
            break
        except ValueError as e:
            print(e)
    return num_playlists


# Choose the platform
def get_platform(playlist_num):
    while True:
        print(f"\nPlaylist {playlist_num}")
        print("1. Jim Bob's Pretty Good Music")
        print("2. Suzy Bob's Better Music")
        try:
            choice = int(input("\nChoose the platform: "))
            if choice not in PLATFORM_CHOICE:
                raise ValueError("Error: Invalid streaming platform")
            break
        except ValueError as e:
            print(e)
    return choice


# Get the length of the playlist
def get_playlist_length(playlist_num):
    while True:
        print(f"\nPlaylist {playlist_num}")
        print("1. Three Songs")
        print("2. Five Songs")
        print("3. Ten Songs")
        try:
            choice = int(input("\nChoose the playlist length: "))
            if choice not in PLAYLIST_CHOICE:
                raise ValueError("Error: Invalid playlist length")
            break
        except ValueError as e:
            print(e)
    return choice


# Calculate the cost of the playlist
def calculate_playlist_cost(platform, playlist_length):
    if platform == ONE:
        return JIM_BOB_PRICES[playlist_length - ONE]
    else:
        return SUZY_BOB_PRICES[playlist_length - ONE]


# Display the total
def display_totals(playlists, costs):
    for i in range(len(playlists)):
        print(f"Playlist {i + ONE}: {playlists[i]}, Cost: ${costs[i]:.2f}")


# Display the final total
def display_final_total(total_cost):
    print(f"Total Cost: ${total_cost:.2f}")


# Run the main program
def main():
    print("\nThis program will allow you to pick a platform and the number of songs in a playlist.")
    total_cost = 0
    playlists = []
    costs = []

    num_playlists = get_playlists()

    for i in range(num_playlists):
        platform = get_platform(i + ONE)
        playlist_length = get_playlist_length(i + ONE)
        cost = calculate_playlist_cost(platform, playlist_length)
        total_cost += cost
        playlists.append((platform, playlist_length))
        costs.append(cost)

    display_totals(playlists, costs)
    display_final_total(total_cost)


# Enter the program
if __name__ == "__main__":
    main()
