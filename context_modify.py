import pandas as pd
ds = '/Users/yunchaewon/gesis/datasets/context_toxicity/data/CCC.csv'
df = pd.read_csv(ds) #, lineterminator='\n')
source = 'xenos2021'

new_df = df[['text']].copy()
tox_codes = df[['tox_codes_oc', 'tox_codes_ic']].copy()
new_df = new_df.rename(columns={"hateSpeech": "text"})

new_df.loc[:, "text"] = new_df["text"].apply(lambda x : x.replace('\n', '\\n'))
new_df['label'] = tox_codes[tox_codes.columns[:]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

new_df['source'] = source 
new_df['language'] = 'en'

col_order = ['text', 'label', 'language', 'source'] #, 'dataset']
new_df = new_df.reindex(columns=col_order)
print(new_df.head())
new_df.to_csv(f'formatted/{source}.csv', index=False, sep='\t')

