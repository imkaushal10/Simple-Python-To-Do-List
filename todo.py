import json
import os

class TodoApp:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()  # Load tasks on start

    # Setting priority when adding a task
    def add_task(self, task, priority="Medium"):
        self.tasks.append({"task": task, "completed": False, "priority": priority})
        print(f"Task '{task}' with priority '{priority}' added!")

    def remove_task(self, task_index):
        try:
            task = self.tasks.pop(task_index)
            print(f"Task '{task['task']}' removed!")
        except IndexError:
            print("Invalid task index.")

    def mark_completed(self, task_index):
        try:
            self.tasks[task_index]["completed"] = True
            print(f"Task '{self.tasks[task_index]['task']}' marked as completed!")
        except IndexError:
            print("Invalid task index.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        else:
            for idx, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{idx}. {task['task']} - {status} - Priority: {task['priority']}")

    # Save tasks to a JSON file
    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=4)
        print("Tasks saved!")

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.tasks = json.load(f)
            print(f"Loaded {len(self.tasks)} task(s) from {self.filename}")

def main():
    todo_app = TodoApp()

    while True:
        print("\n----- Simple To-Do List -----")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task: ")
            priority = input("Enter priority (High/Medium/Low): ")  # New priority input
            todo_app.add_task(task, priority)
        elif choice == '2':
            todo_app.view_tasks()
            try:
                task_index = int(input("Enter task index to remove: "))
                todo_app.remove_task(task_index)
            except ValueError:
                print("Please enter a valid index.")
        elif choice == '3':
            todo_app.view_tasks()
            try:
                task_index = int(input("Enter task index to mark as completed: "))
                todo_app.mark_completed(task_index)
            except ValueError:
                print("Please enter a valid index.")
        elif choice == '4':
            todo_app.view_tasks()
        elif choice == '5':
            todo_app.save_tasks()  # Save on exit
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
