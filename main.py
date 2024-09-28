"""
This program helps users calculate how many months it will take to pay off a 
debt and the total amount of interest paid over the loan period. 

The user inputs their name, the item they are paying off, the principal 
balance, the annual interest rate, and their monthly payment amount. The 
program then calculates and displays the total number of months 
(or years and months) required to pay off the debt, along with the total 
interest paid over that period.

The calculations account for:
1. Monthly interest charges based on the annual interest rate divided by 12.
2. The amount remaining after paying interest, which is applied to the 
principal.
3. The program stops when the remaining debt reaches zero.

It uses global variables to store user inputs and calculated results, and 
prints a final summary showing the total time and interest paid.
"""

import pydoc

# Global Variables
principalBalance = 0
interestRateMonthly = 0
monthlyTotalPayment = 0
months = 0
totalInterestPaid = 0
firstName = "" 
item = ""


def main():
    """
    The main function orchestrates the flow of the program.
    It first gathers user input through gatherInfo(), then
    calculates the loan repayment details using calculateResults(),
    and finally prints the results through printResults().
    """
    gatherInfo()
    
    calculateResults()
    
    printResults()


def gatherInfo():
    """
    This function gathers all necessary inputs from the user, including:
    - The user's first name
    - The item (debt) they need to pay off
    - The principal balance (initial loan amount)
    - The annual interest rate (converted to a monthly interest rate)
    - The user's monthly payment amount
    
    The input values are assigned to global variables for use in the
    calculation and result printing functions.
    """
    # use global variables
    global firstName, item, principalBalance, interestRateMonthly, monthlyTotalPayment
    
    # Ask the user what their name is
    firstName = input("What's your first name? ")
    
    # ask the user what item they need to pay off
    item = input("What is a debt that you need to pay off? ")

    # print starting message
    print(f"Hi, {firstName}! Let's help you pay off your {item}. I'm going to ask you 3 questions. ")

    # ask the user what their principal balance is
    principalBalance = float(input("Question 1. What is your principal balance? "))

    # ask the user what their annual interest rate is
    interestRateAnnually = float(input("Question 2. What is your annual interest rate? "))

    # if the user inputs an annual interest rate greater than 1, divide their
    # answer by 100 to convert to a decimal equivalent
    if interestRateAnnually > 1:
        interestRateAnnually = interestRateAnnually / 100

    # calculate the monthly interest rate by dividing the annual interest rate
    # by 12
    interestRateMonthly = interestRateAnnually / 12

    # ask the user what their monthly payment is
    monthlyTotalPayment = float(input("Question 3. What is your monthly payment? "))
    
    return firstName, item, principalBalance, interestRateMonthly, monthlyTotalPayment


def calculateResults():
    """
    This function calculates the number of months required to pay off
    the debt and the total amount of interest paid over the loan period.
    
    It uses a loop to simulate each month's repayment:
    - Calculates the monthly interest
    - Deducts the remaining balance by the payment amount minus the interest
    - Accumulates interest payments and increments the number of months
    
    The results are stored in global variables 'months' and 'totalInterestPaid'.
    """
    # use global variables
    global principalBalance, interestRateMonthly, monthlyTotalPayment, months, totalInterestPaid
    
    # initialize the number of months to pay off the loan and the total amount of
    # interest paid to 0
    months = 0
    totalInterestPaid = 0
    
    # this while loop calculates how many months it will take to pay off the 
    # debt balance and how much interest will have been paid in total after the
    # last payment
    while principalBalance > 0:
        # split up the total payment into 2 parts: interest and principal
        # calculate the monthly interest payment and principal payment
    
        # interest is paid first
        monthlyInterestPayment = principalBalance * interestRateMonthly
    
        # based off the interest paid, the remainder of the $50 will go towards
        # the principal
        monthlyPrincipalPayment = monthlyTotalPayment - monthlyInterestPayment
    
        # each time the loop runs, add another month to the total
        months += 1
    
        # adjust the balance for the next time the loop runs
        principalBalance -= monthlyPrincipalPayment
    
        # calculate the total interest paid
        totalInterestPaid += monthlyInterestPayment

# print the results based on whether or not it will take over a year to pay
# off the loan


def printResults():
    """
    This function prints the final results to the user, showing:
    - The number of months (or years and months) needed to pay off the debt
    - The total interest paid over the loan period
    
    The results are customized based on whether the repayment period exceeds
    12 months (displayed in years and months).
    """
    if months > 12:
        years = int(months / 12)
        remainingMonths = months % 12
    # print the results
        print(f"It will take {years} years and {remainingMonths} months to pay off your {item}, {firstName}!")
        print(f"The total amount of interest paid in that time will be ${totalInterestPaid:.2f}.")
    else:
        print(f"It will take {months} months to pay off your {item}, {firstName}!")
        print(f"The total amount of interest paid in that time will be ${totalInterestPaid:.2f}.")
        

if __name__ == "__main__":

    main()
    
    pydoc.writedoc("main")





