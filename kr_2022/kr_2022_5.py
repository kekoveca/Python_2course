f_path = input()
arr = []
arr1 =[]
try:
    with open(f_path, 'r') as f:
        srt = f.read().split(sep='\n')
    for el in srt:
        arr.append(el.split())
    for el in arr:
        arr1.append([eval(i) for i in el])
    dc = {sum(x): len(x) for x in arr1}
    srt = sorted(dc.items(), key= lambda elem: (-elem[1], -elem[0]))
    print(srt[0][0])
except:
    print(0)