import hashlib
import numpy as np

data = np.loadtxt('data.txt', dtype = str)
depths =[]
names = []
bloom1 = [0] * 50
bloom2 = [0] * 50

for el in data:
    depths.append(el[0])
    names.append(el[2:])

for depth, name in zip(depths, names):
    hobj1 = hashlib.sha256((name + '1').encode('utf-8'))
    hobj2 = hashlib.sha256((name + '2').encode('utf-8'))
    ind1 = int(hobj1.hexdigest(), base= 16)%50
    ind2 = int(hobj2.hexdigest(), base= 16)%50
    bloom1[ind1] += 1
    bloom1[ind2] += 1

names_2 = []

for depth, name in zip(depths, names):
    hobj1 = hashlib.sha256((name + '1').encode('utf-8'))
    hobj2 = hashlib.sha256((name + '2').encode('utf-8'))
    ind1 = int(hobj1.hexdigest(), base= 16)%50
    ind2 = int(hobj2.hexdigest(), base= 16)%50
    if bloom1[ind1] > 1 and bloom1[ind2] > 1:
        names_2.append(name)

print(names_2)


for name in names_2:
    hobj1 = hashlib.sha256((name + '3').encode('utf-8'))
    hobj2 = hashlib.sha256((name + '4').encode('utf-8'))
    ind1 = int(hobj1.hexdigest(), base= 16)%50
    ind2 = int(hobj2.hexdigest(), base= 16)%50
    bloom2[ind1] = 1
    bloom2[ind2] = 1


print(bloom1)
print(bloom2)

def check(str):
    hobj1 = hashlib.sha256((str + '1').encode('utf-8'))
    hobj2 = hashlib.sha256((str + '2').encode('utf-8'))
    hobj3 = hashlib.sha256((str + '3').encode('utf-8'))
    hobj4 = hashlib.sha256((str + '4').encode('utf-8'))
    ind1 = int(hobj1.hexdigest(), base= 16)%50
    ind2 = int(hobj2.hexdigest(), base= 16)%50
    ind3 = int(hobj3.hexdigest(), base= 16)%50
    ind4 = int(hobj4.hexdigest(), base= 16)%50
    return ind1, ind2, ind3, ind4

ind1, ind2, ind3, ind4 = check('White')

if bloom1[ind1] >= 1 and bloom1[ind2] >= 1:
    print('Есть в первом фильтре')
    if bloom2[ind3] == 1 and bloom2[ind4] == 1:
        print('Есть во втором фильтре -> есть в списке')
    else:
        print('Нету во втором фильтре')
else:
    print('Нету в первом фильтре')
