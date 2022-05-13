import pandas as pd
ds = '/Users/yunchaewon/gesis/datasets/convabuse/1_full/ConvAbuseEMNLPfull.csv'
df = pd.read_csv(ds) #, lineterminator='\n')
source = 'cercascurry2021'

new_df = df[['user']].copy()
new_df = new_df.rename(columns={"user": "text"})

new_df.loc[:, "text"] = new_df["text"].apply(lambda x : x.replace('\n', '\\n'))
new_df['label'] = df[df.columns[8:]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

new_df['source'] = source 
new_df['language'] = 'en'

col_order = ['text', 'label', 'language', 'source'] #, 'dataset']
new_df = new_df.reindex(columns=col_order)
print(new_df.head())
new_df.to_csv(f'formatted/{source}.csv', index=False, sep='\t')

