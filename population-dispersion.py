#**************************************************************************
# File 5 - population-dispersion.py (Section 4.18)
# In this file, we will use the statistics module to calculate measures of dispersion for a population. 
# Using the data provided in 4.18 for 10 six-sided die rolls, and by calling functions in the statistics module - calculate:
#      Population variance using pvariance()
#      Population standard deviation using pstdev()
#      Confirm you get the answers provided (2.25 and 1.5, respectively).
# Read on to explore the differences between population variance & population standard deviation versus a sample variance and sample standard deviation. 
# You don't need to implement the sample calculations - just be aware of the difference for subsequent courses. 
#**************************************************************************

import statistics as stats

# 10 6-sided die rolls
dieRolls = [1, 3, 4, 2, 6, 5, 3, 4, 5, 2]

print('10 6-sided die rolls')
print(f'Rolls: {dieRolls}')
print(f'Population Variance: {stats.pvariance(dieRolls)}')
print(f'Population Standard Deviation: {stats.pstdev(dieRolls)}')

