NM = input()
N, M = NM.split()
K = input()

M = int(M)
N = int(N)

surf = []

for i in range(N):
    surf.append([])

for i in range(N):
    for j in range(M):
        surf[i].append(0)


for i in range(int(K)):
    tmp = [int(s) for s in input().split()]
    if tmp[0] < 0 or tmp[1] > N or tmp[2] < 0 or tmp[3] > M:
        print("broken")
        quit()
    for i in range(tmp[0], tmp[1]):
        for j in range(tmp[2], tmp[3]):
            surf[i][j]+=1

for i in range(N):
    for j in range(M):
        if surf[i][j] > 1:
            print("broken")
            quit()

print("correct")