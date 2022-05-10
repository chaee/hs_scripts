import pandas as pd
ds = '/Users/yunchaewon/gesis/datasets/CONAN/CONAN/CONAN.csv'
df = pd.read_csv(ds) #, lineterminator='\n')
source = 'chung2019'

new_df = df[['hateSpeech', 'hsType', 'hsSubType']].copy()
new_df = new_df.rename(columns={"hateSpeech": "text"})

new_df.loc[:, "text"] = new_df["text"].apply(lambda x : x.replace('\n', '\\n'))
new_df['label'] = df[df.columns[2:4]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

new_df['source'] = source 
new_df['language'] = df['cn_id'].apply(lambda x: x[:2].lower())

col_order = ['text', 'label', 'language', 'source'] #, 'dataset']
new_df = new_df.reindex(columns=col_order)
print(new_df.head())
new_df.to_csv(f'formatted/{source}.csv', index=False, sep='\t')

