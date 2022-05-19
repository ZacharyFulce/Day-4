rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

userInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
playerHand = ""
computer = random.randint(0, 2)
computerHand = ""

if userInput == 0:
    playerHand = rock
elif userInput == 1:
    playerHand = paper
elif userInput == 2:
    playerHand = scissors
print(f"Player:\n {playerHand}")

if computer == 0:
    computerHand = rock
elif computer == 1:
    computerHand = paper
elif computer == 2:
    computerHand = scissors
print(f"Computer: {computerHand}")

if userInput == 0 and computer == 2:
    print("You win!")
elif computer > userInput:
    print("You lose.")
elif computer == userInput:
    print("Tied")
else:
    print("You win!")