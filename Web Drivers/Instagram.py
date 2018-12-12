
# coding: utf-8

# In[5]:


import time
from selenium import webdriver
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime


# In[6]:


date_today = datetime.today().strftime('%m-%d-%Y')


# d={
#     'date': [date_today, date_today, date_today],
#     'insta_name': ['mcstagner', 'capture_the_delta', 'kvphotog'],
#     'follower_count': ['6,379', '4,450', '8,621']
# }

# instagram=pd.DataFrame(data=d)


# instagram.to_csv('instagram.csv', index=False)


# In[7]:


instagram=pd.read_csv('instagram.csv')
instagram


# In[8]:


url = 'https://www.instagram.com/mcstagner'
r = requests.get(url)
soup = BeautifulSoup(r.content)
follower = soup.find('meta', {'name': 'description'})['content']
count = follower.split('Followers')[0]
#today_info=[date, insta_name, follower_count]
d={
   'date': [date_today],
   'insta_name': ['mcstagner'],
   'follower_count': [count]
}
today_info_df=pd.DataFrame(data=d)
instagram=pd.concat([today_info_df, instagram])


# In[9]:


url = 'https://www.instagram.com/capture_the_delta'
r = requests.get(url)
soup = BeautifulSoup(r.content)
follower = soup.find('meta', {'name': 'description'})['content']
count = follower.split('Followers')[0]
#today_info=[date, insta_name, follower_count]
d={
   'date': [date_today],
   'insta_name': ['capture_the_delta'],
   'follower_count': [count]
}
today_info_df=pd.DataFrame(data=d)
instagram=pd.concat([today_info_df, instagram])


# In[10]:


url = 'https://www.instagram.com/kvphotog'
r = requests.get(url)
soup = BeautifulSoup(r.content)
follower = soup.find('meta', {'name': 'description'})['content']
count = follower.split('Followers')[0]
#today_info=[date, insta_name, follower_count]
d={
   'date': [date_today],
   'insta_name': ['kvphotog'],
   'follower_count': [count]
}
today_info_df=pd.DataFrame(data=d)
instagram=pd.concat([today_info_df, instagram])


# In[12]:


instagram.to_csv('instagram.csv')

