import pandas as pd
from distfit import distfit
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


file_path = r'file\distr_c.txt'
data = pd.read_csv(file_path, header=None, names=['value'])

print(data.head())

dist = distfit()

dist.fit_transform(data['value'].to_numpy())

dist.plot()
plt.show()

print("Distribution:", dist.model['name'])
print("Parameters:", dist.model['params'])
