import numpy as np

N, M = (int(el) for el in input().split())
K = int(input())
field = np.zeros((N, M), dtype= int)

for i in range(K):
    X, Y = (int(el) for el in input().split())
    for j in range(N):
        field[j, Y] += 1
    for k in range(M):
        field[X, k] += 1
    field[X, Y] -= 1
    
k = 0
for el in field:
    for elem in el:
        if elem > 1:
            k += 1

print(k)