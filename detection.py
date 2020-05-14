import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest

file = input('name: ')
plot=input('plot(y/n): ')
empresa = pd.read_csv(file+'.csv', sep=',')
empresa = empresa[['date', 'amount']]

data = empresa[['amount']]
scaler = StandardScaler()
np_scaled = scaler.fit_transform(data)
data = pd.DataFrame(np_scaled)

# train isolation forest
model = IsolationForest(contamination=0.1)
model.fit(data)
empresa['anomaly2'] = pd.Series(model.predict(data))
a = empresa.loc[empresa['anomaly2'] == -1, ['date', 'amount']]
a.to_csv('anomalies_' + file+'.csv')
# visualization
if plot=='y':
    fig, ax = plt.subplots(figsize=(10, 6))

     # anomaly

    ax.plot(empresa['date'], empresa['amount'], color='blue', label='Normal')
    ax.scatter(a['date'], a['amount'], color='red', label='Anomaly')
    plt.legend()
    plt.show()
