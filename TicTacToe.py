from os import system
import time
from math import inf as infinity

Board = ["_", "_", "_",   "_", "_", "_",   "_", "_", "_"]

def printBoard(Board):
    print("|-------------|")
    print("| ", Board[0], "|", Board[1], "|", Board[2], " ")
    print("|-------------|")
    print("| ", Board[3], "|", Board[4], "|", Board[5], " ")
    print("|-------------|")
    print("| ", Board[6], "|", Board[7], "|", Board[8], " ")
    print("|-------------|")


def calculate(State):
    if winner(State, "0"):
        score = 1
    elif winner(State, "X"):
        score = -1
    else:
        score = 0

    return score


def availablePlaces(Board):
    places = []
    for i,j in enumerate(Board):
        if j == "_":
            places.append(i)

    return places


def winner(State, Player):
    winningState = [ [State[0], State[1], State[2]],  [State[3], State[4], State[5]],  [State[6], State[7], State[8]],  [State[0], State[3], State[6]],  [State[1], State[4], State[7]],  [State[2], State[5], State[8]],  [State[0], State[4], State[8]],  [State[2], State[4], State[6]] ]

    if [Player, Player, Player]  in  winningState:
        return True
    else:
        return False


def gameOver(State):
    return winner(State, "X") or winner(State, "0")


def clean():
    system('clear')


def humanTurn(Board):
    places = len(availablePlaces(Board))

    if places == 0 or gameOver(Board):
        return

    while True:
        clean()
        print("Human Turn \n")
        printBoard(Board)
        place = int(input("Enter position (1..9): "))

        if place <=9 and place >=1:
            if Board[place-1] == "_":
                Board[place-1] = "X"
                printBoard(Board)
                return

            else:
                print("This position is not free \n")
                time.sleep(2)

        else:
            print("Bad position entered \n")
            time.sleep(2)


def AISolver(Board, Places, Player):
    if Player == "0":
        best = [-1, -infinity]
    else:
        best = [-1, infinity]

    if Places == 0  or gameOver(Board):
        score = calculate(Board)
        return [-1, score]
    
    for place in availablePlaces(Board):
        Board[place] = Player

        if Player == "0":
            score = AISolver(Board, Places-1, "X")
    
        else:
            score = AISolver(Board, Places-1, "0")

        Board[place] = "_"
        score[0] = place

        if Player == "0":
            if best[1] < score[1]:
                best = score
            
        else:
            if best[1] > score[1]:
                best = score

    return best
    

def AITurn():
    places = len(availablePlaces(Board))

    if places == 0 or gameOver(Board):
        return

    clean()

    print("AI Turn \n")
    place = AISolver(Board, places, "0")
    Board[place[0]] = "0"
    printBoard(Board)
    time.sleep(1)
    

def main(Board):
    while len(availablePlaces(Board)) > 0  and  not gameOver(Board):
        humanTurn(Board)
        AITurn()

    if winner(Board, "X"):
        print("Human Won!")
        return 0

    elif winner(Board, "0"):
        print("AI Won!")
        return 0

    else:
        print("Game Draw \n")
        return 0

        
if __name__ == "__main__":
    while True:
        main(Board)
        Board = ["_", "_", "_",   "_", "_", "_",   "_", "_", "_"]
        playAgain = input("Play again? [y/n] : ")
        if playAgain == "n":
            break
