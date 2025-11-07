import math# this program is to let user have an investment calculator or an repayment calculator

print("Investment - to calculate the amount of interest you'll earn on your investment.")

print("Bond - to calculate the amount you'll have to pay on a home loan.")

choice = input("Enter either 'investment' or 'bond' from the menu above to proceed:").lower()

# ask for investment detail and calculate input
if choice == "investment":
    deposit = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate as percentage, e.g. enter as 9 when 9% thus do not add the %: "))
    num_years = int(input("Enter number of years that you want to invest: "))
    type_interest = input("Enter either 'simple' or 'compound' for the interest type preferred: ")

    if type_interest == "simple":
        total_simple = deposit * (1 + interest_rate * num_years)
        print(f"The total amount of money you bill be paid for your investment with simple interest: R{total_simple:.2f} )

    elif type_interest == "compound":
        total_compound = deposit * (1 + interest rate) ** num_years
        print(f"The total amount of money you bill be paid for your investment with simple interest: R{total_compound:.2f} )
    
    else:
        print("Invalid interest type" )

# ask for bond detail and calculate input
elif choice == "bond":
    house_value = float(input("Enter the rand value of your house, e.g. 100 000: "))
    interest_bond = float(input("Enter the interest rate of the bond, e.g. 7: "))
    bond_months = int(input("Enter the number of months you plan to repay the bond: "))

    monthly_interest = (interest_bond / 100) / 12
    bond_repay = (monthly_interest * house_value) / (1 - (1 + monthly_interest) ** (- bond_months))

    print(f"Your monthly repayment amount is: R{bond_repay.2f}")

# neither investment or bond has been chosen
else: 
    print("Invalid input. Either enter 'investment' or 'bond'.")