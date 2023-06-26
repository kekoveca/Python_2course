import numpy as np
N = int(input())

points = []
for i in range(N):
    X, Y, F = [float(el) for el in input().split()]
    cos = X / np.sqrt(X**2 + Y**2)
    sin = Y / np.sqrt(X**2 + Y**2)
    points.append([F*cos, F*sin])

points = np.array(points, dtype = float)

print(f'{points.sum(0)[0]:.4f} {points.sum(0)[1]:.4f}')
