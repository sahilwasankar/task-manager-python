import csv
from task import Task


class TaskManager:
    def __init__(self,filename = "data/tasks.csv" ):
        self.filename = filename
        self.tasks = []      
        self.load_task()


    def load_task(self):
        try:
         with open(self.filename ,"r", newline = "") as file:
            reader  = csv.reader(file)
            for row in reader:
                title = row[0]
                priority = row[1]
                completed = row[2]
                self.tasks.append(Task(title,priority,completed))
        except:
            FileNotFoundError
            pass

    def save_task(self):
        with open(self.filename ,"w", newline="") as file:
            writer = csv.writer(file)

            for task in self.tasks:
                writer.writerow(task.to_csv_row())

    def task_exists(self,title):
        for task in self.tasks:
            if task.title == title:
                return True
        return False    

    def task_priority(self,task):
        priority_order = {"high":0 ,"medium": 1 , "low": 2}
        for i in range(len(self.tasks)):
            if priority_order[task.priority] < priority_order[self.tasks[i].priority]:
               self.tasks.insert(i , task)#at this index the value will get inserted
               return
        self.tasks.append(task)

      

    def add_task(self,task):      
        if self.task_exists(task.title):
            print("Task already exists. Use a unique Title. ")
            return
        
        self.task_priority(task)
        self.save_task()
        print("Task added Successfully")       


    def view_tasks(self):
        if not self.tasks :
            print("Task not found")


        for task in self.tasks:
              if task.completed == True:
                  status = "Done"
              else:
                  status = "pending"    
              print(f"Title: {task.title} priority: {task.priority} Status: {status}")


    def search_task(self,title):
            for task in self.tasks:
                if task.title == title:
                      if task.completed == True:
                         status = "Done"
                      else:
                        status = "pending" 
                        print(f"Title: {task.title}\nPriority: {task.priority}\nStatus: {status}")
                        return
                
            print("Task not exists.")  
                

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                print("\nTask found:")
                print(f"Title: {task.title}\nPriority: {task.priority}\nStatus:{task.completed}")
                confirm = input("Are you sure you want to delete this task: (yes/no): ")
                if confirm == "yes":
                    self.tasks.remove(task)
                    self.save_task()
                    print("Task deleted successfully")
                else:
                    print("Delete operation cancelled")

                return
        print("Task does not found")