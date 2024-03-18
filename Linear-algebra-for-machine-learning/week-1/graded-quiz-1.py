import numpy as np

num_1 = np.array([
    [10, 5, 10],
    [5, 10, 15],
    [6, 4, 5],
], dtype=int)

res_1 = np.array([5,7,6], dtype=int)

# print(np.linalg.solve(num_1, res_1))

num_3 = np.array([
    [1,2,1],
    [2,1,1],
    [-1,2,1],
])

num_6 = np.array([
    [1,2,3],
    [0,2,2],
    [1,4,5],
])

print(np.linalg.det(num_3))
print(np.linalg.det(num_6))
# lambdas, v = np.linalg.eig(num_3.T)
# print(num_3[lambdas==0])

# HOW TO CHECK LINEARLY DEPENDENT OR LINEARLY INDEPENDENT
# for i in range(num_3.shape[0]):
#     for j in range(num_3.shape[0]):
#         if i != j:
#             inner_product = np.inner(
#                 num_3[:,i],
#                 num_3[:,j]
#             )
#             norm_i = np.linalg.norm(num_3[:,i])
#             norm_j = np.linalg.norm(num_3[:,j])

#             print('I: ', num_3[:,i])
#             print('J: ', num_3[:,j])
#             print('Prod: ', inner_product)
#             print('Norm i: ', norm_i)
#             print('Norm j: ', norm_j)
#             if np.abs(inner_product - norm_j * norm_i) < 1E-5:
#                 print('Dependent')
#             else:
#                 print('Independent')