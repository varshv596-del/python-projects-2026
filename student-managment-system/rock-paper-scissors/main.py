import random

print("🎮 Rock Paper Scissors Game")
print("---------------------------")

choices = ["rock", "paper", "scissors"]

player = input("Choose Rock, Paper or Scissors: ").lower()

if player not in choices:
    print("❌ Invalid choice! Please run the game again.")
else:
    computer = random.choice(choices)

    print(f"\n🧑 You chose: {player}")
    print(f"💻 Computer chose: {computer}")

    if player == computer:
        print("🤝 It's a Draw!")
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("🎉 You Win!")
    else:
        print("😢 Computer Wins!")