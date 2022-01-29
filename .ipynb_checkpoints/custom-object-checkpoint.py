#**************************************************************************
# File 4 - custom-object.py (read Sections 4.8-4.17)
# In this file, we will create a custom object with corresponding methods (object functions) 
# - see Module 3: Project Purchase Object Methods 
# Using the information provided, implement the following methods:
#     calculateTax()
#     calculateTip()
# Call the methods and verify you get the same values as the example provided.
#**************************************************************************

# python object representing a purchase for a given amount
class Purchase(object):
    def __init__(self, amount):
        self.amount = amount
        
    def calculateTax(self, taxPercent):
        return self.amount * taxPercent/100.0
    
    def calculateTip(self, tipPercent):
        return self.amount * tipPercent/100.0
    
    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount * (1 + taxPercent/100.0 + tipPercent/100.0)
    
# create purchase object given an amount
purchase = Purchase(100.0)

# set the tax and tip percentages
taxPercent = 7.5
tipPercent = 20.0

#use the object to calculate tax and tip
tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

# display some useful information
print('Tax: ', tax)
print('Tip: ', tip)
print('Total: ', purchase.calculateTotal(taxPercent, tipPercent))

