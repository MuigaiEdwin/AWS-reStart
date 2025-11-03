# This app allows a user to:
# 1. Add new tasks
# 2. View existing tasks
# 3. Mark tasks as completed
# 4. Delete tasks
# 5. Save data to file (tasks.txt)

import os

TASKS_FILE = "tasks.txt"

# --- Load tasks from file ---
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks yet! Add one below.\n")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

def main():
    tasks = load_tasks()

    while True:
        print("=== 🧠 To-Do List Menu ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            new_task = input("Enter new task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print("✅ Task added!\n")
            else:
                print("⚠️ Task cannot be empty.\n")

        elif choice == "3":
            show_tasks(tasks)
            try:
                index = int(input("Enter task number to mark as done: ")) - 1
                if 0 <= index < len(tasks):
                    tasks[index] = f"✔️ {tasks[index]}"
                    save_tasks(tasks)
                    print("🎯 Task marked as done!\n")
                else:
                    print("⚠️ Invalid task number.\n")
            except ValueError:
                print("⚠️ Please enter a valid number.\n")

        elif choice == "4":
            show_tasks(tasks)
            try:
                index = int(input("Enter task number to delete: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    save_tasks(tasks)
                    print(f"🗑️ Deleted task: {removed}\n")
                else:
                    print("⚠️ Invalid task number.\n")
            except ValueError:
                print("⚠️ Please enter a valid number.\n")

        elif choice == "5":
            print("👋 Goodbye, see you next time!")
            break

        else:
            print("⚠️ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
