import pandas as pd
ds = '/Users/yunchaewon/gesis/datasets/CONAN/multitarget_KN_grounded_CN/multitarget_KN_grounded_CN.csv'
df = pd.read_csv(ds) #, lineterminator='\n')
source = 'chung2021'

new_df = df[['hate_speech', 'target']].copy()
new_df = new_df.rename(columns={"hate_speech": "text", "target":"label"})

new_df.loc[:, "text"] = new_df["text"].apply(lambda x : x.replace('\n', '\\n'))
# should i check unique?

new_df['source'] = source 
new_df['language'] = 'en'

col_order = ['text', 'label', 'language', 'source'] #, 'dataset']
new_df = new_df.reindex(columns=col_order)
print(new_df.head())
new_df.to_csv(f'formatted/{source}.csv', index=False, sep='\t')

