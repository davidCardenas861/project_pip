import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('raw.csv')
x = df['Money']

fig , ax = plt.subplots()
ax.hist(x)
plt.savefig('hist.png')

x = df['Departament']
y = df['gender']
fig , ax = plt.subplots()
ax.plot(x)
plt.savefig('plot.png')