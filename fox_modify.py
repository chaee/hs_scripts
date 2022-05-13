#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
pd.options.display.max_colwidth=200


# In[33]:


ds= '/Users/yunchaewon/gesis/datasets/fox-news-comments/annotated-threads/all-comments.txt'
df = pd.read_csv(ds, sep='\:', index_col=False, header=None, lineterminator='\n')
source = 'gao2018'


# In[48]:


df = df.rename(columns={0: "label", 1: "text"})
df


# In[50]:


new_df = df.copy()
new_df.loc[:, "text"] = new_df["text"].apply(lambda x : x.replace('\n', '\\n'))


# In[52]:


new_df['source'] = source 
new_df['language'] = 'en'

col_order = ['text', 'label', 'language', 'source'] #, 'dataset']
new_df = new_df.reindex(columns=col_order)
print(new_df.head())
new_df.to_csv(f'formatted/{source}.csv', index=False, sep='\t')


# In[7]:


new_df = df[['text']].copy()
tox_codes = df[['tox_codes_oc', 'tox_codes_ic']].copy()
new_df = new_df.rename(columns={"hateSpeech": "text"})

new_df.loc[:, "text"] = new_df["text"].apply(lambda x : x.replace('\n', '\\n'))
new_df['label'] = tox_codes[tox_codes.columns[:]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)


# In[53]:


new_df

