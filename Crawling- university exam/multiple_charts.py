#open file
with open("clean_data.csv",encoding = "utf8" ) as file:
    data = file.read().split("\n")
header = data[0]
students = data[1:]
#remove last student
students.pop()
#split hear
header = header.split(",")
subjects = header[5:]
total_student = len(students)
total = 0
#split student in list
for i in range(total_student):
	students[i] = students[i].split(",")
number_students_age = [0,0,0,0,0,0,0,0,0,0,0]
average_number_students_age = [0,0,0,0,0,0,0,0,0,0,0]
#find number students with age
for s in students:
	age = 2020 - int(s[4])
	if age >= 27:
		age = 27
	number_students_age[age-17] +=1
#find average scores 
for student in students:
	age = 2020 -int(student[4])
	dem = 0
	tong=0
	if age >= 27:
		age = 27
	if(age==17):
		print(student)
		

	for i in range(5,16):
		
		if i == 7 or i == 8:
			continue
		elif student[i] != "-1":
			dem+=1
			tong += float(student[i])
	average_number_students_age[age-17]+=tong/dem
for i in range(0,11):
	average_number_students_age[i]=round(average_number_students_age[i]/ number_students_age[i],2)	
    
print(number_students_age)
print(average_number_students_age)
for i in range(0,11):
    average_number_students_age[i] = average_number_students_age[i]*7000
import matplotlib.pyplot as plt;
import numpy as np
import matplotlib.pyplot as plt
figure,axis = plt.subplots()
x = np.arange(11)
objects = ["17","18","19","20","21","22","23","24","25","26","26+"]
y_pos = np.arange(len(objects))
performance = number_students_age
#draw first coulumn
axis.set_ylim(0,70000)
axis.set_xlabel("Tuoi")
axis.set_ylabel("So hoc sinh")
plt.bar(y_pos, performance)
plt.plot(x,average_number_students_age,color='r',marker="o")
#draw second column
axis2 = axis.twinx()
axis2.set_ylim(0,10)
axis2.tick_params('y',colors='r')
plt.xticks(y_pos, objects)
axis2.set_ylabel('Diem')
plt.title('Điểm trung bình của học sinh tương ứng với số tuoi')
#bring value on the chart
rects = axis.patches
for rect, label in zip(rects, number_students_age):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height , label,
            ha='center', va='bottom')
plt.show()




