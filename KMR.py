from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from mc_tools import mc_compute_stationary, mc_sample_path
from discrete_rv import DiscreteRV

N = 6
t = 10000
epsilon = 0.1
x_0 = 0
p = 1/3

A = np.zeros([N+1, N+1])
A[0,0] = 1 - epsilon*0.5
A[0,1] = epsilon*0.5
A[N,N-1] = epsilon*0.5
A[N,N] = 1 - epsilon*0.5
for i in range(1,N):
    x_i = i / N
    if x_i < p:
        A[i, i-1] = x_i * (1 - epsilon*0.5)
        A[i, i+1] = (1 - x_i) * epsilon*0.5
        A[i, i] = 1 - A[i, i-1] - A[i, i+1]
    elif x_i > p:
        A[i, i -1] = x_i * epsilon*0.5
        A[i, i+1] = (1 - x_i) * (1 - epsilon * 0.5)
        A[i, i] = 1- A[i, i-1] - A[i, i+1]
    else:
        A[i, i -1] = x_i * 0.5
        A[i, i+1] = x_i * 0.5
        A[i, i] = 0.5

y = mc_sample_path(A, x_0, t)

fig, ax = plt.subplots()
ax.plot(y)
plt.show()