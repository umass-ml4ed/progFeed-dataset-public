print("Pokemon Finder.")
typechoice = input("What type do you desire? (Fire, Water.): ")
genchoice = input("Now, what generation do you desire? (First, Second.): ")
evochoice = input("Finally, which evolution form do you desire? (First, Second.): ")

if typechoice == "Fire" and genchoice == "First" and evochoice == "First":
    pokemon = "Charmander!"
elif typechoice == "Fire" and genchoice == "First" and evochoice == "Second":
    pokemon = "Charmander2!"
elif typechoice == "Fire" and genchoice == "Second" and evochoice == "First":
    pokemon = "Charmander3!"
else: print("Please try again.")
print(pokemon)