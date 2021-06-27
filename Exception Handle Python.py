# We look for exception handling in python

print("\n A syntax error means any error in our code like missing semicolen in java statements\n")
print("\n Exception is an error that occurs at Run time i.e. users get that error\n")

# If an exception is expected in our code we use an 'try' 'except' methods. instead try catch in java

try:
    num = int(input("\nEnter two number for division\n"))
    num2 = int(input())
    res = num / num2
    print(str(num) + " / " + str(num2) + " = " + str(res))
except ZeroDivisionError:
    print("zero not divisible Enter rather than zero")
