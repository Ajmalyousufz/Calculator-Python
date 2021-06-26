print("This is testing of for while loop")

limit = input("\nEnter number loop limit\n")

limit = int(limit)

# while loop

# 1,2,3,4,...,limit
i = 0

while i < int(limit):
    i = i + 1
    print(i)

# for loop

# 2,4,6,....limit

print("\nPrinting even numbers using for loop\n")

for x in range(2, limit, 2):
    print(x)
