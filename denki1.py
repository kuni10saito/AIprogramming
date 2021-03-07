import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
os.system("pip install japanize_matplotlib")
import japanize_matplotlib


table=pd.read_csv('data_circle.csv')
label=table["エネルギー種別"].values
data=table["消費量"].values
