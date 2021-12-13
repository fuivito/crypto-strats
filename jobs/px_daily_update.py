#!/usr/bin/env python
# coding: utf-8

# In[28]:


import krakenex
from pykrakenapi import KrakenAPI
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import csv
import os
api = krakenex.API()
kraken = KrakenAPI(api)


# In[29]:


from datetime import datetime, timedelta, date


# In[30]:

PATH = "/Users/vittorio/Google Drive/python_projects/crypto_strats/"
df = pd.read_csv(os.path.join(PATH, "data/XBTUSD_DAILY.csv"))



max_date_ts = max(df.date_unix)

print("max date in csv: ", pd.to_datetime(max_date_ts*1e3, unit='ms'))


# In[35]:


today = pd.to_datetime((datetime.now()).strftime("%Y-%m-%d"))
today_ts = datetime.timestamp(today)


# In[36]:


yesterday = pd.to_datetime((datetime.now() - timedelta(1)).strftime("%Y-%m-%d"))
yesterday_ts = datetime.timestamp(yesterday)


# ### Update logic:
#
# - I only care about yesterday's closing business day px
# - Only update data if max data in the csv is before yesterday

# In[48]:


cols = ['date','open', 'high', 'low','close','volume','date_unix']
pair = 'BTCUSD'


# In[49]:


if yesterday_ts > max_date_ts:

    to_append = kraken.get_ohlc_data(pair, interval=1440, ascending = True, since=max_date_ts)[0]

    ### Filtering out today's date - I want up to yesterday
    to_append = to_append[to_append.time < today_ts]

    assert not to_append.empty, "No new data to append"

    to_append = to_append.reset_index().rename(columns={'time':'date_unix', 'dtime':'date'})
    to_append = to_append[cols]
    to_append['date'] = to_append['date'].apply(lambda x: x.strftime("%Y-%m-%d"))

    out_df = df.append(to_append).reset_index(drop=True)
    out_df.to_csv(os.path.join(PATH, "data/XBTUSD_DAILY.csv"), index=False)

else:
    print("no new data to append")
