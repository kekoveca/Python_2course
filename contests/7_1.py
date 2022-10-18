ls = [str(s) for s in input().split()]
srt = []
for elem in ls:
    try:
        with open(elem, 'r') as f:
            srt.extend(f.read().split())
    except:
        pass
for el in sorted({i for i in srt}):
    print(el, end= ' ')