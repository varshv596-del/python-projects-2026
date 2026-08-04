import random

print("🎯 Welcome to Number Guessing Game!")

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("\nEnter your guess (1-100): "))
    attempts += 1

    if guess < number:
        print("📉 Too Low!")
    elif guess > number:
        print("📈 Too High!")
    else:
        print(f"\n🎉 Congratulations! You guessed the number in {attempts} attempts.")
        break

print("👋 Thanks for playing!")