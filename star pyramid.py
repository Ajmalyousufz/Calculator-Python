# Creating star pyramid

print("Star pyramid\n")

limit = int(input("Enter pyramid hight limit\n"))

x = 0
y = 0

while x < limit:

    z = x
    while z < limit:
        print(" ", end="")
        z = z + 1
    y = x
    while y >= 0:
        print("* ", end="")
        y = y - 1
    print("\n")
    x = x + 1
