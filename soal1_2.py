import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_excel(
    'datasets/indo_12_1.xls',
    index_col = 0,
    header = 3,
    skipfooter = 2,
    na_values = '-'
)

max_2010 = df[df[2010] == df[2010][:-1].max()].index.values
min_1971 = df[df[1971] == df[1971].min()].index.values
total = df.iloc[-1].name

df = df.T.reset_index().rename(columns = {'index' : 'Tahun'})

model_max_2010 = linear_model.LinearRegression()
model_max_2010.fit(df[['Tahun']], df[max_2010])
max_2010_best = model_max_2010.predict(df[['Tahun']])
max_2010_2050 = model_max_2010.predict([[2050]])

model_min_1971 = linear_model.LinearRegression()
model_min_1971.fit(df[['Tahun']], df[min_1971])
min_1971_best = model_min_1971.predict(df[['Tahun']])
min_1971_2050 = model_min_1971.predict([[2050]])

model_total = linear_model.LinearRegression()
model_total.fit(df[['Tahun']], df[total])
total_best = model_total.predict(df[['Tahun']])
total_2050 = model_total.predict([[2050]])

print('Prediksi jumlah penduduk {} di tahun 2050: {}'.format(max_2010[0], int(max_2010_2050[0][0])))
print('Prediksi jumlah penduduk {} di tahun 2050: {}'.format(min_1971[0], int(min_1971_2050[0][0])))
print('Prediksi jumlah penduduk {} di tahun 2050: {}'.format(total, int(total_2050[0])))

plt.style.use('seaborn-darkgrid')

plt.plot(df['Tahun'], df[max_2010], marker = '.', color = 'green', label = max_2010[0])
plt.plot(df['Tahun'], max_2010_best, color = 'yellow', alpha = 0.5)

plt.plot(df['Tahun'], df[min_1971], marker = '.', color = 'blue', label = min_1971[0])
plt.plot(df['Tahun'], min_1971_best, color = 'yellow', alpha = 0.5)

plt.plot(df['Tahun'], df[total], marker = '.', color = 'red', label = total)
plt.plot(df['Tahun'], total_best, color = 'yellow', alpha = 0.5, label = 'Best Fit Line')

plt.title('Jumlah Penduduk {} (1971 - 2000)'.format(total))
plt.xlabel('Tahun')
plt.ylabel('Jumlah Penduduk (ratus juta jiwa')
plt.legend()
plt.show()