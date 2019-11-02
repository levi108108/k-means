
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

class Model2:

    def classify(self, filename):
        #filename = '1010.csv'
        res = pd.read_excel(filename, encoding='gbk')
        res = res.drop(['USERID','DAY'],axis=1)
        for f in res:  # 插值法填充
            res[f] = res[f].interpolate()
            # data.dropna(inplace=True)
        #print(res)
        data = np.array(res)
        # print(data)

        estimator =KMeans(n_clusters=5)   #构造一个聚类数为5的聚类器
        estimator.fit(data)   #聚类
        label_pred = estimator.labels_  #获取聚类标签
        centroids = estimator.cluster_centers_ #获取聚类中心
        # print(label_pred)

        for i in range(len(label_pred)):
            if label_pred[i] == 0:
                result = "一般家庭用电负荷曲线"
                #return result
                print(result)
            if label_pred[i] == 1:
                result = "商业建筑用电负荷曲线"
                # return result
                print(result)
            if label_pred[i] == 2:
                result = "有青少年家庭用电负荷曲线"
                # return result
                print(result)
            if label_pred[i] == 3:
                result = "工业用电负荷曲线"
                # return result
                print(result)
            if label_pred[i] == 4:
                result = "高端小区用电负荷曲线"
                #return result
                print(result)
        print(len(label_pred))
