# String letters count

name = input("\n Enter your name\n")

print("\n Your name is " + name)

print("\n Letters count in your name : " + str(len(name)))

# 'n'th letter in string

print("\n Enter any number under " + str(len(name)+1))

number = input()

if int(number) > 20 or int(number) <= 0:
    print("\nEnter a valid number\n")
else:
    print("\n '" + name[int(number)-1] + "' is " + number + "th letter of your name")

print("\n Testing....\n" + name[2:17])
