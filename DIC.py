#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[2]:


from yahoo_fin.stock_info import *


# In[3]:


ticker = input("Enter ticker symbol: ")


# In[4]:


stock_price = get_live_price(ticker)
print("This is current stock price: ")
print(stock_price)


# In[5]:


quote = (get_quote_table(ticker))


# In[6]:


print("This is the current Dividend Yield as %")
quote["Forward Dividend & Yield"]


# In[7]:


div_yield_percentage = div_yield_percentage = float(input("Enter current dividend yield: %"))


# In[8]:


amount_invested = float(input("Enter how much money you want to invest in the company: $ "))


# In[9]:


num_of_shares = amount_invested / stock_price


# In[10]:


print("How many shares you purchased: {:.2f}".format(math.floor(num_of_shares)))


# In[11]:


current_asset_value = math.floor(num_of_shares) * stock_price


# In[12]:


print("The value of your purchase: ${:.2f}".format(current_asset_value))


# In[13]:


money_left_over = amount_invested - current_asset_value


# In[14]:


print("Money left over: ${:.2f}".format (money_left_over))


# In[15]:


div_yield_calculation = div_yield_percentage / 100


# In[16]:


annual_div = div_yield_calculation * current_asset_value
qtr_div = annual_div / 4


# In[17]:


print("Your investment pays this much per quarter: {:.2f}".format(qtr_div))


# In[18]:


print("Your investment pays this much per year: {:.2f}".format(annual_div))


# In[19]:


import pandas as pd
import yfinance as yf
import datetime
import time
import requests
import io


# In[20]:


company = ticker


# In[21]:


data = yf.download(company, '2016-01-01', '2021-01-01')


# In[22]:


data['Adj Close'].plot()


# In[23]:


#Downloading historical data from many companies 


# In[24]:


company_1 = input("Enter the ticker symbol for the company: ")
company_2 = input("Enter the ticker symbol for the company: ")
company_3 = input("Enter the ticker symbol for the company: ")
company_4 = input("Enter the ticker symbol for the company: ")
company_5 = input("Enter the ticker symbol for the company: ")


# In[25]:


ticker_list = [company_1, company_2, company_3, company_4, company_5]


# In[26]:


data =  yf.download(ticker_list,'2017-1-1')['Adj Close']


# In[27]:


data.describe()


# In[28]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[29]:


((data.pct_change()+1).cumprod()).plot(figsize=(10,7))

plt.legend()

plt.title("Returns", fontsize=16)

plt.ylabel('Cumulative Returns', fontsize=14)

plt.grid(which="major", color='k', linestyle='-.', linewidth=.05)


# In[ ]:





# In[ ]:





# In[ ]:




