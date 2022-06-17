import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('datasets/titles.csv')

# heead = dataset.head()
# print(heead)

adda = dataset[dataset.production_countries == 'US']
print(adda)
# from_where = dataset[dataset['production_countries'] == 'US']['release_year']
# print(from_where)