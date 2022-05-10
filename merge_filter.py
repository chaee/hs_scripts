import pandas as pd
import numpy as np
'''
df = pd.read_csv('formatted/sarkar2021en.csv', lineterminator='\n', sep='\t')
print(df.head())
'''
files = ['formatted/chung2019.csv', 'formatted/chung2021.csv', 'formatted/fanton2021.csv', 'formatted/samory2021en.csv', 'formatted/sarkar2021en.csv']

df = pd.read_csv('formatted/formatted.csv', lineterminator='\n', sep='\t',delimiter=None)
df = df[df.language=='en']

for ds in files:
    print(ds)
    ndf = pd.read_csv(ds, lineterminator='\n', sep='\t', skiprows=0, delimiter=None) 
    ndf = ndf[ndf.language=='en']
    print(ndf.head())
    pd.concat([df, ndf], verify_integrity=True, axis=1, ignore_index=True)

df.to_csv(df, 'merged.csv', index=False, sep='\t')

