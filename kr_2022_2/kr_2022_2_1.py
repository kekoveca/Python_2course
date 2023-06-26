N, M = (int(el) for el in input().split())

field = [0] * N
for i in range(N):
    field[i] = [0] * M

K = int(input())

for i in range(K):
    X, Y = (int(el) for el in input().split())
    for j in range(N):
        field[j][Y] += 1
    for k in range(M):
        field[X][k] += 1
    field[X][Y] -= 1

answer = 0

for i in range(N):
    for j in range(M):
        if field[i][j] > 1:
            answer += 1

print(answer)