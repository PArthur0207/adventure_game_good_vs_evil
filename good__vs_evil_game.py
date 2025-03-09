# Ask for the users name, greets the user
name = input("What is your name new student? \n")
gender = int(input("Are you a boy or a girl? \n1. Boy \n2. Girl \n(Pick 1 or 2): "))
if gender == 1:
    prefix = "Mr."
elif gender == 2:
    prefix = "Ms."    
print(f"Welcome to the school for good and evil {prefix} {name}")
# Show intro about the world
# Select wether good or evil
# Select talent/traits
# Think of further features
