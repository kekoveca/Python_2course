ls = [int(s) for s in input().split()]
ls.sort()
for el in ls:
    if ls.count(el) == 1:
        max = el
print(max)