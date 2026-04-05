tasks=[]
def add_task():
    task=input("Enter your task\n")
    tasks.append(task)
    print("Task added Successfully!!\n")


def view_tasks():
    if not tasks:
        print("No tasks are available\n")
    else:
        print("Your To-Do-List\n")
        for i,task in enumerate(tasks,start=1):
            print(f"{i}. {task}")
            print()

def remove_tasks():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed}' removed successfully!\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")


def main():
    
    while True:
        print("====To-Do-List====\n")
        print("1.Add new task\n")
        print("2.View Tasks\n")
        print("3.Remove Task\n")
        print("4.Exit")
        choice=input("Enter your option\n")
        if(choice=='1'):
            add_task()
        elif(choice=='2'):
            view_tasks()
        elif(choice=='3'):
            remove_tasks()
        elif(choice=='4'):
            print("Exiting!!\n")
            break
        else:
            print("Invalid choice!!\n")

main()