#**************************************************************************
# Bonus (optional)
# Share a possible application for these skills at your work. 
# Use your new skills to create a new file named bonus.py that calculates 
# the variance and standard deviation for a new set of raw (or generated) data with at least 100 or more data points) 
# and display an additional screen shot after executing your program. 
# Make sure the output is clearly labeled and useful. 
#**************************************************************************
'''
Application:
In my workplace, the variance and standard deviation can help us to understand more about delivery rates for our female members.
By calculating the population variance and the population standard deviation on the number of deliveries per member over a time period, 
we will be able to better understand how dispersed the number of deliveries are from the average. 
'''

import random, statistics as stats

# create a list of random numbers 
randomList = []
counter = 0
for x in range(150):
    counter += 1
    if x in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        randomList.append(3)
    else:
        randomList.append(random.randrange(0, 3))

# display
print()
print(f'Number of deliveries in the past 3 years for {counter} female members aged 18+: \n {randomList}')
print()
print(f'Population Variance: {stats.pvariance(randomList):.2f}')
print(f'Population Standard Deviation: {stats.pstdev(randomList):.2f}')