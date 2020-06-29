import math
import argparse
import sys

# set up arguments input format
parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str, help="type of calculation")
parser.add_argument("--payment", type=float, help="value of monthly payment")
parser.add_argument("--principal", type=float, help="value of principal")
parser.add_argument("--periods", type=float, help="number of periods needed to pay off the credit")
parser.add_argument("--interest", type=float, help="value of interest rate without a percent sign")

# take command-line arguments
args = parser.parse_args()

if len(sys.argv) != 5:
    # print("This script should be called with four parameters.")
    print("Incorrect parameters")
elif args.type != "annuity" and args.type != "diff":
    # print('--type must be specified to diff or annuity.')
    print("Incorrect parameters")
elif args.type == "diff" and args.payment is not None:
    # print('"diff" and payment cannot be combined.')
    print("Incorrect parameters")
elif args.interest is None:
    # print("This script cannot calculate the interest rate.")
    print("Incorrect parameters")
elif (args.payment is not None and args.payment < 0) or (args.principal is not None and args.principal < 0)\
        or (args.periods is not None and args.periods < 0) or (args.interest is not None and args.interest < 0):
    # print("Negative values are not allowed.")
    print("Incorrect parameters")
else:
    if args.type == "diff":
        nominal_interest = args.interest / (12 * 100)
        total_payments = 0

        for i in range(int(args.periods)):
            payment = math.ceil(args.principal / args.periods + nominal_interest * (args.principal - (args.principal * (i + 1 - 1) / args.periods)))
            print(f"Month {i + 1}: paid out {payment}")
            total_payments += payment

        overpayment = total_payments - args.principal
        print(f"Overpayment = {overpayment}")
    else:
        if args.payment is None:
            nominal_interest = args.interest / (12 * 100)
            payment = math.ceil(args.principal * (nominal_interest * (1 + nominal_interest) ** args.periods) / ((1 + nominal_interest) ** args.periods - 1))
            print(f"Your annuity payment = {payment}!")
            overpayment = math.ceil(payment * args.periods - args.principal)
            print(f"Overpayment = {overpayment}")
        elif args.principal is None:
            nominal_interest = args.interest / (12 * 100)
            principal = math.ceil(args.payment / ((nominal_interest * (1 + nominal_interest) ** args.periods) / ((1 + nominal_interest) ** args.periods - 1)))
            print(f"Your credit principal = {principal}!")
            overpayment = math.ceil(args.payment * args.periods - principal)
            print(f"Overpayment = {overpayment}")
        elif args.periods is None:
            nominal_interest = args.interest / (12 * 100)
            periods = math.ceil(math.log(args.payment / (args.payment - nominal_interest * args.principal), (1 + nominal_interest)))
            if periods % 12 == 0:
                print(f"You need{periods // 12} years to repay this credit!")
            else:
                print(f"You need {periods // 12} years and {periods % 12} months to repay this credit!")
            overpayment = math.ceil(args.payment * periods - args.principal)
            print(f"Overpayment = {overpayment}")
