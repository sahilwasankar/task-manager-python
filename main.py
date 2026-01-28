from task import Task
from task_manager import TaskManager

def show_menu():
    print("\n===== TASK MANAGEMENT SYSTEM ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Delete Task")
    print("5. Exit")
    print("=================================")

manager = TaskManager()

while True:
     show_menu()
     choice = input("Enter choice: ")

     if choice == "1":
          title = input("Enter Title: ").strip()
          task = Task(title)
          manager.add_task(task)

     elif choice == "2" :
          manager.view_tasks()   

     elif choice == "3" :
          search = input("Enter Task to search: ").strip()
          manager.search_task(search)

     elif choice == "4" :
          delete = input("Enter Task to delete: ").strip()
          manager.delete_task(delete)    

     elif choice == "5"  :
          print("Goodbye 👋") 
          break
     else:
          print("Please select the valid menu option")
          


  