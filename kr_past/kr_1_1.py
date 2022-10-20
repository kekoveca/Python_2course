arr = sorted([int(s) for s in input().split()], reverse= True)
N = int(input())
arr_1 = arr[:N]
arr_1 = arr_1[::-1]
for i in range(N):
    print(arr_1[i], sep = '\n')