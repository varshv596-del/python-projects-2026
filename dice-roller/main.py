import random

print("🎲 Welcome to Dice Roller!")

while True:
    input("\nPress Enter to roll the dice...")

    dice = random.randint(1, 6)
    print(f"You rolled: {dice}")

    again = input("Roll again? (y/n): ").lower()

    if again != "y":
        print("👋 Thanks for playing!")
        break
