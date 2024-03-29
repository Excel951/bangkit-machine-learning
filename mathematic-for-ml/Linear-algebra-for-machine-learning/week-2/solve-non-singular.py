import numpy as np

num_1 = np.array([
    [2,5],
    [8,1]
])

res_1 = np.array([
    46,32
])

# print(np.linalg.solve(num_1, res_1))

num_2 = np.array([
    [-3,8,1],
    [2,2,-1],
    [-5,6,2]
], dtype=np.int64)

# print(np.linalg.det(num_2))

num_3 = np.array([
    [1,3],
    [3,12]
])

res_3= np.array([
    15,3
])

# print(np.linalg.solve(num_3, res_3))

num_4 = np.array([
    [2,1],
    [4,2]
])

res_4= np.array([
    5,10
])

# print(np.linalg.solve(num_4, res_4))

num_5 = np.array([
    [1,2,3],
    [2,6,12],
    [4,-8,4],
])

res_5= np.array([
    10,4,8
])

# print(np.linalg.solve(num_5, res_5))

num_6 = np.array([
    [2,1,5],
    [1,3,1],
    [3,4,6]
])

print(np.linalg.matrix_rank(num_6))