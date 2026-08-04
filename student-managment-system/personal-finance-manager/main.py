income = 0
expense = 0

while True:
    print("\n===== PERSONAL FINANCE MANAGER =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Balance")
    print("4. Show Total Income")
    print("5. Show Total Expense")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        amount = float(input("Enter income amount: ₹"))
        income += amount
        print("✅ Income added successfully!")

    elif choice == "2":
        amount = float(input("Enter expense amount: ₹"))
        expense += amount
        print("✅ Expense added successfully!")

    elif choice == "3":
        balance = income - expense
        print(f"\n💰 Current Balance: ₹{balance}")

    elif choice == "4":
        print(f"\n📈 Total Income: ₹{income}")

    elif choice == "5":
        print(f"\n📉 Total Expense: ₹{expense}")

    elif choice == "6":
        print("👋 Thanks for using Personal Finance Manager!")
        break

    else:
        print("❌ Invalid choice!")