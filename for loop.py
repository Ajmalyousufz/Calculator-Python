# Here we looking the working of for loop

print("Working of for loop")

skills = ["c.f", "java.f", "python.f", "html.f", "css.f", "javaScript.f", "Bootstrap.f", "jquery.f", "android.f"]

print("\nName : Muhammed Ajmal y\nFullStack Android Developer and Web Developer\n\nSkills :")

for x in skills:
    print(x)
print(skills)

# How excepting last extensions

for x in skills:
    print(x[0:-2])
    print(x.replace(".f", ".t"))
