class Student: 
    def __init__(self, id, name, program, year): 
        self.id = id 
        self.name = name 
        self.program = program 
        self.year = year 
 
    def display(self): 
        print(self.id, self.name, self.program, self.year) 