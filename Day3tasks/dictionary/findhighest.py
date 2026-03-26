students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

top_student = max(students, key=students.get)

print("Student with highest marks:", top_student)
print("Marks:", students[top_student])