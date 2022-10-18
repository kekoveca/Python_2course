ls = [str(s) for s in input().split()]
d = {x: ls.count(x) for x in ls}
srt = sorted(d.items(), key= lambda elem: (-elem[1], elem[0]))
for elem in srt:
    print(elem[1], elem[0])