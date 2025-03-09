import random

# Ask for the users name, greets the user
name = input("What is your name, new student? \n")
gender = input("Are you a boy or a girl? \n(Type 'girl' or 'boy'): \n").strip().lower()
if gender == "boy":
    prefix = "Mr."
elif gender == "girl":
    prefix = "Ms."    
print(f"Welcome to the school for good and evil {prefix} {name}")
# Show intro about the world
# Select wether good or evil
status = input("Are you good or evil? Or would you rather let fate decide? \n(Type 'good', 'evil', or 'fate'): \n").strip().lower()
if status == "good":
    print(f"Welcome to the school for good {prefix} {name}.")
elif status == "evil":
    print(f"Welcome to the school for evil {prefix} {name}.")
elif status == "fate":
    status = random.randint(1, 2)
    if status == 1:
        status = "good"
        print(f"Welcome to the school for good {prefix} {name}.")
    elif status == 2:
        status = "evil"
        print(f"Welcome to the school for evil {prefix} {name}.")
# Select talent/traits
    # Talents for good: Animal communication, sword talent, charisma, magic adept
    # Traits for evil: Beast communication, potion master, charisma, curse adept
# Think of further features
