# Saturday night fun time - rock paper scissors game 

# Import modules
import random
import time

# Keep track of user and computer score
userScore = 0
computerScore = 0
# Keep track of rounds
roundCount = 0

# List of possible options to pick from in the game
listOfOptions = ["rock", "paper", "scissors"]

while True:

    # Prompt user for Rock, Paper or Scissors
    userSelection = input("Type 'rock', 'paper' or 'scissors' or 'q' to quit\n").lower()

    # Exit the program
    if userSelection == 'q':
        break
    
    # If user's input is incorrect go back to the beginning of the loop and ask again
    if userSelection not in listOfOptions: 
        continue

    # Select a random int between 0 and 2 to represent rock, paper, scissors
    randomInt = random.randint(0, 2)

    # Generate a computer pick. 0 = rock, 1 = paper, 2 = scissors
    computerSelection = listOfOptions[randomInt]

    # New round counter
    roundCount += 1
    print(f"\n*** Round {roundCount} ***")
    time.sleep(2)

    # Say who picked what
    print(f"User picked {userSelection}. Computer picked {computerSelection}.")

    # Declare the winner based on scenarios
    if userSelection == 'rock' and computerSelection == 'scissors':
        userScore += 1
        print(f"User won.")
    elif userSelection == 'paper' and computerSelection == 'rock':
        userScore += 1
        print(f"User won.")
    elif userSelection == 'scissors' and computerSelection == 'paper':
        userScore += 1
        print(f"User won.")
    elif userSelection == computerSelection:
        print("Draw! No change in points.")
    else: 
        computerScore += 1
        print("Computer won.")

    time.sleep(2)
    print(f"\nThe score is User: {userScore}, Computer: {computerScore}.\n")
    time.sleep(2)

print("Thanks for playing!")

# Made with love.
# Check out Harry Mack on YouTube. 
# Have a great day.