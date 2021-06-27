# Check whether the user entered number is positive or negetive

def isPosOrNeg(num):
    if num > 0:
        print(str(num) + " is a positive number")
    elif num == 0:
        print("you Entered zero")
    else:
        print(str(num) + " is a negetive number")


print("Muhammed Ajmal y")
isPosOrNeg(int(input("Enter any number\n")))
