''''
You have just purchased a stereo system that cost $1000 on 
the following credit plan: no down payment, an interest rate of 18% per year 
(and hence 1.5% per month), and monthly payments of $50. The monthly payment of 
$50 is used to pay the interest, and whatever is left is used to pay part of 
the remaining debt. Hence, the first month you pay 1.5% of $1000 in interest. 
That is $15 in interest. The remaining $35 is deducted from your debt, which 
leaves you with a debt of $965.00. The next month you pay interest of 1.5% of 
$965.00, which is $14.48. Hence, you can deduct $35.52 (which is $50–$14.48) 
from the amount you owe. Write a program that will tell you how many months it 
will take you to pay off the loan, as well as the total amount of interest paid 
over the life of the loan. Use a loop to calculate the amount of interest and 
the size of the debt after each month. (Your final program need not output the 
monthly amount of interest paid and remaining debt, but you may want to write a 
preliminary version of the program that does output these values.) Use a 
variable to count the number of loop iterations and hence the number of months 
until the debt is zero. You may want to use other variables as well. The last 
payment may be less than $50 if the debt is small, but do not forget the 
interest. If you owe $50, then your monthly payment of $50 will not pay off 
your debt, although it will come close. One month’s interest on $50 is only 
75 cents.
'''''

# VARIABLES
# initialize the Principal Balance to $1000
stereoSystemPrincipalBalance = 1000

# create variables for the monthly interest rate and total payment
interestRateMonthly = 0.015
monthlyTotalPayment = 50

# initialize the number of months to pay off the loan and the total amount of
# interest paid to 0
months = 0
totalInterestPaid = 0 

# this while loop calculates how many months it will take to pay off the balance
# of the stereo and how much interest will have been paid in total after the
# last payment
while stereoSystemPrincipalBalance > 0:
    # split up the total payment into 2 parts: interest and principal
    # calculate the monthly interest payment and principal payment
    
    # interest is paid first
    monthlyInterestPayment = stereoSystemPrincipalBalance * interestRateMonthly
    
    # based off the interest paid, the remainder of the $50 will go towards
    # the principal
    monthlyPrincipalPayment = monthlyTotalPayment - monthlyInterestPayment
    
    # each time the loop runs, add another month to the total
    months += 1
    
    # adjust the balance for the next time the loop runs
    stereoSystemPrincipalBalance -= monthlyPrincipalPayment
    
    # calculate the total interest paid
    totalInterestPaid += monthlyInterestPayment
    
# print the results
print(f"It will take {months} months to pay off the balance!")
print(f"The total amount of interest paid will be ${totalInterestPaid:.2f}.")
