from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib.pyplot as plt
# Thu Nhap
X = np.array([[52.02,52.41,51.55,58.88,59.66,68.42,64.27,63.01,65.61,61.05,63.36,67.42,67.86,83.39,84.26,77.41,70.08,77.44,75.79,81.89
]]).T
# Tieu dung
y = np.array([[ 48.34,48.54,47.44,54.58,55,63.49,59.22,57.77,60.22,55.4,57.17,60.84,60.73,76.4,
76.42,69.34,61.75,68.78,67.07,72.94]]).T

plt.plot(X, y, 'ro')
plt.axis([40, 100, 40, 100])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()

