'''
Program: taxForm.py
Author: Mason Curtis

Compute a person's income tax
1. Significant constants
    tax rate
    standard deduction
    deduction per dependent
2. The inputs are:
    gross income (How much money you made)
    number of dependents
3. Computations:
    Taxable income = gross income - standard deduction - deduction for each dependent
    Income tax = is a fixed percentage of the taxable income
4. The outputs are:
    The income tax
'''

# Initialize the constants:
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.00
DEPENDENT_DEDUCTION = 1000.00

# Request the inputs:
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

# Compute the income tax:
taxableIncome = grossIncome - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * numDependents

incomeTax = taxableIncome * TAX_RATE

# Display the income tax:
print('The income tax is $' + str(incomeTax) + '.')
