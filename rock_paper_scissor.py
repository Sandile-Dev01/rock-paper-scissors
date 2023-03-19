import random

user_wins = 0
computer_wins = 0
draws = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit. ").lower()
    
    #check if user input is Q or not
    if user_input == "q":
        break

    #If users input is in or not this list
    if user_input not in options:
        print("Write a valid option")
        continue

    random_number = random.randint(0, 2)
    #rock: 0, paper: 1, scissors: 2
    
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    #User input winning conditions
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == computer_pick:
        print("It's a draw, pick again")
        draws += 1

    else:
        print("You lost")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times." )
print("You played draw", draws, "times with the computer.")

if user_wins > computer_wins or user_wins and draws > computer_wins :
    print("You won this round. Goodbye :)")

#Draw condition
elif user_wins == computer_wins:
    print("This round ended in a tie. Goodbye :)")

else:
    print("You lost this round. Goodbye :(")


