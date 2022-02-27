import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from functions import ConvexHull as myConvexHull # Import fungsi ConvexHull implementasi sendiri

data = datasets.load_wine() # Diganti sesuai dataset yang ingin digunakan

#create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
print(df.shape)
df.head()

# INPUT Attribute Index dan title graph yang sesuai
plt.figure(figsize = (10, 6))
plt.title('Total Phenols vs Magnesium') # Diganti sesuai label atribut
attributeIdx1 = 4 # Diganti sesuai index atribut
attributeIdx2 = 5 # Diganti sesuai index atribut

#visualisasi hasil ConvexHull
colors = ['b','r','g', 'c', 'm', 'y', 'k']
plt.xlabel(data.feature_names[attributeIdx1])
plt.ylabel(data.feature_names[attributeIdx2])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[attributeIdx1,attributeIdx2]].values
    hull = myConvexHull(bucket) #bagian ini diganti dengan hasil implementasi ConvexHull Divide & Conquer
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    x = []
    y = []
    for j in range(len(hull)):
        x.append(hull[j][0])
        y.append(hull[j][1])
    if len(hull) > 0:
        x.append(hull[0][0])
        y.append(hull[0][1])
    plt.plot(x, y, colors[i])
    
plt.legend()
plt.show()