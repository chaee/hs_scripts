import pandas as pd
df = pd.read_csv('../datasets/call-me-sexist-but/sexism_data.csv')
new_df = df[['text', 'dataset']].copy()
#new_df['label'] = [(rdf.toxicity).strip(), str(df.sexist).strip()]
new_df['label'] = df[df.columns[3:5]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

new_df['source'] = 'samory2021en'
new_df['language'] = 'en'
col_order = ['text', 'label', 'language', 'source', 'dataset']
new_df = new_df.reindex(columns=col_order)

print(new_df.head())
new_df.to_csv('../formatted/samory2021en.csv', index=False, sep='\t')

