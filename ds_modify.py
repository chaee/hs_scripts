import pandas as pd
import sys

new_df = df[['text', 'dataset']].copy()
meta = {{'source': 'chung2019', 'cols':{['hateSpeech', 'hsType', 'hsSubType', 'cn_id']}, {'source':'samory2021en', 'cols':[]}}

#new_df['label'] = [(rdf.toxicity).strip(), str(df.sexist).strip()]
new_df['label'] = df[df.columns[3:5]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

new_df = new_df.reindex(columns=col_order)

print(new_df.head())
new_df.to_csv('formatted/samory2021en.csv', index=False, sep='\t')

def pick_cols(df, cols):
    # modify if necessary
    new_df = df[[cols]].copy()
    # new_df.loc[:, "text"] = new_df["text"].apply(lambda x : x.replace('\n', '\\n'))
    if df.source == 'Chung2019':
        new_df['language'] = new_df['cn_id'].apply(lambda x: x[:2]).lower()
    return new_df 
    

def add_info(df, cols):
    new_df['source'] = 'samory2021en'
    col_order = ['text', 'label', 'language', 'source', 'dataset']

if __name__ == '__main__':
    '''
    python3 ds_modify.py /Users/yunchaewon/gesis/datasets/CONAN/CONAN/CONAN.csv formatted/ Chung2019
    '''
    
    data_path = sys.argv[1]
    save_path = sys.argv[2] #formatted/
    source = sys.argv[3]
    df = pd.read_csv(data_path, lineterminator='\n')

    cols = 
    new_df = pick_cols(df, cols)
   
    missing_cols = ['source']
    new_df = add_info(new_df, missing_cols):
    
