import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
os.system("pip install japanize_matplotlib")
import japanize_matplotlib


table=pd.read_csv('data_circle.csv')
label=table["エネルギー種別"].tolist()
data=table["消費量"].values


table=pd.read_csv('data_line.csv')
label=table["年次"].tolist()
data1=table["出生数"].values
data2=table["合計特殊出生率"].values

