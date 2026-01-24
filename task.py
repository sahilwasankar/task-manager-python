class Task :
    def __init__(self, task_id,title,complete = False):

        self.task_id = task_id
        self.title = title
        self.complete = complete

    def mark_complete(self):
     self.complete = True

    def to_csv_row(self):
        return[self.task_id,self.title,self.status]
    
    @staticmethod
    def form_csv_row(row):
       task_id = int(row[0])
       title = row[1]
       complete = row[2] == "True"
       return(task_id,title,complete)
       