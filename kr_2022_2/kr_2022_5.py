from PIL import Image
import numpy as np

file_path = input()
img = Image.open(file_path)
data = np.array(img)

new_data = data[::, ::, 0] * 0.299 + data[::, ::, 1] * 0.587 + data[::, ::, 2]*0.114
min = np.min(new_data)
max = np.max(new_data)

print(int(min), int(max))