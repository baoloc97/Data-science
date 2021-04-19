with open("clean_data.csv",encoding = "utf8" ) as file:
    data = file.read().split("\n")
header = data[0]
students = data[1:]
#remove last student
students.pop()
header = header.split(",")
subjects = header[5:]
total_student = len(students)
for i in range(total_student):
	students[i] = students[i].split(",")
not_take_exam = [0,0,0,0,0,0,0,0,0,0,0]

for student in students:
	for i in range(5,16):
		if student[i] == "-1":
			not_take_exam[i-5] +=1
print(not_take_exam)
not_take_exam_percentage = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,11):
	not_take_exam_percentage[i]= round(not_take_exam[i]*100/total_student,2)
print(not_take_exam_percentage)
import matplotlib.pyplot as plt;
import numpy as np
import matplotlib.pyplot as plt
figure,axis = plt.subplots()

take_exam = [0,0,0,0,0,0,0,0,0,0,0]
for student in students:
	for i in range(5,16):
		if student[i] != "-1":
			take_exam[i-5]+=1

take_exam_percentage = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,11):
	take_exam_percentage[i] = round(take_exam[i]*100/total_student,2)

print(take_exam_percentage)
objects = subjects
y_pos = np.arange(len(objects))
performance = take_exam_percentage
axis.set_ylim(0,100)
plt.bar(y_pos, performance)
plt.xticks(y_pos, objects)
plt.ylabel('Percentage')
plt.title('Số học sinh thi mỗi môn ')
rects = axis.patches
for rect, label in zip(rects, take_exam):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
            ha='center', va='bottom')
plt.show()





