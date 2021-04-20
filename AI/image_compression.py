import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
import numpy 
from PIL import Image

img = plt.imread("thoga.jpg")
width = img.shape[0]
height = img.shape[1]
img = img.reshape(width*height,3)

kmeans = KMeans(n_clusters=4).fit(img)
clusters = kmeans.cluster_centers_
labels = kmeans.predict(img)
clusters = kmeans.cluster_centers_
print(labels)
print(clusters)
img2 = numpy.zeros_like(img)
for i in range(len(img2)):
	img2[i] = clusters[labels[i]]
img2 = img2.reshape(width,height,3)	
fig = plt.figure(frameon = False)
ax = plt.Axes(fig,[0.,0.,1.,1.])
ax.set_axis_off()
fig.add_axes(ax)
plt.imshow(img2)
plt.show()	
im = Image.fromarray(img2)
im.save("your_file.jpg")



