# todo.py

class Task:
    def __init__(self, description, is_done=False):
        self.description = description
        self.is_done = is_done

    def mark_done(self):
        self.is_done = True

    def __str__(self):
        status = "✔️" if self.is_done else "❌"
        return f"{status} {self.description}"

class TodoList:
    def __init__(self, filename='tasks.txt'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        tasks = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    description, is_done = line.strip().split(' | ')
                    tasks.append(Task(description, is_done == 'True'))
        except FileNotFoundError:
            pass  # No tasks file exists yet
        return tasks

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.description} | {task.is_done}\n")

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        self.save_tasks()

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def mark_task_done(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_done()
            self.save_tasks()
            print(f"Task {task_number} marked as done!")
        else:
            print("Invalid task number.")

def show_menu():
    print("\nTo-Do List CLI")
    print("1. Add a new task")
    print("2. Display all tasks")
    print("3. Mark  task as done")
    print("4. Exit")

def main():
    todo_list = TodoList()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter the task description: ")
            todo_list.add_task(description)
            print("Task has been added!")
        elif choice == "2":
            todo_list.display_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to mark as done: "))
            todo_list.mark_task_done(task_number)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
