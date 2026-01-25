class Task :
    def __init__(self, task_id,title,completed = False):

        self.task_id = task_id
        self.title = title
        self.completed = completed

    def mark_completed(self):
     self.completed = True

    def to_csv_row(self):
        return[self.task_id,self.title,self.completed]
    
    @staticmethod
    def from_csv_row(row):
       task_id = int(row[0])
       title = row[1]
       completed = row[2] == "True"
       return Task(task_id,title,completed)
       