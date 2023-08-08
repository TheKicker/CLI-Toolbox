import random

# Define the symbols and their probabilities
symbols = ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar"]
probabilities = [0.3, 0.2, 0.15, 0.1, 0.1, 0.15]

def spin_reel():
    return random.choices(symbols, probabilities)[0]

def display_slot(slot):
    print(" | ".join(slot))

def main():
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
        else:
            print("Sorry, no winning combination this time.")
        
        print(f"Current balance: {balance} coins\n")
    
    print("Game over. You're out of coins!")

if __name__ == "__main__":
    main()
