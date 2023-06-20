import pandas as pd


df = pd.DataFrame(
    ['1', 'Fares', 32, True],
    ['2', 'Elena', 23, False],
    ['3', 'Jessica', 18, True],
)
df.columns = ['id', 'name', 'age', 'married']

print(df)
print()
print(df[['id', 'name']])
