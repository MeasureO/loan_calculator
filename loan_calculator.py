import math
import argparse
import sys  
    
parser = argparse.ArgumentParser(description="Process some arguments")
parser.add_argument('--type')
parser.add_argument('--principal', type=float)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=int)
args = parser.parse_args()
loan_principal = args.principal
annuity_payment = args.payment
month_number = args.periods
loan_interest = args.interest
parameters_number = 0

if loan_interest is not None:
    nominal_interest = loan_interest / 1200
if args.type is None or len(sys.argv) < 5 or args.interest is None:
    print("Incorrect parameters")
elif args.type == 'annuity':
    if args.principal is None:
        loan_principal = annuity_payment / (nominal_interest * (1 + nominal_interest) ** month_number / ((1 + nominal_interest) ** month_number - 1))
        print(f"Your loan principal = {loan_principal}!")
    if args.payment is None:
        monthly_payment = loan_principal * nominal_interest * (1 + nominal_interest) ** month_number / ((1 + nominal_interest) ** month_number - 1)
        print(f"Your monthly payment = {math.ceil(monthly_payment)}!")
        print(f"Overpayment = {math.ceil(monthly_payment) * month_number - loan_principal}!")
    if args.periods is None:
        month_number = math.ceil(math.log(annuity_payment / (annuity_payment - nominal_interest * loan_principal), 1 + nominal_interest))
        years = month_number // 12
        months = month_number % 12
        if years == 0 and months == 1:
            print(f"It will take {months} month to repay the loan")
        elif years == 0 and months > 1:
            print(f"It will take {months} months to repay the loan")
        elif years > 0 and months == 1:
            print(f"It will take {years} years and {months} month to repay this loan!")
        elif years > 0:
            print(f"It will take {years} years and {months} months to repay this loan!")
        print(f"Overpayment = {month_number * annuity_payment - loan_principal}")
elif args.type == 'diff':
    s = 0
    for i in range(1, month_number + 1):
        d = math.ceil(loan_principal / month_number + nominal_interest * (loan_principal - loan_principal * (i - 1) / month_number))
        s += d
        print(f"Month {i}: payment is {d}")
    print(f"\nOverpayment = {s - loan_principal}")
        
        



