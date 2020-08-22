import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

file = './barometerplus.csv'
df = pd.read_csv(file, usecols=[1,2], index_col='TIME')
df.index = pd.to_datetime(df.index)
print(df.head())

df.plot(ax=ax)

file2 = './KCMD.csv'
kcmd = pd.read_csv(file2, header=6).drop(0)
kcmd.index = pd.to_datetime(kcmd['Date_Time'])
print(kcmd.head())

(kcmd['pressure_set_1d'].astype(float)/100).plot(ax=ax)