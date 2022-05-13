import pandas as pd
ds = '/Users/yunchaewon/gesis/datasets/hatecheck-data/all_cases.csv'
df = pd.read_csv(ds) #, lineterminator='\n')
source = 'roettger2020'

new_df = df[['test_case', 'label_gold']].copy()
new_df = new_df.rename(columns={"test_case": "text", 'label_gold':'label'})

new_df.loc[:, "text"] = new_df["text"].apply(lambda x : x.replace('\n', '\\n'))

new_df['source'] = source 
new_df['language'] = 'en'

col_order = ['text', 'label', 'language', 'source'] #, 'dataset']
new_df = new_df.reindex(columns=col_order)
print(new_df.head())
new_df.to_csv(f'formatted/{source}.csv', index=False, sep='\t')

