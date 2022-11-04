import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_file = pd.read_csv('./iris.data',names=['s_len','s_wid','p_len','p_wid','class'])
frame_data = pd.DataFrame(data_file)

# 각 클래스별로 나누어 그리기
# 클래스별로 true or false 확인
is_setosa=frame_data['class']=='Iris-setosa'
is_versicolor=frame_data['class']=='Iris-versicolor'
is_virginica=frame_data['class']=='Iris-virginica'

seto = frame_data[is_setosa]
ver = frame_data[is_versicolor]
vir = frame_data[is_virginica]

slen_seto = seto[['s_len']]
slen_ver = ver[['s_len']]
slen_vir = vir[['s_len']]

#B question1 : row(sepal length), col(count)
plt.hist(slen_seto, bins=40, range=(4,8), color='red',alpha=0.3)
plt.hist(slen_ver, bins=40, range=(4,8), color='green',alpha=0.3)
plt.hist(slen_vir, bins=40, range=(4,8), color='skyblue',alpha=0.3)
plt.xlabel('sepal length')
plt.ylabel('frequency')
plt.show()

#B question1: row(sepal width) col(count)
swid_seto = seto[['s_wid']]
swid_ver = ver[['s_wid']]
swid_vir = vir[['s_wid']]
plt.hist(swid_seto, bins=30, range=(2,5), color='red',alpha=0.3)
plt.hist(swid_ver, bins=30, range=(2,5), color='green',alpha=0.3)
plt.hist(swid_vir, bins=30, range=(2,5), color='skyblue',alpha=0.3)
plt.xlabel('sepal width')
plt.ylabel('frequency')
plt.show()

#B question1: row(petal length) col(count)
plen_seto = seto[['p_len']]
plen_ver = ver[['p_len']]
plen_vir = vir[['p_len']]
plt.hist(plen_seto, bins=60, range=(1,7), color='red',alpha=0.3)
plt.hist(plen_ver, bins=60, range=(1,7), color='green',alpha=0.3)
plt.hist(plen_vir, bins=60, range=(1,7), color='skyblue',alpha=0.3)
plt.xlabel('petal length')
plt.ylabel('frequency')
plt.show()

#B question1: row(petal width) col(count)
plen_seto = seto[['p_wid']]
plen_ver = ver[['p_wid']]
plen_vir = vir[['p_wid']]
plt.hist(plen_seto, bins=30,range=(0,3), color='red',alpha=0.3)
plt.hist(plen_ver, bins=30, range=(0,3),color='green',alpha=0.3)
plt.hist(plen_vir, bins=30, range=(0,3),color='skyblue',alpha=0.3)
plt.xlabel('petal width')
plt.ylabel('frequency')
plt.show()

#B question2) (1) sepal length, sepal width
x_seto1 = seto[['s_len']]
y_seto1 = seto[['s_wid']]
x_ver1 = ver[['s_len']]
y_ver1 = ver[['s_wid']]
x_vir1 = vir[['s_len']]
y_vir1 = vir[['s_wid']]
plt.scatter(x_seto1,y_seto1,s=20,c='red',alpha=0.3)
plt.scatter(x_ver1,y_ver1,s=20,c='green',alpha=0.3)
plt.scatter(x_vir1,y_vir1,s=20,c='blue',alpha=0.3)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()

#B question2) (2) sepal length, petal length
y_seto2 = seto[['p_len']]
y_ver2 = ver[['p_len']]
y_vir2 = vir[['p_len']]
plt.scatter(x_seto1,y_seto2,s=20,c='red',alpha=0.3)
plt.scatter(x_ver1,y_ver2,s=20,c='green',alpha=0.3)
plt.scatter(x_vir1,y_vir2,s=20,c='blue',alpha=0.3)
plt.xlabel('sepal length')
plt.ylabel('petal length')
plt.show()

#B question2) (3) sepal length, petal width
y_seto3 = seto[['p_wid']]
y_ver3 = ver[['p_wid']]
y_vir3 = vir[['p_wid']]
plt.scatter(x_seto1,y_seto3,s=20,c='red',alpha=0.3)
plt.scatter(x_ver1,y_ver3,s=20,c='green',alpha=0.3)
plt.scatter(x_vir1,y_vir3,s=20,c='blue',alpha=0.3)
plt.xlabel('sepal length')
plt.ylabel('petal width')
plt.show()

#B question2) (4) sepal width, petal length
x_seto2 = seto[['s_wid']]
x_ver2 = ver[['s_wid']]
x_vir2 = vir[['s_wid']]
plt.scatter(x_seto2,y_seto2,s=20,c='red',alpha=0.3)
plt.scatter(x_ver2,y_ver2,s=20,c='green',alpha=0.3)
plt.scatter(x_vir2,y_vir2,s=20,c='blue',alpha=0.3)
plt.xlabel('sepal width')
plt.ylabel('petal length')
plt.show()

#B question2) (5) sepal width, petal width
plt.scatter(x_seto2,y_seto3,s=20,c='red',alpha=0.3)
plt.scatter(x_ver2,y_ver3,s=20,c='green',alpha=0.3)
plt.scatter(x_vir2,y_vir3,s=20,c='blue',alpha=0.3)
plt.xlabel('sepal width')
plt.ylabel('petal width')
plt.show()

#B question2) (6) petal length, petal width
x_seto3 = seto[['p_len']]
x_ver3 = ver[['p_len']]
x_vir3 = vir[['p_len']]
plt.scatter(x_seto3,y_seto3,s=20,c='red',alpha=0.3)
plt.scatter(x_ver3,y_ver3,s=20,c='green',alpha=0.3)
plt.scatter(x_vir3,y_vir3,s=20,c='blue',alpha=0.3)
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.show()

