#**************************************************************************
# File 1 - bult-in-min-max.py (Sections 4.1, 4.2, 4.3)
# In this file, we will call functions to calculate min and max.
# Using the code and data provided in Section 4.3, calculate:
#    maximum (you can use the code provided to find the maximum of any 3 values) or call the built-in max().
#    minimum (you can call the built-in min() function which accepts any number of arguments. Could you write your own minimum() function?
#    Confirm you get the answers provided, e.g. the 
#        maximum(12, 27, 36) = max(12, 27, 36) = 36 
#        and the min(15, 9, 27, 14) = 9. 
#**************************************************************************

def maximum(value1, value2, value3):
    """Return the maximum of three values."""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

def minimum(value1, value2, value3, value4):
    """Return the minimum of three values."""
    min_value = value1
    if value2 < min_value:
        min_value = value2
    if value3 < min_value:
        min_value = value3
    if value4 < min_value:
        min_value = value4        
    return min_value

# prompt the user for input values and print the maximum
print("Enter values to test the maximum function:")
maxValue1 = int(input('Enter first integer: '))
maxValue2 = int(input('Enter second integer: '))
maxValue3 = int(input('Enter third integer: '))
print(f'The maximum value using the custom function is: {maximum(maxValue1, maxValue2, maxValue3)}')
print(f'The maximum value using built-in function is: {max(maxValue1, maxValue2, maxValue3)}')

print()

# prompt the user for input values and print the minimum
print("Enter values to test the minimum function:")
minValue1 = int(input('Enter first integer: '))
minValue2 = int(input('Enter second integer: '))
minValue3 = int(input('Enter third integer: '))
minValue4 = int(input('Enter fourth integer: '))
print(f'The minimum value using the custom function is: {minimum(minValue1, minValue2, minValue3, minValue4)}')
print(f'The minimum value using the built-in function is: {min(minValue1, minValue2, minValue3, minValue4)}')
