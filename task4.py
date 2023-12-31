# -*- coding: utf-8 -*-
"""TASK4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DmkzLkOh0c-dkRHavdSXJ4fHtBskdbm7
"""

from google.colab  import drive
drive.mount('/content/drive')

import numpy as n
import pandas as pd
import matplotlib.pyplot as plot
import seaborn as s

file=p.read_csv("/content/drive/MyDrive/advertising.csv")
file.head()

file.describe()

s.pairplot(file,x_vars=['TV','Radio','Newspaper'],y_vars='Sales',kind='scatter')
plot.show()

file['TV'].plot.hist(bins=10)

file['Radio'].plot.hist(bins=10,color="green",xlabel="Radio")

file['Newspaper'].plot.hist(bins=10,color="purple",xlabel="newspaper")

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(file[['TV']],file[['Sales']],test_size=0.3,random_state=0)

print(X_train)

print(y_train)

print(X_test)

print(y_test)

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train,y_train)

result=model.predict(X_test)
print(result)

model.coef_

model.intercept_

plot.plot(result)

plot.scatter(X_test,y_test)
plot.plot(X_test,7.14382225+0.05473199*X_test,'r')
plot.show()