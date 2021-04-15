#!/usr/bin/env python
# coding: utf-8

# In[1]:


from yahoo_fin.stock_info import *


# In[2]:


ticker = input("Enter ticker symbol: ")


# In[3]:


stock_price = get_live_price(ticker)
print("This is current stock price: ")
print(stock_price)


# In[4]:


quote = (get_quote_table(ticker))


# In[5]:


print("This is the current Dividend Yield as %")
quote["Forward Dividend & Yield"]


# In[6]:


import math


# In[7]:


amount_invested = float(input("Enter how much money you want to invest in the company: $ "))


# In[8]:


num_of_shares = amount_invested / stock_price


# In[9]:


print("How many shares you purchased: {:.2f}".format(math.floor(num_of_shares)))


# In[10]:


current_asset_value = math.floor(num_of_shares) * stock_price


# In[11]:


print("The value of your purchase: ${:.2f}".format(current_asset_value))


# In[12]:


money_left_over = amount_invested - current_asset_value


# In[13]:


print("Money left over: ${:.2f}".format (money_left_over))


# In[ ]:


div_yield_percentage = div_yield_percentage = float(input("Enter current dividend yield: %"))


# In[ ]:


div_yield_calculation = div_yield_percentage / 100


# In[ ]:


annual_div = div_yield_calculation * current_asset_value
qtr_div = annual_div / 4


# In[ ]:


print("Your investment pays this much per quarter: {:.2f}".format(qtr_div))


# In[ ]:


print("Your investment pays this much per year: {:.2f}".format(annual_div))


# In[ ]:


import pandas as pd
import yfinance as yf
import datetime
import time
import requests
import io


# In[ ]:


company = ticker


# In[ ]:


data = yf.download(company, '2016-01-01', '2021-01-01')


# In[ ]:


data['Adj Close'].plot()


# In[ ]:


#Downloading historical data from many companies 


# In[ ]:


company_1 = input("Enter the ticker symbol for the company: ")
company_2 = input("Enter the ticker symbol for the company: ")
company_3 = input("Enter the ticker symbol for the company: ")
company_4 = input("Enter the ticker symbol for the company: ")
company_5 = input("Enter the ticker symbol for the company: ")


# In[ ]:


ticker_list = [company_1, company_2, company_3, company_4, company_5]


# In[ ]:


data =  yf.download(ticker_list,'2017-1-1')['Adj Close']


# In[ ]:


data.describe()


# In[ ]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


((data.pct_change()+1).cumprod()).plot(figsize=(10,7))

plt.legend()

plt.title("Returns", fontsize=16)

plt.ylabel('Cumulative Returns', fontsize=14)

plt.grid(which="major", color='k', linestyle='-.', linewidth=.05)


# In[ ]:





# In[ ]:





# In[ ]:




