import random

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
status = int(input("Are you good or evil? \n1. Good \n2. Evil \n3. I don't know, let fate decide \n(Pick 1-3) \n"))
if status == 1:
    print(f"Welcome to the school for good {prefix} {name}.")
elif status == 2:
    print(f"Welcome to the school for evil {prefix} {name}.")
elif status == 3:
    status = random.randint(1, 2)
    if status == 1:
        print(f"Welcome to the school for good {prefix} {name}.")
    elif status == 2:
        print(f"Welcome to the school for evil {prefix} {name}.")
# Select talent/traits
# Think of further features
