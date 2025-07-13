# Bar graph

import matplotlib.pyplot as plt
import numpy as np

arr1 = ["Food","Rent","Groceries","BIlls"]
arr2 = [1200,4500,800,1300]
arr3 = [1000,5000,480,2200]

# plt.bar(arr1, arr2)
# plt.barh(arr1,arr2)
plt.bar(arr1,arr2, color='r')
plt.bar(arr1,arr3, bottom=arr2,color='b')
plt.xlabel('Category')
plt.ylabel('Expenses')
plt.show()