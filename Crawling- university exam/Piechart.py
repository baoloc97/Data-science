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
number_students = [0,0,0,0,0,0,0,0,0,0,0,0]

for student in students:
	dem = 0
	for i in range(5,16):
		if i == 7 or i == 8:
			continue
		elif student[i] != "-1":
			dem+=1

	number_students[dem]+=1
	
others = 0
print(number_students)
number_students_percentage = []
for i in range (0,10):
	if i == 0 or i == 7 or i == 8 or i ==9 or i == 1 or i==2:
	    others += number_students[i]
	else:
	     number_students_percentage.append(number_students[i]) 
number_students_percentage.append(others)
print(number_students_percentage)
import matplotlib.pyplot as plt
import numpy as np
y = np.array(number_students_percentage)
mylabels = ["3","4","5","6","Others"]
colors =['orange','yellow','green','blue','purple','red']
plt.pie(y, labels = mylabels,colors = colors,autopct='%1.2f%%')
plt.legend(title = "Số môn được thi nhiều nhất:")
plt.show() 






