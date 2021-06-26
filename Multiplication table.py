# Here we create a multiplication table that receives number from user and terminal display the multiplication table of
# that number till 10

print("\n Multiplication Table\n")

num = int(input("Enter a number\n"))

rang = int(input("Enter table limit\n"))

for x in range(1, rang + 1):
    result = x * rang
    print(str(x) + " * " + str(num) + " = " + str(result))

