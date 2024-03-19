import numpy as np

M1 = np.array([
    [2,-1],
    [3,-3]
])
M2 = np.array([
    [5,-2],
    [0,1]
])

print(np.dot(M1, M2))

A = np.array([
    [1,1],
    [2,2],
])

print(np.linalg.det(A))

B = np.array([
    [0.4,-0.2],
    [-0.2,0.6],
])

print(np.linalg.det(B))

C = np.array([
    [0.25,-0.25],
    [-0.125,0.625],
])

print(np.linalg.det(C))

D = np.array([
    [0,0,1],
    [2,2,1],
    [1,0,0],
])

print(np.linalg.det(np.linalg.inv(D)))