from operator import xor
import numpy as np

def rightRotate(lists, num):
    output_list = []
 
    # Will add values from n to the new list
    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])
 
    # Will add the values before
    # n to the end of new list
    for item in range(0, len(lists) - num):
        output_list.append(lists[item])
 
    return output_list

str = 'hello world'

binar = list(format(el, 'b') for el in bytearray(str, "utf-8"))
length = bin(len(binar)*8)
binar.append('10000000')
for i in range(56 - len(binar)):
    binar.append('00000000')
binar[-1] = length[2:]
# print(binar)

for i in range(len(binar)):
    if len(binar[i]) != 8:
        binar[i] = '0' + binar[i]

for i in range(len(binar)):
    if len(binar[i]) != 8:
        binar[i] = '0' + binar[i]

for i in range(len(binar)):
    if len(binar[i]) != 8:
        binar[i] = '0' + binar[i]

binar1 = ''.join(binar)
w1 = binar1[32:64]

a1 = int((''.join(rightRotate(w1, 7))), 2)
a2 = int((''.join(rightRotate(w1, 18))), 2)
a3 = int(w1, 2) >> 3
print("a1 =", a1)
print("a2 =", a2)


s0 = a1 ^ a2 ^ a3
print(bin(s0))

w16 = int(binar1[0:32], 2) + s0
print(bin(w16))