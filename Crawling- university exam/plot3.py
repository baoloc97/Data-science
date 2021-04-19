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
number_students = [0,0,0,0,0,0,0,0,0,0]
average = [0,0,0,0,0,0,0,0,0,0]
for student in students:
	dem = 0
	total = 0
	for i in range(5,16):
		if i == 7 or i == 8:
			continue
		elif student[i] != "-1":
			dem+=1
			total += float(student[i])
	
	average[dem] += total / dem	

	number_students[dem]+=1
for i in range(0,10):
	if number_students[i] == 0:
		continue
	else:
	    average[i] = round(average[i] / number_students[i],2)     	


import matplotlib.pyplot as plt;
import numpy as np
import matplotlib.pyplot as plt
figure,axis = plt.subplots()
objects = ["0","1","2","3","4","5","6","7","8","9"]
y_pos = np.arange(len(objects))
performance = average
axis.set_ylim(0,10)
plt.bar(y_pos, performance)
plt.xticks(y_pos, objects)
plt.ylabel('Percentage')
plt.title('Điểm trung bình của học sinh tương ứng với số môn thi ')
rects = axis.patches
for rect, label in zip(rects, average):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height , label,
            ha='center', va='bottom')
plt.show()