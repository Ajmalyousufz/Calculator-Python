# Here we look for the for loop range

print("\nEven numbers printing with your range\n")

fnum = int(input("Enter the start even number\n"))

if fnum % 2 == 0:
    print("Ok it is a even number\n")
else:
    print("Please Enter An Even number instead of odd number\n")

lnum = int(input("Enter the limit of even number tablen\n"))

for x in range(fnum, lnum + 2, 2):
    print(x)
