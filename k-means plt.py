import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

filename = '1010.csv'
res = pd.read_excel(filename, encoding='gbk')
res = res.drop(['USERID','DAY'],axis=1)
for f in res:  # 插值法填充
    res[f] = res[f].interpolate()
    # data.dropna(inplace=True)
#print(res)
data = np.array(res)
print(data)

estimator =KMeans(n_clusters=5)   #构造一个聚类数为5的聚类器
estimator.fit(data)   #聚类
label_pred = estimator.labels_  #获取聚类标签
centroids = estimator.cluster_centers_ #获取聚类中心
print(label_pred[: 50])

print(label_pred[30000: 30050])

for i in range(len(label_pred)):
    if label_pred[i] == 0:
        x = [i for i in range(48)]
        plt.plot(x, data[i], '#e24fff')
    if label_pred[i] == 1:
        x = [i for i in range(48)]
        plt.plot(x, data[i], 'g')
    if label_pred[i] == 2:
        x = [i for i in range(48)]
        plt.plot(x, data[i], 'r')
    if label_pred[i] == 3:
        x = [i for i in range(48)]
        plt.plot(x, data[i], 'k')
    if label_pred[i] == 4:
        x = [i for i in range(48)]
        plt.plot(x, data[i], 'c')
plt.show()