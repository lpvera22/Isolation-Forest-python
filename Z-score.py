import numpy as np
import pandas as pd

file = input('name: ')
empresa = pd.read_csv(file + '.csv', sep=',')

empresa = empresa[['date', 'amount']]


def outliers_modified_z_score(ys):
    threshold = 3.5

    median_y = np.median(ys)
    median_absolute_deviation_y = np.median([np.abs(y - median_y) for y in ys])
    modified_z_scores = [0.6745 * (y - median_y) / median_absolute_deviation_y
                         for y in ys]
    return np.where(np.abs(modified_z_scores) > threshold)


print(outliers_modified_z_score(empresa['amount'].values))
