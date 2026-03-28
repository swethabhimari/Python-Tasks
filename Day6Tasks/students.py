#Tuple for sub nams
subjects =("Maths","Science","English")
#set for unique students
students_set=set()
#dictionary to store students marks
students_marks={}
#Recursive func to calculate total marks
def calculate_total(marks_list,index=0):
    if index == len(marks_list):
        return 0
    return marks_list[index]+calculate_total(marks_list,index+1)
#function to add studnt 
def add_student():
    try:
        name = input("Enter student name:")
        marks=[]
        for subject in subjects:
            mark = float(input("Enter marks for {subject}:"))
            marks.append(mark)

        students_set.add(name)
        students_marks[name]=marks
    except ValueError:
        print("Invalid input!Please enter numeric marks.")
    except TypeError:
        print("Marks data type error.")
    #Func to display students
def display_students():
    if not students_marks():
        print("No records found.")
    else:
        for name,marks in students_marks.items():
            print(f"{name} : {marks}")
#Func to calculate average
def calculate_average():
    try:
        name = input("Enter student name to calculate average:")
        if name not in students_marks:
            raise NameError
        marks = students_marks[name]
        total = calculate_total(marks)
        average=total/len(marks)
        print("Total Marks:",total)
        print("Average Marks:",average)
    except NameError:
        print("Student name not found.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except TypeError:
        print("Marks datatype error.")
#main
while True:
    print("\n1.Add student.")
    print("2.Display Students.")
    print("3.Calculate Average.")
    print("4.Exit.")
    choice = input("Enter choice.")
    if choice=='1':
        add_student()
    elif choice=='2':
        display_students()
    elif choice=='3':
        calculate_average()
    elif choice=='4':
        print("Existing Program.....")
        break
    else:
        print("Invalid choice .Try again.")
    





