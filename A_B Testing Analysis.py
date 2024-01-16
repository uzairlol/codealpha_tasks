# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 18:11:56 2024

@author: Moon
"""

# Import necessary libraries
import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# Load your A/B testing data
ab_data = pd.read_csv('ab_testing_data.csv')

# Assume 'group' is the column indicating group membership (A or B) and 'outcome' is the binary outcome variable
group_a_data = ab_data[ab_data['group'] == 'A']['outcome']
group_b_data = ab_data[ab_data['group'] == 'B']['outcome']

# Conduct two-sample t-test
t_statistic, p_value = ttest_ind(group_a_data, group_b_data)

# Display results
print(f'T-Statistic: {t_statistic:.2f}')
print(f'P-Value: {p_value:.4f}')

# Determine statistical significance
alpha = 0.05
if p_value < alpha:
    print('The difference between groups is statistically significant.')
else:
    print('There is no statistically significant difference between groups.')

# Calculate and display effect size
cohen_d = (np.mean(group_a_data) - np.mean(group_b_data)) / np.sqrt((np.std(group_a_data) ** 2 + np.std(group_b_data) ** 2) / 2)
print(f'Effect Size (Cohen\'s d): {cohen_d:.2f}')
