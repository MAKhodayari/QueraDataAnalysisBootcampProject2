# %%

import os
import plotly as px
import numpy as np
import pandas as pd
import missingno as msno
import numpy as np
import tensorflow as tf
from tensorflow import keras as K
# %%
# 2. define model
init = K.initializers.RandomUniform(seed=1)
simple_sgd = K.optimizers.SGD(learning_rate=0.010)#پارامتر نرخ یادگیری اسم جدیدتری دارد
# توی لینک زیر یک مقدار متفاوت هستش
# https://keras.io/api/optimizers/sgd/
# بنظر می‌رسه درستش اینه:
# simple_sgd = K.optimizers.experimental.SGD(learning_rate=0.1)

# %%
model = K.models.Sequential()
model.add(K.layers.Dense(units=10, input_dim=13, kernel_initializer=init, activation='tanh')) # hidden layer
model.add(K.layers.Dense(units=10, activation='tanh')) # hidden layer
model.add(K.layers.Dense(units=1, activation=None))
model.compile(loss='mean_squared_error', optimizer = "adam" , metrics=['mse'])

# %%
dirname = os.path.dirname(__file__)
Datasets_path = dirname[:-17] + "Datasets/"
# %%
df = pd.read_csv(Datasets_path+"DataWithFullGDP.csv")
if "Unnamed: 0" in df.columns:
    df.drop(columns= "Unnamed: 0", inplace=True)
df
# %%
df.isnull().sum()
# دروغ می‌گه :)
# %%
df.info()
# %%
# بیایین تبدیل به float کنیم وقتی خطا داد می‌فهمیم باید حرکتی بزنیم.
#df = pd.read_csv(Datasets_path+"CountryInfo.csv")
list_col_err =[]
for col in df.columns[2:]:
    try:
        df[col] = df[col].astype(float)
    except ValueError as err:
        if "could not convert string to float: '...'" in str(err):
            list_col_err.append(col)
        else:
            print(err)

len(df.columns[2:]),len(list_col_err)
# پس خیلی اوضاع خیطه

# %%
for col in list_col_err:
    for j in range(len(df)):
        if df.at[j , col] == '...':
            df.at[j , col] = np.nan


# %%
df.isnull().sum()

# %%
msno.matrix(df)
# %%

df.columns[14]
# %%
df[df[df.columns[5]].isnull()]
# اگر توی غیر از اون ستون 'Population Annual Doubling Time (years)' مشکلی می‌بود به کمک این قسمت می‌تونستیم اون بخش‌ها رو پیدا کنیم.


# %%
df.dropna(inplace=True)
# %%
df
# %%
# الآن دیگه باید وارد فاز طراحی مدل بشیم.
# من اینجا می‌خوام شبکه عصبی رو تست کنم.
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

train , test = train_test_split(df, test_size=.2, random_state=313)
train , valid = train_test_split(train, test_size=.2, random_state=313)


# %%
