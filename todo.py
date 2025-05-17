import os
import json

TODO_FILE = "todos.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def list_tasks(tasks):
    if not tasks:
        print("✅ No tasks!")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"➕ Added: {task}")

def remove_task(tasks):
    list_tasks(tasks)
    index = int(input("Enter task number to remove: ")) - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"❌ Removed: {removed}")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        list_tasks(tasks)
        print("\nOptions: [add] [remove] [quit]")
        choice = input("Choose an option: ").strip().lower()
        if choice == "add":
            add_task(tasks)
        elif choice == "remove":
            remove_task(tasks)
        elif choice == "quit":
            save_tasks(tasks)
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
