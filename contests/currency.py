import numpy as np
import matplotlib.pyplot as plt
import json

f = open("contests/currency.txt",'r')

file = json.load(f)
means = []
for el in file:
    if type(el['ask']) == float:
        means.append(el['ask'])

means = np.array(means)

print(means.mean())