import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
size = 3
for i in range(size):
    data = np.loadtxt('vessel_{0}.txt'.format(i))
    X, Y, Z = data.T
    plt.plot(X, Y, Z, label='vessel_{0}'.format(i))

plt.legend()
plt.show()
