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
#
def input_marks():
    course_id = input("Enter the course ID to input marks: ")
    if not any(course[0] == course_id for course in courses):
        print("Course not found\n")
        return
#create dictionary save mark
    course_marks = {}
    for student in students:
        student_id, name, _ = student #create tuple
        mark = float(input(f"Enter mark for {name} (ID: {student_id}): "))
        course_marks[student_id] = mark
    marks[course_id] = course_marks
    print("Marks added successfully\n")
#In progress
def list_courses():
    print("Courses: ")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")
        print()

def list_students():
    print("Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")
        print()


def show_marks():
    course_id = input("Enter the course ID to view mark: ")
    if course_id not in marks:
        print("No marks found for this course \n")
        return
    course_name = next(course[1] for course in courses if course[0] == course_id) #next use to run the values back to the 1st one
    print(f"Marks for course: {course_name}")
    for student in students:
        student_id, name, _ = student 
        mark = marks[course_id].get(student_id, "N/A") 
        print(f"{name} (ID: {student_id}): {mark}")
    print()

def main():

    while True:
        print("\nStudent Mark Management System")
        print("1. Input student information")
        print("2. Input course information")
        print("3. Input marks for a course")
        print("4. List all courses")
        print("5. List all students")
        print("6. Show student marks for a course")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            input_students()
        elif choice == "2":
            input_courses()
        elif choice == "3":
            input_marks()
        elif choice == "4":
            list_courses()
        elif choice == "5":
            list_students()
        elif choice == "6":
            show_marks()
        elif choice == "7":
            print("Exiting the system. Thanks for using.")
            break
        else:
            print("Invalid choice, please try again.\n")
          
if __name__ == "__main__":
    main()

