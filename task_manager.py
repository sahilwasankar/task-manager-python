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
                completed = row[1]
                self.tasks.append(Task(title,completed))
        except:
            FileNotFoundError
            pass

    def save_task(self):
        with open(self.filename ,"w", newline="") as file:
            writer = csv.writer(file)

            for task in self.tasks:
                writer.writerow(task.to_csv_row())


    def add_task(self,task):      
        self.tasks.append(task) 
        self.save_task()
        print("Task added Successfully")       


    def view_tasks(self):
        if not self.tasks :
            print("Task not found")


        for task in self.tasks:
              status = "Done" if task.completed else "Pending"
              print(f"Title: {task.title} Status: {status}")


    def search_task(self,title):
            for task in self.tasks:
                if task.title == title:
                    print(f"Title: {task.title}\nStatus: {task.completed}")
                    return 
                
            print("task does not exists")


