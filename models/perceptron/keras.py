# %%

import os
import plotly as px
import numpy as np
import pandas as pd
import missingno as msno
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
# الآن دیگه باید وارد فاز طراحی مدل بشیم.
# من اینجا می‌خوام شبکه عصبی رو تست کنم.
