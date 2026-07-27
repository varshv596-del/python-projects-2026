tasks = []

while True:
    print("\n===== TODO APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("✅ Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("📭 No tasks found.")
        else:
            print("\n📋 Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("📭 No tasks to delete.")
        else:
            print("\n📋 Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                task_no = int(input("Enter task number to delete: "))
                if 1 <= task_no <= len(tasks):
                    removed = tasks.pop(task_no - 1)
                    print(f"🗑️ '{removed}' deleted successfully!")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Please enter a valid number.")

    elif choice == "4":
        print("👋 Thanks for using Todo App!")
        break

    else:
        print("❌ Invalid choice. Please try again.")