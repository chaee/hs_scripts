import pandas as pd
ds = '/Users/yunchaewon/gesis/datasets/chess_racism/recreate_dataset/sample_comments.json'
df = pd.read_json(ds, orient='records', typ='series', dtype=dict)
new_df = pd.DataFrame({'text':[]})
new_df['text'] = df.values
new_df['label'] = 'benign chess'
new_df['language'] = 'en'
new_df['source'] = 'sarkar2021en'

col_order = ['text', 'label', 'language', 'source']#, 'dataset']
new_df = new_df.reindex(columns=col_order)

print(new_df.head())
new_df.to_csv('formatted/sarkar2021en.csv', index=False, sep='\t')
