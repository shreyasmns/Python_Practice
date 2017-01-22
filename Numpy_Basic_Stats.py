
# Numpy Enforces a Single data type in an Array -> hence Speed
import numpy as np
import matplotlib

# Generating Data using Numpy
#(distribution mean, distr standard deviation, number of samples)
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15,  5000), 2)

np_city = np.column_stack((height, weight))

# Basic Statistics with Numpy
print('Mean : ', np.mean(np_city))
print('Median : ', np.median(np_city))
print('Corr ef : ', np.corrcoef(np_city))
print('Std dev : ', np.std(np_city))
print('Sum : ', np.sum(np_city))

