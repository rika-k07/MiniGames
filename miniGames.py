import random
#taking input
while True:
    choose=input("\nDo you want to play the games? yes/no: ")
    if choose =="yes":
        choice=int(input("Enter 1,2 or 3 to choose which game you want to play\n1:HANGMAN\n2:TIC TAC TOE\n3:ROCK PAPER SCISSORS\n"))

#hangman        
        if choice==1:
            words = ["komala", "mango", "kitten", "elephant", "fish", "icecream", "python", "snake", "komi"]
            word = random.choice(words)
            guessed = ["_"] * len(word)
            attempts = 6
            guessed_letters = []

            print("Welcome to a simple Hangman game")
            print("Guess the word")
            print(" ".join(guessed))

            while attempts > 0 and "_" in guessed:
                guess = input("\nEnter a letter: ").lower()

                if not guess.isalpha() or len(guess) != 1:
                    print("Please enter only one alphabet letter")
                    continue

                if guess in guessed_letters:
                    print("You've already guessed that letter")
                    continue

                guessed_letters.append(guess)

                if guess in word:
                    print("Correct!")
                    for i in range(len(word)):
                        if word[i] == guess:
                            guessed[i] = guess
                else:
                        attempts -= 1
                        print("Wrong! Attempts left:", attempts)

                print(" ".join(guessed))

            if "_" not in guessed:
                print("\nCongratulations! You win ")
                print("The word was:", word)
            else:
                print("\nBetter luck next time ")
                print("The word was:", word)



#tic tac toe
#not using random module in this code(play with another person)
        if choice==2:
            board=["-","-","-",
                    "-","-","-",
                    "-","-","-"]
            currentPlayer="X"
            winner=None
            gameRunning=True

            def printBoard(board):
                print(board[0] +" | "+board[1]+" | "+board[2])
                print(board[3] +" | "+board[4]+" | "+board[5])
                print(board[6] +" | "+board[7]+" | "+board[8])
        
            def playerInput(board):
                inp=int(input("enter no. from 1-9: ")) 
                if inp>=1 and inp<=9 and board[inp-1]=="-": 
                    board[inp-1]=currentPlayer
                else:
                    print("Oops enter a valid number")

            def checkHorizontle(board):
                global winner
                if board[0]==board[1]==board[2] and board[0]!="-":
                    winner=board[0]
                    return True
                elif board[3]==board[4]==board[5]and board[5]!="-":
                    winner=board[3]
                    return True
                elif board[6]==board[7]==board[8]and board[6]!="-":
                    winner=board[6]
                    return True

            def checkRow(board):
                global winner
                if board[0]==board[3]==board[6] and board[0]!="-":
                    winner=board[0]
                    return True
                elif board[2]==board[5]==board[8]and board[2]!="-":
                    winner=board[2]
                    return True
                elif board[1]==board[4]==board==[7] and board[1]!="-":
                    winner=board[1]
                    return True

            def checkDiag(board):
                global winner
                if board[0]==board[4]==board[8] and board[0]!="-":
                    winner=board[0]
                    return True
                elif board[2]==board[4]==board[6] and board[2]!="-":
                    winner=board[2]
                    return True

            def checkTie(board):
                global gameRunning
                if "-" not in board:
                    printBoard(board)
                    print("It's a tie!")
                    gameRunning=False

            def checkwin():
                global gameRunning
                if checkDiag(board) or checkHorizontle(board) or checkRow(board):
                    printBoard(board)
                    print(f"The winner is {winner}")
                    gameRunning=False
    
            def switchPlayer():
                global currentPlayer
                if currentPlayer=="X":
                    currentPlayer="O"
                else:
                    currentPlayer="X"

            while gameRunning:
                printBoard(board)
                playerInput(board)
                checkwin()
                checkTie(board)
                switchPlayer()
        
#rock paper scissors game
        if choice==3:
            def rock_paper_scissors():
                print("ROCK PAPER SCISSORS GAME")
                print("Rules:")
                print("Rock beats Scissors")
                print("Scissors beats Paper")
                print("Paper beats Rock")
                print("-----------------------------")

            choices = ["rock", "paper", "scissors"]

            while True:
                user_choice = input("Enter rock, paper, or scissors: ").lower()

                if user_choice not in choices:
                    print("Invalid choice! Try again.\n")
                    continue

                computer_choice = random.choice(choices)

                print(f"You chose: {user_choice}")
                print(f"Computer chose: {computer_choice}")

                if user_choice == computer_choice:
                    print("It's a tie!")
                    break
                elif ((user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock")):
                    print("You win!")
                    break
                else:
                    print("Computer wins!")
                    break
    if choose =="no":
        print("Come again someother time to play :)")


































































































    




    








