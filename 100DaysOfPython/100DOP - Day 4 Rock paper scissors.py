from random import randint

games = int(input("How many games do you want to play?>> "))
playerPoints = 0
computerPoints = 0
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
while games >= 1 :
    playerChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    computerChoice = randint(0,2)
    gameImages = [rock, paper, scissors]

    if playerChoice > 2:
        print("Invalid number")
    else:
        print(gameImages[playerChoice])
        print(gameImages[computerChoice])


        # if playerChoice > 2:
        #     print("Invalid number")
        # elif playerChoice == 0 and computerChoice == 2:
        #     print("You Win")
        # elif playerChoice == 2 and computerChoice == 0:
        #     print("You Lose")
        # elif computerChoice > playerChoice:
        #     print("You Lose")
        # elif playerChoice > computerChoice:
        #     print("You Win")
        # elif computerChoice == playerChoice:
        #     print("It's a draw")

    if computerChoice == playerChoice:
        print("A draw")
    elif computerChoice == 2 and int(playerChoice) == 1 or computerChoice == 1 and int(playerChoice) == 0 or computerChoice == 0 and int(playerChoice) == 2:
        print("You Lose.HA")
        games -= 1
        computerPoints += 1
    else:
        print("You win")
        games -= 1
        playerPoints += 1
    print(f"You have {playerPoints} points, the computer has {computerPoints} points")

