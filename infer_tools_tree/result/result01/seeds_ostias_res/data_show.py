from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

seeds = pd.read_csv('seeds.csv')
ostias = pd.read_csv('ostias.csv')


fig, ax = plt.subplots()
# fig = plt.figure()
ax = plt.axes(projection='3d')

# x = seeds['x']
# y = seeds['y']
# z = seeds['z']
# ax.scatter(x, y, z)
# ax.set_title('seeds distribution')
x, y, z = ostias['x'], ostias['y'], ostias['z']
ax.scatter(x, y, z)
plt.show()
