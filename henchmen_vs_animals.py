# Initialize list of henchmens, complete with health, movesets, and special talents
henchmen = {
    # All stats when combined must be equal to 300 for balance
    "Ogre": {"health": 120, "strength": 150, "speed": 30}, # Special talent: Has a chance to reduce the opponent's damage significantly
    "Goblin": {"health": 80, "strength": 80, "speed": 140}, # Special talent: Can multiply (Limit this)
    "Banshee": {"health": 100, "strength": 80, "speed": 120}, # Special talent: Is hard to hit 
    "Werewolve": {"health": 100, "strength": 100, "speed": 100}, # Special talent: Has a chance to increase all stats when full moon
    # Add more henchmens in the future
}

# Asks user to pick which henchmen to pick
while True:
    print("Pick your henchman:", ", " .join(henchmen.keys()))
    henchman_choice = input("Enter your henchman's name: ").strip().title()

    if henchman_choice in henchmen:
        ally_stats = henchmen[henchman_choice]
        print(henchman_choice, ally_stats)

        # Assigned values got from dictionary
        health = ally_stats.get("health")
        strength = ally_stats.get("strength")
        speed = ally_stats.get("speed")

        # To see if it works
        print(f"Health: {health}")
        print(f"Strength: {strength}")
        print(f"Speed: {speed}")

        break
    
    else:
        ("Invalid choice, please pick only from the choices.")
# Do a turn based battle that users can have fun with
# Possibly add moves by user that is not among the movesets of the henchmen (do this later)
# Do the same for animal allies (for good)