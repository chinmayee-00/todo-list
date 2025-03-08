import json

class ToDoList:
    def _init_(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, category, priority):
        """Add a new task with title, category, and priority."""
        task = {
            "title": title,
            "category": category,
            "priority": priority,
            "completed": False
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully!")

    def remove_task(self, title):
        """Remove a task by title."""
        for task in self.tasks:
            if task["title"] == title:
                self.tasks.remove(task)
                self.save_tasks()
                print(f"Task '{title}' removed successfully!")
                return
        print(f"Task '{title}' not found.")

    def mark_completed(self, title):
        """Mark a task as completed."""
        for task in self.tasks:
            if task["title"] == title:
                task["completed"] = True
                self.save_tasks()
                print(f"Task '{title}' marked as completed!")
                return
        print(f"Task '{title}' not found.")

    def show_tasks(self):
        """Display all tasks sorted by priority (High > Medium > Low)."""
        if not self.tasks:
            print("No tasks available.")
            return

        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        sorted_tasks = sorted(self.tasks, key=lambda x: priority_order[x["priority"]])

        print("\nYour Tasks:")
        for task in sorted_tasks:
            status = "✔ Completed" if task["completed"] else "❌ Pending"
            print(f"Title: {task['title']} | Category: {task['category']} | Priority: {task['priority']} | Status: {status}")
        print()

    def save_tasks(self):
        """Save tasks to a JSON file."""
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=4)

    def load_tasks(self):
        """Load tasks from a JSON file."""
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

# Example Usage
if _name_ == "_main_":
    todo = ToDoList()

    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Mark Completed\n4. Show Tasks\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Task Title: ")
            category = input("Category (e.g., Work, Personal): ")
            priority = input("Priority (High, Medium, Low): ").capitalize()
            if priority not in ["High", "Medium", "Low"]:
                print("Invalid priority! Setting default priority to 'Low'.")
                priority = "Low"
            todo.add_task(title, category, priority)

        elif choice == "2":
            title = input("Enter task title to remove: ")
            todo.remove_task(title)

        elif choice == "3":
            title = input("Enter task title to mark as completed: ")
            todo.mark_completed(title)

        elif choice == "4":
            todo.show_tasks()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again!")
