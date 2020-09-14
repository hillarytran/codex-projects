#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('fivethirtyeight')

df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv', parse_dates=['Date'])
df['Total Cases'] = df[['Confirmed', 'Recovered', 'Deaths']].sum(axis=1)
df.head()

# Worldwide Cases

worldwide_df = df.groupby(['Date']).sum()
w = worldwide_df.plot(figsize=(8,5))
w.set_xlabel('Date')
w.set_ylabel('Number of Cases WorldWide')
w.title.set_text('Worldwide COVID-19 Cases Trend')

us_df = df[df['Country']=='US'].groupby(['Date']).sum()

fig = plt.figure(figsize=(12,5))
ax = fig.add_subplot(111)

ax.plot(worldwide_df[['Total Cases']], label='Worldwide')
ax.plot(us_df[['Total Cases']], label='United States')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Total Cases')
ax.title.set_text('Worldwide vs United States Total COVID-19 Cases')

plt.legend(loc='upper left')
plt.show()

# United States Daily Cases and Deaths

us_df['Daily Confirmed'] = us_df['Confirmed'].sub(us_df['Confirmed'].shift())
us_df['Daily Deaths'] = us_df['Deaths'].sub(us_df['Deaths'].shift())

fig = plt.figure(figsize=(20,8))
ax = fig.add_subplot(111)

ax.bar(us_df['Date'], us_df['Daily Confirmed'], color='g', label='US Daily Confirmed Cases')
ax.bar(us_df['Date'], us_df['Daily Deaths'], color='r', label='US Daily Deaths')
ax.set_xlabel('Date')
ax.set_ylabel('Number of People Affected')
ax.title.set_text('United States Daily COVID-19 Cases and Deaths')

plt.legend(loc='upper left')
plt.show()

from datetime import date, timedelta
yesterday = date.today() - timedelta(days=1)
yesterday.strftime('%Y-%m-%d')

today_df = df[df['Date']==yesterday]
top_10 = today_df.sort_values(['Confirmed'], ascending=False) [:10]
top_10.loc['Rest of World'] = today_df.sort_values(['Confirmed'], ascending=False) [10:].sum()
top_10.loc['Rest of World', 'Country'] = 'Rest of World'

fig = plt.figure(figsize=(5,10))
ax = fig.add_subplot(111)

ax.pie(top_10['Confirmed'], labels=top_10['Country'], autopct='%1.1f%%')
ax.title.set_text('Hardest Hit COVID-19 Countries Worldwide')

plt.legend(loc='upper left')
plt.show()





# In[ ]:




