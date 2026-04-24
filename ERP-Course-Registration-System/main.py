from student import Student 
from course import view_courses, register_course 
 
print("=== Student Profile ===") 
 
sid = input("Enter ID: ") 
name = input("Enter Name: ") 
program = input("Enter Program: ") 
year = input("Enter Year: ") 
 
student = Student(sid, name, program, year) 
 
while True: 
    print("\n1. View Profile") 
    print("2. View Courses") 
    print("3. Register Course") 
    print("4. Exit") 
 
    ch = input("Enter choice: ") 
 
    if ch == "1": 
        student.display() 
 
    elif ch == "2": 
        view_courses() 
 
    elif ch == "3": 
        register_course() 
 
    elif ch == "4": 
        break 
 
    else: 
        print("Invalid choice") 
