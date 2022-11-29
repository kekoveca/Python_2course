import requests as re
import collections as cl

for i in range(25):
    r = []
    for j in range(5):
        r.append(re.get(f'https://demoflask.kekoveca.repl.co/propose/{j}/{i + 1}').text)
    most_freq = max(list(cl.Counter(r).items()), key= lambda e: e[1])[0]
    for j in range(5):
        re.get(f'https://demoflask.kekoveca.repl.co/accept/{j}/{i + 1}/{most_freq}')