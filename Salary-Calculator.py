#Programmer name: Trevor Hudson
#Purpose: To create a payroll program that takes data inputs and calculates net pay
#My submission of this program indicates that I have neither received nor
#given unauthorized assistance in writing this program.
#All coding is my own work.

import sys

def main():
    name = str(input("Enter employee's name: "))
    hourly_rate = float(input("Enter hourly rate: "))
    fed_tax = float(input("Enter federal withholding rate %: "))
    state_tax = float(input("Enter state tax withholding %: "))
    print("Roth or Traditional Retirement?\n\t1 - Roth\n\t2 - Traditional")
    retirement_plan = int(input("Enter your retirement plan: "))
    retirement_withholding = int(input("Enter your retirement withholding %: "))

    hours_worked = 2080
    retirement_withholding = retirement_withholding / 100
    fed_tax = fed_tax / 100
    state_tax = state_tax / 100
    social_security_rate = 0.062
    gross_pay = hourly_rate * hours_worked
    social_security = social_security_rate * gross_pay
    medicare_tax_rate = 0.0145
    medicare_surtax_rate = 0.009
    medicare_tax = medicare_tax_rate * gross_pay
    medicare_surtax = medicare_surtax_rate * gross_pay
    fedtax_total = fed_tax * gross_pay
    statetax_total = state_tax * gross_pay

    print("\n\n----------------- Yearly Salary Breakdown -----------------")

    print(f'\n\nEmployee Name: {name}\n')
    print(f'Hourly Rate: \t\t\t\t ${hourly_rate:>15,.2f}')
    print(f'\nGross Pay: \t\t\t\t ${gross_pay:>15,.2f}\n')
    print("Deductions:") 
    print(f'\tFederal Withholding {fed_tax:.1%}: \t ${fedtax_total:>15,.2f}')
    print(f'\tState Withholding {state_tax:.1%}: \t ${statetax_total:>15,.2f}')
    print(f'\tSocial Security 6.2%: \t\t ${social_security:>15,.2f}')
    print(f'\tMedicare Tax 1.45%: \t\t ${medicare_tax:>15,.2f}')
    if gross_pay >= 200000:
        print(f'\tMedicare Surtax 0.9%: \t\t ${medicare_surtax:>15,.2f}')
    if retirement_plan == 2:
        retirement_plan = "Trad"
        retirement = gross_pay * retirement_withholding
        if gross_pay >= 200000:
            total_deductions = fedtax_total + statetax_total + social_security + medicare_tax + medicare_surtax
        else:
            total_deductions = fedtax_total + statetax_total + social_security + medicare_tax 
        net_pay = gross_pay - total_deductions
    elif retirement_plan == 1:
        retirement_plan = "Roth"
        if gross_pay >= 200000:
            total_deductions = fedtax_total + statetax_total + social_security + medicare_tax + medicare_surtax
        else:
            total_deductions = fedtax_total + statetax_total + social_security + medicare_tax 
        net_pay = gross_pay - total_deductions
        retirement = net_pay * retirement_withholding
        total_deductions = total_deductions + retirement
        net_pay = gross_pay - total_deductions
    print(f'\t{retirement_plan} Retirement {retirement_withholding:.1%} \t\t ${retirement:>15,.2f}')
    print(f'\nTotal Deductions: \t\t\t ${total_deductions:15,.2f}')
    print(f'\nNet pay: \t\t\t\t ${net_pay:>15,.2f}\n')
    print("\n-----------------------------------------------------------")
                                
main()
    
