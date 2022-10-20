arr = str(input()).split(sep='0')
print(len(max(arr, key=lambda x: len(x))))
