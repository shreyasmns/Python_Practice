
import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 66.2]

np_height = np.array(height)
np_weight = np.array(weight)

print('Type of np_height', type(np_height))
print('Type of np_weight', type(np_weight))

np_2D = np.array([ [1,2,3,4], [5,6,7,8] ])
print('Type of np_2D array : ', type(np_2D))
print('Stats of np_2D array : ', np_2D.shape)

print(np_2D[0])
print(np_2D[1])