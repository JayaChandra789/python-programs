import random  #The random module in Python is used for generating random numbers. 

def get_user_choice(): #def keyword
    user_input = input("Enter your choice (rock, paper, scissors): ").lower() #input from user
    if user_input in ['rock', 'paper', 'scissors']:
        return user_input
    else:
        print("Invalid choice. Please try again.")
        return get_user_choice()
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)
if __name__ == "__main__": #play_game() would be called only when you run the script directly from the command line
    play_game()
