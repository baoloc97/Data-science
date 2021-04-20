from sklearn import datasets
import numpy as np 
import math
def take_first(elem):
    return elem[0]
def Distance(p1,p2):
	dis = 0
	for i in range(len(p1)):
		dis += (p1[i]-p2[i])*(p1[i]-p2[i])
	return math.sqrt(dis)	
def get_k_neigbors(X_train,Y_train,point,K):
	dis = []
	for i in range(len(X_train)):
		dis_new = Distance(X_train[i],point)
		dis.append((dis_new,Y_train[i]))
	dis = sorted(dis, key=take_first)
	dis_final = dis[0:K]
	return dis_final
def predict(X_train,Y_train,point,K):
	array = get_k_neigbors(X_train,Y_train,point,K)
	labels_count = [0,0,0]
	for label in array:
		labels_count[label[1]] += 1
	max_count = max(labels_count)
	label = labels_count.index(max_count) 	
	return label




iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target 
randIndex = np.arange(iris_X.shape[0])
np.random.shuffle(randIndex)

iris_X = iris_X[randIndex]
iris_y = iris_y[randIndex]

X_train = iris_X[:100,:]
X_test  = iris_X[100:,:]
Y_train = iris_y[:100]
Y_test  = iris_y[100:]
# for i in range(len(X_test)):
# 	dis = Distances(X_train,Y_train,X_test[i],4)
count = 0
for i in range(len(X_test)):
	label = predict(X_train,Y_train,X_test[i],5)
	if label == Y_test[i]:
		count= count+1
	else:
		print(i)	
print("So lan du doan dung trong" ,len(Y_test),"la " ,count,"lan.")
print("DO CHINH XAC LA ",count/len(Y_test)*100,"%")



