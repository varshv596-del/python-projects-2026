import json
import os

FILE_NAME = "expenses.json"

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        expenses = json.load(file)
else:
    expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: ₹"))

        expenses.append({
            "name": name,
            "amount": amount
        })

        with open(FILE_NAME, "w") as file:
            json.dump(expenses, file, indent=4)

        print("✅ Expense added successfully!")

    elif choice == "2":
        if not expenses:
            print("📭 No expenses found.")
        else:
            print("\n📋 Expenses:")
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. {expense['name']} - ₹{expense['amount']}")

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"\n💰 Total Expense: ₹{total}")

    elif choice == "4":
        print("👋 Thanks for using Expense Tracker!")
        break

    else:
        print("❌ Invalid choice.")