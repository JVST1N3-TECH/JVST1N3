tasks = []

# Function to view all tasks
def view_tasks():
    if tasks:  # Check if there are any tasks in the to-do list
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):  # Loop through the tasks and display them
            status = "Complete" if task['completed'] else "Incomplete"
            print(f"{index}. {task['name']} - {status}")
    else:
        print("No tasks in the to-do list.")  # Message if the list is empty

# Function to add a new task
def add_task(name):
    tasks.append({'name': name, 'completed': False})  # Add task with 'completed' set to False
    print(f"Task '{name}' added to the list.")

# Function to mark a task as complete
def complete_task(task_number):
    if 0 < task_number <= len(tasks):  # Check if the task number is valid
        tasks[task_number - 1]['completed'] = True  # Mark the task as completed
        print(f"Task '{tasks[task_number - 1]['name']}' marked as complete.")
    else:
        print("Invalid task number.")  # Message if the task number is out of range

# Main loop to display the menu and get user input
while True:
    # Display the options menu
    print(" ---Contact list--- ")
    print("\n1. View To-Do List")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Exit")

    # Get the user's choice
    choice = input("choose an option (1-4): ")

    # Handle each option based on the user's input
    if choice == '1':  # View all tasks
        view_tasks()
    elif choice == '2':  # Add a new task
        task_name = input("Enter task name: ")  # Get the task name from the user
        add_task(task_name)
    elif choice == '3':  # Complete a task
        view_tasks()  # First display the current task list
        task_number = int(input("Enter the task number to complete: "))  # Get the task number
        complete_task(task_number)
    elif choice == '4':  # Exit the program
        print("Exiting the to-do list system.")
        break  # End the loop and exit
    else:
        print("Invalid choice, please try again.")  # Handle invalid input
