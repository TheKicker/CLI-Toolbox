import random

def spin_wheel():
    return random.randint(0, 36)

def get_color_from_number(number):
    if number == 0:
        return "green"
    elif number % 2 == 0:
        return "red"
    else:
        return "black"

def get_bet_type():
    while True:
        try:
            print("1. Bet on a number")
            print("2. Bet on a color")
            print("3. Bet on a number and a color")
            choice = int(input("Select your bet type: "))
            
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_number():
    while True:
        try:
            number = int(input("Enter the number you're betting on (0-36): "))
            if 0 <= number <= 36:
                return number
            else:
                print("Invalid number. Please enter a number between 0 and 36.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_color():
    while True:
        color = input("Enter the color you're betting on (red/black/green): ").strip().lower()
        if color in ["red", "black", "green"]:
            return color
        else:
            print("Invalid color. Please enter 'red', 'black' or 'green'.")

def get_amount(player_money):
    while True:
        try:
            amount = int(input("Enter the amount of money to bet: "))
            if 0 < amount <= player_money:
                return amount
            else:
                print("Invalid amount. Please enter a valid amount within your balance.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("\n----------------------------------------------------------------")
    print("                ♠♣♥♦ WELCOME TO ROULETTE! ♠♣♥♦")
    print("")
    print("----------------------------------------------------------------")
    print(
        "Game Rules:\n\
        The table features numbers 0 to 36\n\
        Red are odd, Black are even, Green is zero.\n\
        Bet a Number (Bet x 36), a Color (Bet x 2.5), or a Number and a Color (Bet x 72)."
    )
    player_money = 1000
    
    while player_money > 0:
        print(f"\nYour current balance: ${player_money}")
        bet_type = get_bet_type()
        bet_amount = get_amount(player_money)
        
        winning_number = spin_wheel()
        winning_color = get_color_from_number(winning_number)
        
        if bet_type == 1:  # Bet on a number
            bet_number = get_number()
            player_money -= bet_amount
            if bet_number == winning_number:
                winnings = bet_amount * 36
                print(f"The ball landed on {winning_number} ({winning_color})")
                print(f"Congratulations! You won ${winnings}")
                player_money += winnings
            else:
                print(f"Sorry, you lost this round. The winning number was {winning_number} on {winning_color}")
        elif bet_type == 2:  # Bet on a color
            bet_color = get_color()
            player_money -= bet_amount
            if bet_color == winning_color:
                winnings = bet_amount * 2.5
                print(f"The ball landed on {winning_number} ({winning_color})")
                print(f"Congratulations! You won ${winnings}")
                player_money += winnings
            else:
                print(f"Sorry, you lost this round. The winning number was {winning_number} on {winning_color}")
        else:  # Bet on a number and a color
            bet_number = get_number()
            bet_color = get_color()
            player_money -= bet_amount
            if (bet_number == winning_number) and (bet_color == winning_color):
                winnings = bet_amount * 36 * 2
                print(f"The ball landed on {winning_number} ({winning_color})")
                print(f"Congratulations! You won ${winnings}")
                player_money += winnings
            elif (bet_number != winning_number) and (bet_color != winning_color):
                print(f"Sorry, you lost this round. The winning number was {winning_number} on {winning_color}")
            else:
                print(f"The ball landed on {winning_number} ({winning_color})")
                player_money += bet_amount
                print(f"You got one but not the other, so you got your bet of ${bet_amount} back.")
        
    print("Game over. You've run out of money.")

if __name__ == "__main__":
    main()
