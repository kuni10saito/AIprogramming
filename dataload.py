import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
os.system("pip install japanize_matplotlib")
import japanize_matplotlib


table=pd.read_csv('AIprogramming/data_circle.csv')
label=table["エネルギー種別"].tolist()
data=table["消費量"].values


table1=pd.read_csv('AIprogramming/data_line.csv')
label1=table1["年次"].tolist()
data1=table1["出生数"].values
data2=table1["合計特殊出生率"].values

