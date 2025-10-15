import random

def check_win(user, computer):
    # Returns 1 if user wins, -1 if computer wins, 0 if it's a tie
    if user == computer:
        return 0
    elif (user == 's' and computer == 'w') or \
         (user == 'w' and computer == 'g') or \
         (user == 'g' and computer == 's'):
        return 1
    else:
        return -1

def get_computer_choice():
    return random.choice(['s', 'w', 'g'])

def main():
    print("Welcome to Snake Water Gun Game!")
    print("Enter 's' for Snake, 'w' for Water, 'g' for Gun")
    
    user_choice = input("Your turn: ").lower()
    if user_choice not in ['s', 'w', 'g']:
        print("Invalid input! Please enter 's', 'w' or 'g'.")
        return
    
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = check_win(user_choice, computer_choice)

    if result == 0:
        print("It's a tie!")
    elif result == 1:
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    main()
