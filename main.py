name = input("Welcome to Angus's Choose Your Own Adventure Game! Please enter your name: ")
print(name + ", welcome to the adventure!\n")

direction = input("First, you must choose a path! Left turn or right turn? ")
while direction.lower() != "left turn" and direction.lower() != "left" and direction.lower() != "right turn" and direction.lower() != "right":
  print("\nInvalid input. Please try again: ")
  direction = input("First, you must choose a path! Left turn or right turn? ")

if direction.lower() == "left turn" or direction.lower() == "left":
  print("\nYou have encountered a dragon!")
  attack = input("Choose fire or water to use against the dragon: ")

  while attack.lower() != "fire" and attack.lower() != "water":
    print("\nInvalid input. Please try again: ")
    attack = input("Choose fire or water to use against the dragon: ")

  if attack.lower() == "water":
    print("\nYou have defeated the dragon and brought peace to the village!")
    print("--------------------------")
  else:
    print("\nFire didn't work! Unfortunately, your adventure has come to an end.")
    print("--------------------------")
else:
  print("\nYou encounter a beggar on the side of the road!")
  choice = input("Do you give some of your food to the beggar (Yes/No)? ")

  while choice.lower() != "yes" and choice.lower() != "no":
    print("\nInvalid input. Please try again: ")
    choice = input("Do you give some of your food to the beggar (Yes/No)? ")

  if choice.lower() == "yes":
    print("\nThe beggar is actually the world's overseer, and thanks to your kindness, has returned the world back to a peaceful state!")
    print("--------------------------")
  else:
    print("\n\nThe beggar is actually the world's overseer, and because of your selfishness, the world will continue to be bleak into the unforeseeable future.")
    print("--------------------------")