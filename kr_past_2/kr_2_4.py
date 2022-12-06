import numpy as np

N = int(input())

temperatures = []
pressures = []

for i in range(N):
    tmp = [float(el) for el in input().split()]
    if tmp[0] >= -70 and tmp[0] <= 80:
        pressures.append(tmp[1])
    temperatures.append(tmp[0])

print(f'{np.mean(temperatures):.4f}', f'{np.mean(pressures):.4f}')