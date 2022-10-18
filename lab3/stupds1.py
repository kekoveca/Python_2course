import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('lab3/students.csv', sep=';')
print(df)


df1 = df[df['Prep'] == 'prep1']
print(df[df['Prep'] == 'prep1'])
# df1.plot(x = 'Prep', kind='bar', stacked=True,
#         title='Stacked Bar Graph by dataframe')
# plt.show()
for i in range (10, 2, -1):
        df1.loc[:, f'Оценка {i}'] = df1.loc[:, 'Mark'].count(i)

print(df1)