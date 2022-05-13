#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
pd.options.display.max_colwidth=200


# In[2]:


import pandas as pd
#ds = '/Users/yunchaewon/gesis/datasets/CONAN/CONAN/CONAN.csv'
ds = '/Users/yunchaewon/gesis/datasets/Hatemoji/HatemojiBuild/validation.csv'
df = pd.read_csv(ds) #, lineterminator='\n')
source = 'kirk2021validation'


# In[3]:


df


# In[4]:


new_df = df[['text']].copy()

new_df.loc[:, "text"] = new_df["text"].apply(lambda x : x.replace('\n', '\\n'))
new_df


# In[5]:


cols = ['target', 'label_gold']
new_df['label'] = df[cols].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

new_df['source'] = source 
new_df['language'] = 'en'


# In[6]:


new_df


# In[7]:


col_order = ['text', 'label', 'language', 'source'] #, 'dataset']
new_df = new_df.reindex(columns=col_order)
print(new_df.head())
new_df.to_csv(f'formatted/{source}.csv', index=False, sep='\t')


# In[ ]:




