import matplotlib.pyplot as plt
import numpy as np

N_array = []
data_array = []

for i in range(5):
    N_array.append(np.loadtxt(f"dead_moroz/00{i+1}.dat", max_rows=1, dtype= int))
    data_array.append(np.loadtxt(f"dead_moroz/00{i+1}.dat", skiprows=1, max_rows= N_array[i], dtype= float))

X_array = []
Y_array = []

for j in range(5):
    X_array.append([data_array[j][i, 0] for i in range(N_array[j])])
    Y_array.append([data_array[j][i, 1] for i in range(N_array[j])])

for i in range(5):
    plt.subplots(figsize = (16,10), dpi = 400)
    plt.scatter(X_array[i], Y_array[i], c = 'blue', s = 750/len(Y_array[i]))
    plt.title(f"Number of points: {N_array[i]}")
    plt.savefig(f"plot{i+1}.png")