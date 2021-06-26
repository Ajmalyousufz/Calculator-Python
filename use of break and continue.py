# Here we look for the use of break and continue statements

print("\n USE OF BREAK AND CONTINUE STATEMENTS\n")

num = int(input("Enter a number"))

for x in range(num + 1):

    if x == 5:
        continue

    print(x)
