import csv
from task import Task

class TaskManager:
    def __init__(self ):
        self.tasks = []      
        
    def add_task(self,task):      
        self.tasks.append(task) 
        print("Task added Successfully")       

    def view_tasks(self):
        if not self.tasks :
            print("Task not found")

        for task in self.tasks:
              status = "Done" if task.completed else "Pending"
              print(f"Title: {task.title} Status: {status}")
