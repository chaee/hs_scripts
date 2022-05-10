import pandas as pd
ds = '/Users/yunchaewon/gesis/datasets/CONAN/Multitarget-CONAN/Multitarget-CONAN.csv'
df = pd.read_csv(ds) #, lineterminator='\n')
source = 'fanton2021'

new_df = df[['HATE_SPEECH', 'TARGET']].copy()
new_df = new_df.rename(columns={"HATE_SPEECH": "text", 'TARGET':'label'})

new_df.loc[:, "text"] = new_df["text"].apply(lambda x : x.replace('\n', '\\n'))
new_df['label'] = df[df.columns[2:4]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

new_df['source'] = source 
new_df['language'] = 'en'

col_order = ['text', 'label', 'language', 'source'] #, 'dataset']
new_df = new_df.reindex(columns=col_order)
print(new_df.head())
new_df.to_csv(f'formatted/{source}.csv', index=False, sep='\t')

