N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))

pos = [x for x in arr if x >= 0]
neg = [x for x in arr if x < 0]

res = sorted(pos) + sorted(neg, key = abs)
for el in res:
    print(el, end=' ')