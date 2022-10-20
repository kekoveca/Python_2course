arr = [s for s in input().split()]
M = int(arr[0])
N = int(arr[1])

fld = []

for i in range(N):
    fld.append(list(input()))

arr = [s for s in input().split()]
X = int(arr[0])
Y = int(arr[1])
FOV = int(arr[2])


if X - FOV < 0:
    try:
        for y in range(Y - FOV, Y + FOV + 1):
            print(''.join(fld[y][0:X+FOV+1]))
    except:
        pass
elif X - FOV > M:
    for y in range(Y - FOV, Y + FOV + 1):
        print(''.join(fld[y][X-FOV:M + 1]))
elif Y - FOV < 0:
    try:
        for y in range(0, Y + FOV + 1):
            print(''.join(fld[y][X-FOV:X+FOV+1]))
    except:
        pass
elif Y - FOV > N:
    for y in range(Y - FOV, N + 1):
        print(''.join(fld[y][X-FOV:X+FOV+1]))
else:
    for y in range(Y - FOV, Y + FOV + 1):
        print(''.join(fld[y][X-FOV:X+FOV+1]))