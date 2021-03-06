# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SVVTrSXjcT1H1ZtQRtLLhf-KaChcFKLW
"""

#importing the required librarires
import numpy as np
import pandas as pd

#Reading the data into a dataframe
df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data ",header=None)
df.describe()
df

#Assigning Column Names to the Data
df.columns=['price','buying','maint','doors ','persons','lug_boot','safety']
df

#Examining the data
df.dtypes

df.shape

#Plotting the categorical features in a bar graph
import matplotlib
import matplotlib.pyplot as plt
import math
# %matplotlib inline

fig = plt.figure(figsize=(20,15))
cols = 3
rows = 3
for i,column in enumerate(df.loc[:, df.dtypes == np.object]):
 draw_plot = fig.add_subplot(5, 5, i+1)
 draw_plot.set_title(column)
 df[column].value_counts().plot(kind = 'bar')
 plt.xticks(rotation="vertical")
 plt.subplots_adjust(hspace=0.7, wspace=0.2)

#Coverting the categorical data into numerical labeled data
from sklearn.preprocessing import LabelEncoder
list1 = ['price','buying','maint','doors ','persons','lug_boot','safety']
for i in list1:
 label_encoder = LabelEncoder()
 df[i] = label_encoder.fit_transform(df[i])
df

#Plotting correlations
import seaborn as sns
sns.heatmap(df.corr(),square=True)
plt.show()

from pandas.plotting import scatter_matrix
scatter_matrix(df.iloc[:, 5:8])
plt.show()

#Splitting the input and output into X and Y
X = df.drop('price',1)
Y = df.price
X

#Splitting the dataset into test and training data
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size = 0.8, test_size =0.2)
X_train.shape
Y_train.shape

#Scaling the test and training data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(16,),max_iter=500)
mlp.fit(X_train,Y_train)

predictions = mlp.predict(X_test)
predictions

from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(Y_test,predictions))

print(classification_report(Y_test,predictions))

mlp.coefs_

mlp.intercepts_

mlp.loss_