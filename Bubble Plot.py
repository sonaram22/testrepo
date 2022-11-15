#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from bubbly.bubbly import bubbleplot
from plotly.offline import init_notebook_mode, iplot


# In[3]:


gapminder_indicators=pd.read_csv('gapminder_full.csv')


# In[4]:


gapminder_indicators.head()


# In[6]:


figure=bubbleplot(dataset=gapminder_indicators, x_column='gdp_cap', y_column='life_exp',
                  bubble_column='country', time_column='year', color_column='continent',
                  x_title="GDP Per Captiva", y_title="Life Expectancy", title="Gapminder Global Indicators",
                  x_logscale=True, scale_bubble=3, height=650)
iplot(figure,config={'scrollzoom': True})


# In[ ]:




