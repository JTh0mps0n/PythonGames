from DinosaurGame import *

def printMenu():
    print('\n' * 5)
    print("Welcome to Game Selection")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~ 1. Hangman (Console)      ~")
    print("~ 2. Dinosaur Game (Window) ~")
    print("~ 3. Color Wheel (Window)   ~")
    print("~ q. quit                   ~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()

def hangman():
    print("Launching Hangman")


def colorWheel():
    print("Launching Color Wheel")


def menu():
    validInputs = ["q", "1", "2", "3"]
    userInput = '0'
    while userInput != 'q':
        printMenu()
        userInput = input("Please enter the game you would like to play(1, 2, 3, q): ")
        while userInput not in validInputs:
            print()
            print("Invalid input. Must be '1', '2', '3', or 'q'.")
            userInput = input("Please enter the game you would like to play(1, 2, 3, q): ")

        if(userInput == '1'):
            hangman()
        elif(userInput == '2'):
            dinosaurGame()
        elif(userInput == '3'):
            colorWheel()
        elif(userInput == 'q'):
            break


    print("\n"*5)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~    Thanks for playing!    ~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #menu()
    dinosaurGame()
