n = input()
while True:
    n = sum(map(int, str(n)))
    if int(n) < 10:
        break

print(n)