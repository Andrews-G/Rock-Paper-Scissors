import random


def main():
    options = ["rock", "paper", "scissors"]
    user_wins = 0
    computer_wins = 0    
    ties = 0
    user_input = 0
    
    while user_input != "q":
        user_input = get_input(options)
        computer_pick = computer_choice(options)
        user_wins, computer_wins, ties = determine_winner(user_input, computer_pick, user_wins, computer_wins, ties)
        
    if user_input == "q":
        final_results(user_wins, computer_wins, ties)
    
    
def get_input(options):
    
    options = ["rock", "paper", "scissors"]
    
    while True:
        user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
        if user_input in options or user_input == "q":
            break
    return user_input


def computer_choice(options):
    
    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")    
    return computer_pick
    
    
def determine_winner(user_input, computer_pick, user_wins, computer_wins, ties):
    
    if user_input == "q":
        return user_wins, computer_wins, ties
    
    else:
   
        if user_input == "rock" and computer_pick == "scissors":
            print("You won!")
            user_wins += 1
        
        elif user_input == "paper" and computer_pick == "rock":
            print("You won!")
            user_wins += 1
        
        elif user_input == "scissors" and computer_pick == "paper":
            print("You won!")
            user_wins += 1
        
        elif user_input == computer_pick:
            print("It's a tie!")
            ties += 1
        else:
            print("You lost!")
            computer_wins += 1    
            
        return user_wins, computer_wins, ties
        
    
def final_results(user_wins, computer_wins, ties):
    
    print("You won", user_wins, "time(s).")
    print("The computer won", computer_wins, "time(s).")
    if ties > 0:
        print("You tied with the computer", ties, "time(s).")
    print("Goodbye!")    
    
    
main()