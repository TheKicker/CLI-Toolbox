import random, os

# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the txt file
txt_file_path = os.path.join(script_directory, 'wallet.txt')

# Define the symbols and their probabilities
symbols = ["🍒", "🍋", "🍊", "🍔", "🍕", "🌮"]
probabilities = [0.3, 0.2, 0.15, 0.1, 0.1, 0.15]

def spin_reel():
    return random.choices(symbols, probabilities)[0]

def display_slot(slot):
    print(" | ".join(slot))

def main():
    wallet = 0
    with open(txt_file_path, "r") as file:
        for line in file:
            if line.strip():  # Skip empty lines
                number = int(line)
                wallet += number
    file.close()
    print("\n----------------------------------------------------------------")
    print("                 ♠♣♥♦ WELCOME TO SLOTS! ♠♣♥♦")
    print("")
    print("----------------------------------------------------------------")
    print(
        "Game Rules:\n\
        Get three symbols in a row to win!\n\
        Everyone begins with a wallet of 100 coins."
    )
    print("\tLifetime Winnings:", wallet, " coins")
    print("")
    
    balance = 100
    while balance > 0:
        input("Press Enter to spin the slot machine...")
        
        # Deduct the bet amount
        bet = 10
        balance -= bet
        
        # Spin the reels
        reels = [spin_reel(), spin_reel(), spin_reel()]
        display_slot(reels)
        
        # Check for winning combinations
        if reels[0] == reels[1] == reels[2]:
            winnings = bet * 5
            balance += winnings
            print(f"Congratulations! You won {winnings} coins!")
            # Write balance to the wallet.txt file
            with open(txt_file_path, "a") as file:
                file.write(f"{str(winnings)}")
                file.close()
        else:
            print("Sorry, no winning combination this time.")
            # Write balance to the wallet.txt file
            with open(txt_file_path, "a") as file:
                file.write(f"\n{str(-10)}")
                file.close()
        
        print(f"Current balance: {balance} coins\n")
    
    print("Game over. You're out of coins!")

if __name__ == "__main__":
    main()
