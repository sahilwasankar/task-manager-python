from task import Task
from task_manager import TaskManager

def show_menu():
    print("\n===== TASK MANAGEMENT SYSTEM ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark task as completed")
    print("4. Search Task")
    print("5. Delete Task")
    print("6. Exit")
    print("=================================")


manager = TaskManager()


while True:
     show_menu()
     choice = input("Enter choice: ")

     if choice == "1":
          title = input("Enter Title: ").strip()
          priority = input("Enter priority (High/Low/Medium): ").strip().lower()
          task = Task(title,priority)
          manager.add_task(task)

     elif choice == "2" :
          manager.view_tasks()  

     elif choice == "3" :
           title = input("Enter task title: ").strip()   
           manager.mark_status(title)
           

     elif choice == "4" :
          search = input("Enter Task to search: ").strip()
          manager.search_task(search)

     elif choice == "5" :
          delete = input("Enter Task to delete: ").strip()
          manager.delete_task(delete)    

     elif choice == "6"  :
          print("Goodbye 👋") 
          break
     else:
          print("Please select the valid menu option")
          


  