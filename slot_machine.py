import random

def spin_reels():
    symbols = ["🍒", "🍋", "🔔", "⭐", "🍉"]
    return [random.choice(symbols) for _ in range(3)]

def check_win(reels):
    return reels[0] == reels[1] == reels[2]

def play_slot_machine():
    balance = 100  # Starting balance
    bet_amount = 10
    
    while balance >= bet_amount:
        input("Press Enter to spin...")
        reels = spin_reels()
        print(" | ".join(reels))
        
        if check_win(reels):
            print("🎉 Jackpot! You won 50 coins! 🎉")
            balance += 50
        else:
            print("Better luck next time!")
            balance -= bet_amount

        print(f"Current balance: {balance} coins\n")
        
        if balance < bet_amount:
            print("Game Over! You ran out of coins.")
            break

if __name__ == "__main__":
    play_slot_machine()
