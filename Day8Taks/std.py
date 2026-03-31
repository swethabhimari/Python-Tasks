#Student Attendance Record
name= input("Enter student name:")
with open("attendance.txt","a") as f:
    f.write(name+"\n")
print("\nAttendance Records:")
with open("attendance.txt","r") as f:
    print(f.read())