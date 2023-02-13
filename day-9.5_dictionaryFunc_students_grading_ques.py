# write a program where you have to access to the database of student_score in the format of dictionary
# the KEYS in the students_score are the name of students and the value are their exam scores
# write a program that convert their scores to their grades
# by the end of your program you have a new dictionary called students_grades
# that should contain student name for KEYS and tr Grades for their VALUES
# where grading are :
# score 91 - 100 grade = "Outstanding"
# score 81 - 90 grade = "excelent"
# score 71 - 80 grade = "acceptable"
# score70 or lower grade = "fail"
students_score = {
    "Ram": 81,
    "Hari": 78,
    "sohan": 99,
    "mohan": 74,
    "radha": 62
}
#print(students_score)

student_grades = {}

for i in students_score:
    score = students_score[i]
    if score > 90 :
        student_grades[i] = "outstanding"
    elif score > 80:
        student_grades[i] = "excelent"
    elif score > 70:
        student_grades[i] = "acceptable"
    else:
        student_grades[i] = "fail"

print(student_grades)