class Task :
    def __init__(self,title,priority,completed = False):

        self.title = title
        self.priority = priority
        self.completed = completed

    def mark_completed(self) :
        self.completed = True     

    def to_csv_row(self):
        return[self.title,self.priority,self.completed]
    

       