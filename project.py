import random

choices = ["rock", "paper", "scissor"]

def CheckWinner(playerSelection, computerSelection):
    outcomes = {
        ("rock", "scissor"): "You win!",
        ("paper", "rock"): "You win!",
        ("scissor", "paper"): "You win!",
        ("rock", "paper"): "You lose!",
        ("paper", "scissor"): "You lose!",
        ("scissor", "rock"): "You lose!",
    }
    if playerSelection == computerSelection:
        return "It's a tie!"
    return outcomes.get((playerSelection, computerSelection), "")

def Start():
    while True:
        playerSelection = input("rock, paper, or scissor?: ")
        if playerSelection not in choices:
            print("Please enter a valid choice.")
            continue
        
        computerSelection = random.choice(choices)
        print("Computer:", computerSelection)
        print("Player:", playerSelection)
        
        result = CheckWinner(playerSelection, computerSelection)
        print(result)
        
        play_again = input("Play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
    
    print("Bye!")

Start()
