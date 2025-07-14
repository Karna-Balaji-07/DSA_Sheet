import math

import matplotlib.pyplot as plt
import numpy as np


'''
Simple line chart
'''
# simple line chart
x = np.array([1,2,3,4,5,6,7,8,9])
y = x*2

a = [1,2,3,4,5]
b = [1,2,3,4,5]
plt.plot(a,b)

plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-label')
plt.title('Line chart')
plt.show()


'''
Annotations
'''
# x = [1,2,3,4,5,6,7,8,9]
# y = [2,4,6,8,10,12,14,16,18]
# plt.figure(figsize =(20,20))
# plt.plot(x,y,marker='X',linestyle='-')
# for i, (xi,yi) in enumerate(zip(x,y)):
#     plt.annotate(
#         f'({xi},{yi})',
#         (xi,yi),
#         textcoords="offset points",
#         xytext=(0, 10),
#         ha='center',
#     )
# plt.title('Line chart with annotations')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()
#

