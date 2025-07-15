#!/usr/bin/env python3
"""
Simple Task Manager
A basic command-line task management application
"""

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, description):
        """Add a new task to the list"""
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False
        }
        self.tasks.append(task)
        print(f"✓ Task added: {description}")
    
    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("No tasks found!")
            return
        
        print("\n" + "="*50)
        print("YOUR TASKS")
        print("="*50)
        
        for task in self.tasks:
            status = "✓" if task['completed'] else "○"
            print(f"{status} [{task['id']}] {task['description']}")
        print("="*50)
    
    def complete_task(self, task_id):
        """Mark a task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                if task['completed']:
                    print(f"Task {task_id} is already completed!")
                else:
                    task['completed'] = True
                    print(f"✓ Task {task_id} marked as completed!")
                return
        print(f"Task with ID {task_id} not found!")
    
    def delete_task(self, task_id):
        """Delete a task from the list"""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                removed_task = self.tasks.pop(i)
                print(f"✓ Task deleted: {removed_task['description']}")
                return
        print(f"Task with ID {task_id} not found!")


def display_menu():
    """Display the main menu options"""
    print("\n" + "="*30)
    print("TASK MANAGER")
    print("="*30)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    print("="*30)


def handle_add_task(manager):
    """Handle adding a new task"""
    description = input("Enter task description: ").strip()
    if description:
        manager.add_task(description)
    else:
        print("Task description cannot be empty!")


def handle_complete_task(manager):
    """Handle completing a task"""
    try:
        task_id = int(input("Enter task ID to complete: "))
        manager.complete_task(task_id)
    except ValueError:
        print("Please enter a valid task ID (number)!")


def handle_delete_task(manager):
    """Handle deleting a task"""
    try:
        task_id = int(input("Enter task ID to delete: "))
        manager.delete_task(task_id)
    except ValueError:
        print("Please enter a valid task ID (number)!")


def process_choice(manager, choice):
    """Process user menu choice"""
    if choice == '1':
        handle_add_task(manager)
    elif choice == '2':
        manager.view_tasks()
    elif choice == '3':
        handle_complete_task(manager)
    elif choice == '4':
        handle_delete_task(manager)
    elif choice == '5':
        print("Thanks for using Task Manager! Goodbye!")
        return False
    else:
        print("Invalid choice! Please enter 1-5.")
    return True


def main():
    """Main application loop"""
    manager = TaskManager()
    print("Welcome to Simple Task Manager!")
    
    while True:
        display_menu()
        try:
            choice = input("Enter your choice (1-5): ").strip()
            if not process_choice(manager, choice):
                break
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()