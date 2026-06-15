students =[]

def add_student():
    roll=input("enter roll no")
    name=input("enter name")
  
    subject={}
    
    for i in range(1,4):
        subject_name=input(f"enter subject {i}  name:")
        marks=int(input("enter marks for{subject_name}:"))
        subject[subject_name]=marks
        
        
    
    
    student={
        "roll":roll,
        "name":name,
        "subject":subject,
        
    }
    
    students.append(student)
    print("student added")
    
def view_students():
    if not students:
        print("No Student Found!\n")
        return

    print("\nStudent Records:")
    for student in students:
        print(f"roll: {student['roll']}")
        print(f"name: {student['name']}")
        
        total=0
        
        print("subject and marks:")
        for subject, marks in student ["subjects"].items():
         print(subject,":",marks)
         total += marks
         
         average = total/len(student["subject"])
         
        if average >=90:
            grade="A"
            
        elif average >=75:
            grade="B"
            
        else :
            grade="c"
            
            print("total :",total)
            print("average :", round(average,2))
            print("grade :", grade)      
def search_student():
    roll = input("Enter Roll Number to Search: ")

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found:")
            print(student)
            return

    print("Student Not Found!\n")


# Delete Student
def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student Deleted Successfully!\n")
            return

    print("Student Not Found!\n")


# Update Student
def update_student():
    roll = input("Enter Roll Number to Update: ")

    for student in students:
        if student["roll"] == roll:
            student["name"] = input("Enter New Name: ")
            student["course"] = input("Enter New Course: ")
            print("Student Updated Successfully!\n")
            return

    print("Student Not Found!\n")


# Display Unique Courses using Set
def display_unique_courses():
    courses = set()

    for student in students:
        courses.add(student["course"])

    print("\nUnique Courses:")
    for course in courses:
        print(course)
    print()


# Main Menu
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Display Unique Courses")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        update_student()

    elif choice == "6":
        display_unique_courses()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")
        
        
        
        
    
    