#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
pd.options.display.max_colwidth=200


# In[67]:


ds = '/Users/yunchaewon/gesis/datasets/HateXplain/Data/dataset.json'
df = pd.read_json(ds)#, typ='frame')#, orient='records')#, lineterminator='\n')
# allowed orients are {'split','records','index', 'columns','values', 'table'}
source = 'mathew2021'


# In[68]:


df = df.T
df.head()


# In[75]:


df.annotators[0]

def change(anns):
    label = list()
    target = list()
    for ann in anns:
        label.append(ann['label'])
        target.append(ann['target'])
    return label + target


# In[76]:


new_df = df[['annotators', 'post_tokens']].copy()
new_df = new_df.rename(columns={"annotators": "label", "post_tokens":"text"})

new_df.loc[:, "label"] = new_df["label"].apply(change)

new_df.loc[:, "text"] = new_df["text"].apply(lambda x : ' '.join(x))
new_df.reset_index(drop=True, inplace=True)
new_df.head()


# In[77]:


new_df['source'] = source 
new_df['language'] = 'en'

col_order = ['text', 'label', 'language', 'source'] #, 'dataset']
new_df = new_df.reindex(columns=col_order)
print(new_df.head())
new_df.to_csv(f'formatted/{source}.csv', index=False, sep='\t')


# In[79]:


new_df


# In[60]:


# cols = ['target', 'label_gold']
# new_df['label'] = df[cols].apply(
#     lambda x: ','.join(x.dropna().astype(str)),
#     axis=1
# )

new_df['source'] = source 
new_df['language'] = 'en'


# In[80]:


col_order = ['text', 'label', 'language', 'source'] #, 'dataset']
new_df = new_df.reindex(columns=col_order)
print(new_df.head())
new_df.to_csv(f'formatted/{source}.csv', index=False, sep='\t')


# In[ ]:




