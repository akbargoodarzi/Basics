class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def show_tasks(self):
        for task in self.tasks:
            print(task)

# Usage
my_todo = ToDoList()
my_todo.add_task("Learn Python")
my_todo.add_task("Read a book")
my_todo.show_tasks()
