import matplotlib.pyplot as plt
import numpy as np

data_raw = np.loadtxt("students.csv", dtype=str)
data = []

for i in range(len(data_raw)):
    data.append(tuple(data_raw[i].split(';')))

# print(sorted(data, key = lambda e: e[1]))

preps = sorted(data, key = lambda e: (e[0], e[2]))

plt.subplots(nrows=2, ncols=1, figsize = (16, 10), dpi = 400)
plt.subplot(11)
plt.bar(['prep1','prep2','prep3','prep4','prep5','prep6','prep7'],  )
