"""
At the top of the program include the line: import math
    - this is needed for the formulae to be used. 

Design a program that allows the user to access two 
different financial calculators.
    - investment calculator 
    - bond repayment calculator
store the input data as variables called: investment , bond

# ================== INVESTMENT ======================

if the user selects: investment
    request the user to input the following:
    - the amount they are depositing
        store the input data as a variable called: P
    - the interest rate (only the number of the interest rate, not the %)
        store the input data as a variable called: percentage_rate
    - the number of years they plan on investing
        store the input data as a variable called: t
    - request the user to input if they want "simple" or "compound" interest
        store the input data as a variable called: interest

calculate the percentage of "percentage_rate": percentage_rate / 100
    - store the calculated value as a variable called: r

create a variable called: A
    - this is to store the total amount once the interest has been applied

================== SIMPLE =============================

 if the user inputs: "simple" (for the type of interest):
        the following formula applies to variable "A": A = P * (1 + r*t)
    
    print "Your investment payout after {t} years, will be R{A} at the 'simple' interest rate of {percentage_rate}%")

================== COMPOUND =============================

    if the user inputs: "compound" (for the type of interest):
        the following formula applies to variable "A": A = P * math.pow((1+r), t)
    
    print "Your investment payout after {t} years, will be R{A} at the 'compound' interest rate of {percentage_rate}%")

=================== INVALID ENTRIES ==================

else if the user inputs any invalid entries, other than "simple" or "compound":
    print "You have made an invalid entry."

# ================= BOND REPAYMENT ====================

if the user selects: bond
    request the user to input the following:
    - the present value of the house
        store the input data as a variable called: P
    - the interest rate (only the number of the interest rate, not the %)
        store the input data as a variable called: percentage_rate
    - the number of months they plan to take to repay the bond
        store the input data as a variable called: n

calculate the percentage of "percentage_rate": percentage_rate / 100
    - store the calculated value as a variable called: r

calculate the monthly interest rate: r / 12
    store the calculated value has a variable called: i

create a variable called: repayment
    - this is to store the total monthly repayment value
the following formula applies to variable "repayment": repayment = (i * P)/(1 - (1 + i) ** (-n))

    print "Your monthly repayment will be: R{repayment}, over a period of {n} months at an interest rate of {percentage_rate}%.")

=================== INVALID ENTRIES ==================

else if the user inputs any invalid entries, other than "investment" or "bond":
    print "You have made an invalid entry."
"""
import math

# =============== OPTION SELECTION (INVESTMENT OR BOND) ================

finance_calculators = input('''
investment  - to calculate the amount of interest you'll earn on your investment
bond        - to calculate the amount you'll have to pay on a home loan

Enter either 'investment' or 'bond' from the menu above to proceed: ''').lower()

# ========================== INVESTMENT ================================

if finance_calculators == "investment":  # if 'investment' is selected
    investment = finance_calculators

# requesting following input data
    print("\nThank you! Please enter the following information: ")
# investment amount
    P = float(input("\nThe amount you want to deposit                    : ")) 
# percentage rate
    percentage_rate = float(input("The interest rate (only the number)               : ")) 
# number of years wanting to invest
    t = int(input("The number of years you are planning on investing : "))  
# the type of interest (simple or compound)
    interest = input("Do you want 'simple' or 'compound' interest?      : ").lower() 

# ========================== SIMPLE INTEREST ============================

    if interest == "simple":  # if 'simple' interest was selected
        simple = interest  # then 'simple' is assigned to 'interest'
        r = (percentage_rate / 100)  # converting the percentage number inputted to a simple form for calculation
        A = P * (1 + r*t)  # the formula for calculating simple interest
        # output print once calculation has been made
        print(f"\nYour investment payout after {t} years, will be R{round(A)} at a 'simple' interest rate of {percentage_rate}%.\n")
    
# ========================== COMPOUND INTEREST ===========================

    elif interest == "compound":  # if 'compound' interest was selected
        compound = interest  # then 'compound' is assigned to 'interest'
        r = (percentage_rate / 100)  # converting the percentage number inputted to a simple form for calculation
        A = P * math.pow((1+r), t)  # the formula for calculating compound interest
        # output print once calculation has been made
        print(f"\nYour investment payout after {t} years, will be R{round(A)} at the 'compound' interest rate of {percentage_rate}%.\n")

# =================== INVALID ENTRIES (SIMPLE OR COMPOUND)================

    else:  # if the user inputs anything other than 'simple' or 'compound'
        print(f"\nYou have made an invalid selection.\n")

# ========================== BOND REPAYMENT ==============================
else:
    if finance_calculators == "bond":  # if 'bond' is selected
        bond = finance_calculators

    # requesting following input data
        print("\nThank you! Please enter the following information: ")
    # the present value of the house
        P = float(input("\nThe present value of the house                    : "))
    # the interest that the user will be charged at
        percentage_rate = float(input("The interest rate (only the number)               : "))
    # the number of months or term the bond will be for
        n = int(input("The number of months you are planning on repaying : "))

        # ========== BOND FORMULA ===================

        r = (percentage_rate / 100)  # converting the percentage number inputted to a simple form for calculation
        i = (r / 12)  # calculating the annual interest rate
        repayment = (i * P)/(1 - (1 + i) ** (-n))  # the formula for calculating the bond repayment amount
        # output print once calculation has been made
        print(f"\nYour monthly repayment will be: R{round(repayment)}, over a period of {n} months at an interest rate of {percentage_rate}%.\n")

# ========================== INVALID ENTRIES ================================

    else:  # if the user inputs anything other than 'investment' or 'bond'
        print(f"\nYou have made an invalid selection.")

"""
This took me a day and a half to do, as I was struggling with 
the output for the simple and compound interest.
The calculation worked, but it printed incorrectly. 
I took heed of the feedback from Tselani Moeti on my Task 8 submissions
and added the .lower() function to my input statement.
This solved the problem! Thanks Tselani Moeti for your feedback, it helped me A LOT!

it was fun! Thanks, Farinaaz :)
"""
