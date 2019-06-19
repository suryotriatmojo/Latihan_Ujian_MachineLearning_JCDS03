import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_excel(
    'datasets/indo_12_1.xls',
    index_col = 0,
    header = 3,
    skipfooter = 2,
    na_values = ['-']
)

# df prov 2010 jumlah penduduk max
max_2010 = df[df[2010] == df[2010][:-1].max()]

# df prov 1971 jumlah penduduk min
# df.dropna(subset = [1971])  # menghapus di kolom 1971 yang ada NaN
min_1971 = df[df[1971] == df[1971].min()]

# df INDONESIA
indo = df[df[2010] == df[2010].max()]

# modeling linear regression
model_max_2010 = linear_model.LinearRegression()
model_min_1971 = linear_model.LinearRegression()
model_indo = linear_model.LinearRegression()

# print(max_2010.columns.values.reshape(-1, 1)) # reshape jadi 2D dgn shape = (6, 1)
# sama dengan
# print(max_2010.columns.values.reshape(6, 1))

# training
x_max_2010 = max_2010.columns.values.reshape(-1, 1)
y_max_2010 = max_2010.values[0]
model_max_2010.fit(x_max_2010, y_max_2010)

x_min_1971 = min_1971.columns.values.reshape(-1, 1)
y_min_1971 = min_1971.values[0]
model_min_1971.fit(x_min_1971, y_min_1971)

x_indo = indo.columns.values.reshape(-1, 1)
y_indo = indo.values[0]
model_indo.fit(x_indo, y_indo)

# 2050 prediction
max_2010_2050 = model_max_2010.predict([[2050]])
min_1971_2050 = model_min_1971.predict([[2050]])
indo_2050 = model_indo.predict([[2050]])

print('Prediksi jumlah penduduk {} di tahun 2050: {}'.format(max_2010.index[0], int(max_2010_2050[0])))
print('Prediksi jumlah penduduk {} di tahun 2050: {}'.format(min_1971.index[0], int(min_1971_2050[0])))
print('Prediksi jumlah penduduk {} di tahun 2050: {}'.format(indo.index[0], int(indo_2050[0])))

# plot figure
plt.figure('Prediksi Populasi {}'.format(indo.index[0]), figsize = (12,8))
plt.style.use('seaborn-darkgrid')

# plot real data
plt.plot(max_2010.columns.values, max_2010.iloc[0], marker = 'o', label = max_2010.index[0], color = 'green')
plt.plot(min_1971.columns.values, min_1971.iloc[0], marker = 'o', label = min_1971.index[0], color = 'blue')
plt.plot(indo.columns.values, indo.iloc[0], marker = 'o', label = indo.index[0], color = 'red')

# plot best fit data => y = mx + c
plt.plot(
    max_2010.columns.values,
    model_max_2010.coef_ * max_2010.columns.values + model_max_2010.intercept_,
    color = 'yellow',
    alpha = 0.5
)
plt.plot(
    min_1971.columns.values,
    model_min_1971.coef_ * min_1971.columns.values + model_min_1971.intercept_,
    color = 'yellow',
    alpha = 0.5
)
plt.plot(
    indo.columns.values,
    model_indo.coef_ * indo.columns.values + model_indo.intercept_,
    label = 'Best Fit Line',
    color = 'yellow',
    alpha = 0.5
)

plt.title('Jumlah Penduduk {} (1971 - 2000)'.format(indo.index[0]))
plt.xlabel('Tahun')
plt.ylabel('Jumlah Penduduk (Ratus Juta Jiwa)')
plt.legend()

plt.grid(True)
plt.tight_layout()

plt.show()