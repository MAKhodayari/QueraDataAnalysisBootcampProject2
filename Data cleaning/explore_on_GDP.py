# %%
import numpy as np
import pandas as pd
import os
# %%
dirname = os.path.dirname(__file__)
datas_path = dirname[:-13] + "datas"
datas_path 
# %%
gdp_df = pd.read_csv(datas_path+"Life Expectancy vs GDP 1950-2018.csv")
# %%
