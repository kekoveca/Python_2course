import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("frames.dat", dtype = float)
X_array = []
Y_array = []

for i in range(6):
    X_array.append(data[2*i])
    Y_array.append(data[2*i + 1])


plt.subplots(nrows=3, ncols=2, figsize = (16, 10), dpi = 400)
for i in range(6):
    plt.subplot(int(f"32{i+1}"))
    plt.plot(X_array[i], Y_array[i])
    plt.title(f"Frame {i+1}")
    plt.grid("on")
    plt.minorticks_on()
    plt.savefig("frames.png")