arr = input()
arr = arr.split(" ")
ints = []

for el in arr:
    ints.append(int(el))

print(max(ints) - min(ints))
