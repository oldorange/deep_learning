# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 16:48:12 2018

@author: staff
"""
import matplotlib.pyplot as plt

import numpy as np
from matplotlib.colors import ListedColormap
X1 = np.array([0,1])
X2 = np.array([0,1])
Z = np.array([[1,8],[0,8]])
plt.contourf(X1, X2, Z,alpha = 0.5, cmap = ListedColormap(('red', 'green', 'cyan')))
#plt.contourf(Z)
#plt.xlim(X1.min(), X1.max())
#plt.ylim(X2.min(), X2.max())

plt.show()