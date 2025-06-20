student_marks = {"Alice":85,"Bob":92,"Charlie":78,"Diana":90}
print(student_marks)
name = input("Enter the student's name: ")
if name in student_marks:
    mark = student_marks[name]
    print(mark)
else:
    print("Student doesn't exist")