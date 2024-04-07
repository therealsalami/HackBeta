import pandas as pd
df = pd.read_csv('updatedLeather.csv')


def counter():
    # Directly sum each column and store the results in a list
    counts = [df[column].sum() for column in ['BeefCount', 'shoeCount', 'coatCount', 'leatherCount']]
    return counts

print(counter())
