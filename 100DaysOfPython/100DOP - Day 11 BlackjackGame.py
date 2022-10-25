import random
from replit import clear
from blackjackArt import logo


############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
# https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.


# Hint 5: Deal the user and computer 2 cards each using deal_card() and append()


# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.
# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

def deal_card(reciever, number_of_cards):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    for i in range(0, number_of_cards):
        reciever.append(cards[random.randint(0, len(cards) - 1)])

    return reciever


# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.
# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().


def calculate_Score(cards_for_checking):
    # sum cards
    sum_cards = sum(cards_for_checking)

    # check for blackjack and return 0 if blackjack
    if sum_cards == 21:
        sum_cards = 0

    # check for over 21 and if has ace then reduce by 10
    if sum_cards > 21:
        for card in cards_for_checking:
            if card == 11:
                cards_for_checking.remove(11)
                cards_for_checking.append(1)
                sum_cards = sum(cards_for_checking)

    # return score
    return sum_cards


def turn_ending_score(score):
    if score > 21:
        return True
    elif score == 21 or score == 0:
        return True


def compare(userScore, dealerScore):
    if userScore == dealerScore:
        return "Draw"
    elif userScore == 0 or dealerScore > 21:
        return "Player Wins"
    elif dealerScore == 0 or userScore > 21:
        return "House Wins"
    elif dealerScore > userScore:
        return "House Wins"
    else:
        return "Player Wins"


# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.


# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


def blackjack():
    is_a_winner = False
    playerCards = []
    dealerCards = []

    print(logo)
    ## deal 2 cards each
    playerCards = deal_card(playerCards, 2)
    dealerCards = deal_card(dealerCards, 2)

    print(
        f"The Game Starts. You have {playerCards} and across the table you can see one of the dealers cards [{dealerCards[0]}]")

    ## find the score
    playerScore = calculate_Score(playerCards)
    dealerScore = calculate_Score(dealerCards)

    ##check the score for initial blackjacks

    if dealerScore == 0 or playerScore > 21:
        print("Dealer Wins")
        is_a_winner = True
    elif playerScore == 0 or dealerScore > 21:
        print("Player Wins")
        is_a_winner = True

    ## give more cards
    hit_me = input(f"Would you like another card?\n>>>")

    while hit_me == "yes":
        # deal Cards
        playerCards = deal_card(playerCards, 1)
        # calculate Scores
        playerScore = calculate_Score(playerCards)

        # check score isnt a winner or loser
        if playerScore > 21:
            print("You're over 21, You lose")
            break
        elif playerScore == 0:
            print("Player Wins")
            break

        hit_me = input(f"your score is: {playerScore}, with the cards {playerCards}. Would you like another card?\n")

    if playerScore < 21:
        while dealerScore < 17 and dealerScore != 0:
            dealerCards = deal_card(dealerCards, 1)
            dealerScore = calculate_Score(dealerCards)
            print("The Dealer takes a card")
            print(f"The Dealer now has {dealerCards}")

    print(f"The Dealers score is: {dealerScore}, with the cards {dealerCards}")
    print(f"Your score is: {playerScore}, with the cards {playerCards}.")
    print(compare(playerScore, dealerScore))

    finishedPlaying = input("Are you finished playing? \n >>>")
    if finishedPlaying == "no":
        clear()
        blackjack()


blackjack()