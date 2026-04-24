courses = { 
    "CS101": "Python", 
    "CS102": "DSA", 
    "CS103": "Algorithms" 
} 
 
registered = set() 
 
def view_courses(): 
    for code, name in courses.items(): 
        print(code, "-", name) 
 
def register_course(): 
    code = input("Enter course code: ").upper() 
 
    if code in courses: 
        if code in registered: 
            print("Already registered") 
        else: 
            registered.add(code) 
            print("Registered") 
    else: 
        print("Invalid course") 