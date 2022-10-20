import collections as c

f_path = input()
wrd = input().lower()
l = []
try:
    with open(f_path, 'r') as f:
        srt = f.read().split()
    for el in srt:
        try:
            float(el)
        except:
            l.append(el.lower())
    cnt = c.Counter(l)
    if cnt.get(wrd) == None:
        print(0)
    else:
        print(cnt.get(wrd))

except:
    print(0)