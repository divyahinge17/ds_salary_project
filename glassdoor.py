# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 18:47:45 2022

@author: divya
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/divya/OneDrive/Documents/Project/ds_salary_project/chromedriver"

df = gs.get_jobs('data scientist', 15, False, path, 15)