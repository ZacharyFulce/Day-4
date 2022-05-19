import random

names_split = input("Give me everyone's name separated by a comma.\n")
names = names_split.split(", ")
listLength = len(names)
billPayer = names[random.randint(0, listLength-1)]
print(f"{billPayer} is going to pay for the bill today!")

randomChoice = random.choice(names)
print(f"{randomChoice} is going to pay for the bill today!")

