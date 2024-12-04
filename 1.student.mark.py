students = [] #list tuple of students
courses = [] #tuple for courses id, name
marks = {} #tuple using dictionary to save all marks of student
#enter in4 of students
def input_students():
    num_students = int(input("Enter the number of students in the class: "))
    for _ in range(num_students): #range is create a list num from 0 to num_student - 1
        st_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        Dob = input("Enter student Date of Birth: ")
        students.append((st_id, name, Dob)) #add student into the list(tuple)
        print("Students added successfully\n")

#enter in4 of courses        
def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses): #another range
        c_id = input("Enter course ID: ") #course_id
        name = input("Enter course name: ")
        courses.append((c_id, name)) #add to the tuple
        print("Courses added successfully\n")

#In progress
