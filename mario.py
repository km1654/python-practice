from cs50 import get_int

height = 0
while (height < 1 or height > 8):
    height = get_int("Height: ")

for i in range(height):
    for j in range(height - 1 - i):
        print(" ", end="")
    for k in range(1 + i):
        print("#", end="")
    print("  ", end="")
    for l in range(1 + i):
        print("#", end="")
    print()
