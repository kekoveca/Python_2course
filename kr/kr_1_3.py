import decimal as dm

x = str(input())
arr = [s for s in x]
try:
    ind = arr.index('.')
except:
    print(int(x) - 1)
else:
    print(format(round((float(x) - pow(10, -(len(arr[ind:]) - 1))), len(arr[ind:]) - 1), f'.{len(arr[ind:]) - 1}f'))
