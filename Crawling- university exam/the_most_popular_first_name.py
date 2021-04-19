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
lastname_list_total=[]
lastname_list = []
count_lastname_list=[]
#find a list contain last name
for s in students:
	data = s[1].split(" ")
	lastname = data[0]
	lastname_list_total.append(lastname)
	if lastname not in lastname_list:
		lastname_list.append(lastname)
		count_lastname_list.append(0)
		count_lastname_list[lastname_list.index(lastname)]+=1
	else:
		count_lastname_list[lastname_list.index(lastname)]+=1

for i in range(len(lastname_list)):
	for j in range(len(lastname_list)):
		if count_lastname_list[i]>count_lastname_list[j]:
			count_lastname_list[i],count_lastname_list[j] = count_lastname_list[j],count_lastname_list[i]
			lastname_list[i],lastname_list[j]=lastname_list[j],lastname_list[i]

count_lastname_final= count_lastname_list[:20]
lastname_list_final=lastname_list[:20]
import matplotlib.pyplot as plt;
import numpy as np
import matplotlib.pyplot as plt
figure,axis = plt.subplots()
objects = lastname_list_final
y_pos = np.arange(len(objects))
performance = count_lastname_final
axis.set_ylim(0,30000)
plt.bar(y_pos, performance)
plt.xticks(y_pos, objects)
plt.ylabel('So nguoi')
plt.xlabel('Ho')
plt.title('Ho pho bien nhat viet nam ')
rects = axis.patches
for rect, label in zip(rects, count_lastname_final):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height , label,
            ha='center', va='bottom')
plt.show()





