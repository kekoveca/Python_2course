minX, maxX = (float(el) for el in input().split())
minY, maxY = (float(el) for el in input().split())
minZ, maxZ = (float(el) for el in input().split())

N = int(input())

points = []

for i in range(N):
    points.append([float(el) for el in input().split()])

k = 0

for el in points:
    if minX <= el[0] <= maxX and minY <= el[1] <= maxY and minZ <= el[2] <= maxZ:
        k += 1

print(k)