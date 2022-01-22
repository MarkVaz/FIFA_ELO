# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 19:00:06 2022

@author: MC
"""

import pandas as pd




data = {'Date':['January-21-2022'], 'Austin':[1500],'Liam':[1500],'MC':[1500],'Donovan':[1500]}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])

df.to_csv('ELO_Rankings')



