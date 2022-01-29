#**************************************************************************
# File 2 - playing-craps.py (Sections 4.4, 4.5)
# In this file, we will use random functions to simulate chance events (rolling a pair of six-sided dice). 
#
# Following the example provided in Section 4.4 "Rolling a Six-Sided Die 6,000,000 Times", 
# create a simulation that rolls two dice 6 million times. 
# Hint: On line 15, make face = random.randrange(1,7) + random.randrange(1,7) 
# and expand the the if block to up to 12 (6+6, the maximum value of two dice).  
# For one possible solution, see Module 3: Project Craps (One possible solution) 
#
# What fraction of the time did you roll "craps"? (add the frequencies for 2, 3, or 12)
# What fraction of the time did you "win"? (add the frequencies for 7 or 11)
# Confirm you get approximately the same as the example run shown below.
#**************************************************************************

import random

# track frequency for each roll (12=6+6, the maximum value of two dice)
frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0  
frequency7 = 0
frequency8 = 0
frequency9 = 0
frequency10 = 0
frequency11 = 0
frequency12 = 0  
rollCount = 0
        
# roll the dice 6,000,000 times
for roll in range(6_000_000):
   
    rollCount += 1
    face = random.randrange(1,7) + random.randrange(1,7)
    
    # count the occurrence for each total roll (d1+d2)
    if face == 1:
        frequency1 += 1
    elif face == 2:
        frequency2 += 1    
    elif face == 3:
        frequency3 += 1
    elif face == 4:
        frequency4 += 1
    elif face == 5:
        frequency5 += 1        
    elif face == 6:
        frequency6 += 1       
    elif face == 7:
        frequency7 += 1
    elif face == 8:
        frequency8 += 1    
    elif face == 9:
        frequency9 += 1
    elif face == 10:
        frequency10 += 1
    elif face == 11:
        frequency11 += 1        
    elif face == 12:
        frequency12 += 1      

# print results
print(f'Face{"Frequency":>13}')
print(f'{1:>4}{frequency1:>13}')
print(f'{2:>4}{frequency2:>13}')
print(f'{3:>4}{frequency3:>13}')
print(f'{4:>4}{frequency4:>13}')
print(f'{5:>4}{frequency5:>13}')
print(f'{6:>4}{frequency6:>13}')
print(f'{7:>4}{frequency7:>13}')
print(f'{8:>4}{frequency8:>13}')
print(f'{9:>4}{frequency9:>13}')
print(f'{10:>4}{frequency10:>13}')
print(f'{11:>4}{frequency11:>13}')
print(f'{12:>4}{frequency12:>13}')   
    
print()     
    
# What fraction of the time did you roll "craps"? (add the frequencies for 2, 3, or 12)
print(f'You rolled craps {frequency2 + frequency3 + frequency12} times out of {rollCount}')
print(f'{(frequency2 + frequency3 + frequency12) / rollCount * 100:.2f}%')

print()

# What fraction of the time did you "win"? (add the frequencies for 7 or 11)
print(f'You won {(frequency7 + frequency11)} times')
print(f'{(frequency7 + frequency11) / rollCount * 100:.2f}%')
