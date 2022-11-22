N = int(input())
data = []
data_lower = []

for i in range(N):
    arr = [s for s in input().split()]
    data += arr
print(data)

data_set = list(set(data))
print(sorted(data_set))

