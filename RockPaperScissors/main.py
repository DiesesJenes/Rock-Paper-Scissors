import random


def check_who_won():    # checking who won a match of Rock Paper Scissors
    global computer_score, human_score, human_player, computer_player
    if human_player == computer_player:
        print("Draw")
    elif human_player == "Paper" and computer_player == "Rock":
        human_score += 1
        print("You made a point!")
    elif human_player == "Rock" and computer_player == "Scissors":
        human_score += 1
        print("You made a point!")
    elif human_player == "Scissors" and computer_player == "Paper":
        human_score += 1
        print("You made a point!")
    else:
        computer_score += 1
        print("The Computer made a Point!")


def check_game_winner():    # checking who won the game of Rock Paper Scissors
    global computer_score, human_score
    if computer_score == 3:
        print("The computer has won!")
        return False
    elif human_score == 3:
        print("You have won!")
        return False
    else:
        return True


def display_picks():    # displaying the picks of the Computer and the Player
    global computer_player, human_player
    print("You choose '" + human_player + "' and the computer chooses '" + computer_player + "'.")


def human_pick():       # making sure, that the input is correct
    pick = input("Choose Rock, Paper or Scissors: ")
    while True:
        if pick == "Rock" or pick == "Paper" or pick == "Scissors":
            return pick
        else:
            pick = input("Please type your choice of Rock, Paper or Scissors in correctly : ")


computer_player_possibilities = ["Rock", "Paper", "Scissors"]
computer_score = 0
human_score = 0
game = True

while game:
    computer_player = random.choice(computer_player_possibilities)
    human_player = human_pick()
    display_picks()
    check_who_won()
    game = check_game_winner()

print("Thanks for playing!")
