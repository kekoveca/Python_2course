import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('lab_pandas/transactions.csv', sep=',')
df1_sorted = df.sort_values(by='SUM', ascending=False)
tmp = df1_sorted[df1_sorted['STATUS'] == 'OK']
print(f"Три самых больших платежа: \n {tmp.iloc[0:3]}") ## ЗАДАЧА 1

print('================================================')

tmp = df[df['STATUS'] == 'OK']
tmp = tmp[tmp['CONTRACTOR'] == 'Umbrella, Inc']
summa = tmp['SUM'].sum()
print(f"Сумма всех проведенных платежей Umbrella: {summa}")

print('================================================')


df = pd.read_csv('lab_pandas/flights.csv', sep=',')
nimble = df[df['CARGO'] == 'Nimble']
nimble_quantity = len(nimble.index)
nimble_sum = nimble.loc[:, 'PRICE'].sum()
nimble_weight = nimble.loc[:, 'WEIGHT'].sum()

jumbo = df[df['CARGO'] == 'Jumbo']
jumbo_quantity = len(jumbo.index)
jumbo_sum = jumbo.loc[:, 'PRICE'].sum()
jumbo_weight = jumbo.loc[:, 'WEIGHT'].sum()

medium = df[df['CARGO'] == 'Medium']
medium_quantity = len(medium.index)
medium_sum = medium.loc[:, 'PRICE'].sum()
medium_weight = medium.loc[:, 'WEIGHT'].sum()

quantities = [nimble_quantity, jumbo_quantity, medium_quantity]
sums = [nimble_sum, jumbo_sum, medium_sum]
weights = [nimble_weight, jumbo_weight, medium_weight]


labels = ['Nimble', 'Jumbo', 'Medium']
width = 0.2

plt.subplot(3,1,1)
plt.bar(labels, quantities, width, label = 'Количество рейсов', color = 'blue')
plt.legend()
plt.subplot(3,1,2)
plt.bar(labels, sums, width, label = 'Сумма стоимостей', color = 'red')
plt.legend()
plt.subplot(3,1,3)
plt.bar(labels, weights, width, label = 'Сумма веса грузов', color = 'green')
plt.legend()

plt.show()