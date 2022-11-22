import statistics
import random
print(random.randint(1,2))

N = int(input())
arr = []
for i in range(N):
    arr.append([s for s in input().split()])

arr.sort()

dc = {x[0]: [] for x in arr}

for el in arr:
    dc[el[0]].append(el[1])

strs = []
M = int(input())
for i in range(M):
    strs.append(input())

for elem in strs:
    try:
        print(statistics.median_low(dc[elem]))
    except:
        print('no data')