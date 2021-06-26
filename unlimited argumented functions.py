# Here look for how to add unlimited arguments in python

print("Unlimited Argument function in python")


def names(*values):
    print("first value = " + values[0] + "\nSecond Value = " + str(values[1]) + "\nThird value = " + values[2])


names("Muhammed Ajmal y", 25, "Android Developer")

x = 1


def jf():
    print(x)
    # x = x + 1 This line is error in here i.e. cant assign global variable in functions same variable


# Without argument order we can pass parameters

def sample(a, b, c):
    print("first value : " + a + "\nSecond Value : " + b + "\nThird value :" + c)


sample(b="Ajmal", a="Muhammed", c="Yousuf")
