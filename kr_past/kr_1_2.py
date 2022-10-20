arr = [s for s in input().split()]
l = []
for el in arr:
    try:
        l.append(int(el))
    except ValueError:
        pass

print(sum(l))