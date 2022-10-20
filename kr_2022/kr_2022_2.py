arr = list({s for s in input().split()})
arr1 = sorted(arr, key = lambda el: (-len(el), el[0]))
for el in arr1:
    print(el, sep = '\n')