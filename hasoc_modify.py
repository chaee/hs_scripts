import pandas as pd
ds = '/Users/yunchaewon/gesis/datasets/HASOC_english/hasoc2019_en_test-2919.tsv'
#ds = '/Users/yunchaewon/gesis/datasets/HASOC_english/english_dataset.tsv'
df = pd.read_csv(ds, lineterminator='\n', sep='\t')
source = 'mandl2019test'

new_df = df[['text', 'task_1', 'task_2', 'task_3']].copy()

new_df.loc[:, "text"] = new_df["text"].apply(lambda x : x.replace('\n', '\\n'))
new_df['label'] = df[df.columns[1:]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

new_df['source'] = source 
new_df['language'] = 'en'

col_order = ['text', 'label', 'language', 'source'] #, 'dataset']
new_df = new_df.reindex(columns=col_order)
print(new_df.head())
new_df.to_csv(f'formatted/{source}.csv', index=False, sep='\t')

