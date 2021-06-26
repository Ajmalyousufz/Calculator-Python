# Functions

print("\nFunctions in pythons\n")


# simple function i.e. without parameter and without return value
def hey():
    print("hey i am ajmal")


hey()


# Function with parameter

def name(name):
    print("Your name is " + name)


name("Ajmal")

value = 'Muhammed ajmal y'

name(value)


# Function with parameter and return value

def sum(a, b):
    return a + b


x = sum(3, 5)

print(sum(3, 8))
print(x)


# Function with retun value

def result():
    a = 3
    b = 5
    return a + b


print(result())
