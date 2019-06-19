import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

# plot figure
plt.figure('Populasi {}'.format(indo.index[0]), figsize = (12,8))
plt.style.use('seaborn-darkgrid')

plt.plot(max_2010.columns.values, max_2010.iloc[0], marker = 'o', label = max_2010.index[0], color = 'green')
plt.plot(min_1971.columns.values, min_1971.iloc[0], marker = 'o', label = min_1971.index[0], color = 'blue')
plt.plot(indo.columns.values, indo.iloc[0], marker = 'o', label = indo.index[0], color = 'red')

plt.title('Jumlah Penduduk {} (1971 - 2000)'.format(indo.index[0]))
plt.xlabel('Tahun')
plt.ylabel('Jumlah Penduduk (Ratus Juta Jiwa)')
plt.legend()

plt.grid(True)
plt.tight_layout()

# cara ngeplot lainnya menggunakan DataFrame
# compile = pd.concat([max_2010, min_1971, indo])
# compile.T.plot(marker = 'o', color = ['green', 'blue', 'red'])
# print(compile.T)

plt.show()