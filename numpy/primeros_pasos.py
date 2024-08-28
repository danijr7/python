import numpy as np

#Job titles
hob_titles = np.array(['Data Analyst', 'Data Scientist', 'Data Engineer', 'Machine Learning Engineer', 'AI Engineer'])

#Base salaries
base_salaries = np.array([60000, 80000, 75000, 90000, np.nan])

#Bonus rates
bonus_rates = np.array([.05, .1, .08, .12, np.nan])

total_salaries = base_salaries * (1 + bonus_rates)
total_salaries

np.nanmean(total_salaries)