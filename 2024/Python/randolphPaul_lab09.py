# Randolph Paul 4/3/2024 randolphPaul_lab09
# The purpose of this program is to uses loops to display 2 different patterns.

# Set constants
NEGATIVE_ONE = -1
ZERO = 0
ONE = 1
TEN = 10
ELEVEN = 11

# Display pattern A
print("\nPattern A\n")
for i in range(ONE, ELEVEN):
    for j in range(ONE, i + ONE):
        print("+", end="")
    print()

# Display pattern B
print("\nPattern B\n")
for i in range(TEN, ZERO, NEGATIVE_ONE):
    for j in range(ONE, i + ONE):
        print("+", end="")
    print()
