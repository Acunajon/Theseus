import numpy as np
import matplotlib.pyplot as plt

a = [1,2,3,4]
b = [5,4,3,1]

c = ((a-b)**2)/b







print sum(c)**2


plt.hold(True)
plt.scatter(a,b, c='red')
plt.scatter(a,c)
plt.show()