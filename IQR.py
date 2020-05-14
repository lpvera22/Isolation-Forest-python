import pandas as pd
import numpy as np

file = input('name: ')

empresa = pd.read_csv(file + '.csv', sep=',')

empresa = empresa[['date', 'amount']]
empresa_sorted = sorted(empresa.amount.values)
print(empresa_sorted)
q1, q3 = np.percentile(empresa_sorted, [25, 75])
print(q1, q3)
iqr = q3 - q1
print(iqr)
lower_bound = q1 - (1.5 * iqr)
print(lower_bound)
upper_bound = q3 + (1.5 * iqr)
print(upper_bound)
a = empresa[(empresa.amount < lower_bound) | (empresa.amount > upper_bound)]
a.to_csv('IQR_' + file+'.csv')
