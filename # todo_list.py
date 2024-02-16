# todo_list.py

# Function to display the menu
def display_menu():
    print("Todo List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. Display Tasks")
    print("5. Exit")

# Function to add a task to the list
def add_task(task):
    with open("todo.txt", "a") as file:
        file.write(task + "\n")

# Function to remove a task from the list
def remove_task(task):
    tasks = get_tasks()
    if task in tasks:
        tasks.remove(task)
        with open("todo.txt", "w") as file:
            for t in tasks:
                file.write(t + "\n")
        print("Task removed successfully.")
    else:
        print("Task not found.")

# Function to mark a task as completed
def mark_completed(task):
    tasks = get_tasks()
    if task in tasks:
        print("Task marked as completed.")
    else:
        print("Task not found.")

# Function to display all tasks
def display_tasks():
    tasks = get_tasks()
    if tasks:
        print("Tasks:")
        for task in tasks:
            print("- " + task)
    else:
        print("No tasks.")

# Function to get all tasks from the file
def get_tasks():
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

# Main function
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == "3":
            task = input("Enter the task to mark as completed: ")
            mark_completed(task)
        elif choice == "4":
            display_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
