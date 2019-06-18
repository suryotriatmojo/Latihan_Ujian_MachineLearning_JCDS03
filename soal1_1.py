import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

plt.style.use('seaborn-darkgrid')

plt.plot(df['Tahun'], df[max_2010], marker = '.', color = 'green', label = max_2010[0])
plt.plot(df['Tahun'], df[min_1971], marker = '.', color = 'blue', label = min_1971[0])
plt.plot(df['Tahun'], df[total], marker = '.', color = 'red', label = total)
plt.title('Jumlah Penduduk {} (1971 - 2000)'.format(total))
plt.xlabel('Tahun')
plt.ylabel('Jumlah Penduduk (ratus juta jiwa')
plt.legend()
plt.show()