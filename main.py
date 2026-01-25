from task import Task
from task_manager import TaskManager

def show_menu():
    print("\n===== TASK MANAGEMENT SYSTEM ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    print("=================================")

manager = TaskManager()

while True:
     show_menu()
     choice = input("Enter choice: ")

     if choice == "1":
          task_id = input("Enter ID: ").strip()
          title = input("Enter Title: ").strip()
          task = Task(task_id,title)
          manager.add_task(task)

     elif choice == "2" :
          manager.view_tasks()   

     elif choice == "3"  :
          print("Goodbye 👋") 
          break
     else:
          print("Please select the valid menu option")
          


  