# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 01:51:52 2022

@author: divya
"""

import pandas as pd
df = pd.read_csv('glassdoor_jobs.csv')

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
signs = salary.apply(lambda x: x.replace('$','').replace('K',''))

min_hr = signs.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

#df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
#df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)


df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis=1)
df['age'] = df.Founded.apply(lambda x: x if x<1 else 2022-x)

df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python.value_counts()

df['R'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.R.value_counts()

df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

df_out = df.drop(['Unnamed: 0'], axis = 1)

df_out.to_csv('salary_data_cleaned.csv', index = False)

pd.read_csv('salary_data_cleaned.csv')