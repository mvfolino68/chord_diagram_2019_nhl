#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:24:07 2019

@author: michael
"""

#%%
import requests
from io import BytesIO
import pandas as pd

r = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQB7zUG_PqExM2Rc2A5KzFkuYo4LNIfwdifnd-wpjjxxEEthw1DYFuPGvd5iPMNp4NryiMknEU_PHae/pub?gid=543667841&single=true&output=csv')
data = r.content
df = pd.read_csv(BytesIO(data))


#%%
new_list_web = str(df[['team_a','team_b','SUM of G']].values.tolist())

#%%
r2 = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQB7zUG_PqExM2Rc2A5KzFkuYo4LNIfwdifnd-wpjjxxEEthw1DYFuPGvd5iPMNp4NryiMknEU_PHae/pub?gid=442685179&single=true&output=csv')
data2 = r2.content
df2 = pd.read_csv(BytesIO(data2))


#%%

colors = str(dict(zip(df2.team_a, df2.color)))

team_sort = str(df2.team_a.to_list())
