games = []

while True:
    print("\n===== GAMING STATS TRACKER =====")
    print("1. Add Game")
    print("2. View Games")
    print("3. Show Total Hours")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        game = input("Game name: ")
        hours = float(input("Hours Played: "))

        games.append({
            "game": game,
            "hours": hours
        })

        print("✅ Game added successfully!")

    elif choice == "2":
        if not games:
            print("No games added yet.")
        else:
            print("\nYour Games:")
            for i, g in enumerate(games, start=1):
                print(f"{i}. {g['game']} - {g['hours']} hours")

    elif choice == "3":
        total = sum(g["hours"] for g in games)
        print(f"\n🎮 Total Hours Played: {total}")

    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice!")