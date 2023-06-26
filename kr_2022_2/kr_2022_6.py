import numpy as np

path_im = input()
path_filter = input()

filtr = np.loadtxt(path_filter)
im = np.loadtxt(path_im)

P, N = [float(el) for el in input().split()]
N = int(N)

for i in range(N):
    res1 = np.matmul(filtr, im)
    k = np.count_nonzero(np.abs(res1) > P)
    im = res1
    print(k)