# Katelyn Curtiss
# October 29 2024
# List Evidence 

student = []
school = []
course = []
quiz_score = []

student.append(input('Enter first and last name: '))
school.append(input('Enter school:'))
course.append(input('Enter class name: '))
quiz_score.append(int(input('Enter first quiz score: ')))
quiz_score.append(int(input('Enter second quiz score: ')))
quiz_score.append(int(input('Enter third quiz score: ')))
quiz_score.append(int(input('Enter fourth quiz score: ')))


num_elements = len(quiz_score)
average_quiz_score = sum(quiz_score) / num_elements

print(f'Semester 1 Grade Report\n Student: {student} \n School: {school} \n Course: {course} \n Average Score: {average_quiz_score}')

"\n"

#Second student
student2 = []
school2 = []
course2 = []
quiz_score2 = []

#Second Student 
student2.append(input('Enter first and last name: '))
school2.append(input('Enter school name: '))
course2.append(input('Enter class name: '))
quiz_score2.append(int(input('Enter first quiz score: ')))
quiz_score2.append(int(input('Enter second quiz score: ')))
quiz_score2.append(int(input('Enter third quiz score: ')))
quiz_score2.append(int(input('Enter fourth quiz score: ')))

#Second student
num_elements2 = len(quiz_score2)
average_quiz_score2 = sum(quiz_score2) / num_elements2


print(f'\n Student: {student2} \n School: {school2} \n Course: {course2} \n Average Score: {average_quiz_score2}')


