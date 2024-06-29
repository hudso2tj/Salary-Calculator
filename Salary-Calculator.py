#Programmer name: Trevor Hudson
#Purpose: To create a payroll program that takes data inputs and calculates net pay
#My submission of this program indicates that I have neither received nor
#given unauthorized assistance in writing this program.
#All coding is my own work.

import sys


def main():
    #User inputs
    name = str(input("Enter employee's name: "))
    hourly_rate = float(input("Enter hourly rate: "))
    fed_tax = float(input("Enter federal withholding rate %: "))
    state_tax = float(input("Enter state tax withholding %: "))
    print("Roth or Traditional Retirement?\n\t1 - Roth\n\t2 - Traditional")
    retirement_plan = int(input("Enter your retirement plan: "))
    retirement_withholding = int(input("Enter your retirement withholding %: "))

    #Constant percentage values
    retirement_withholding = retirement_withholding / 100
    fed_tax = fed_tax / 100
    state_tax = state_tax / 100
    social_security_rate = 0.062
    medicare_tax_rate = 0.0145
    medicare_surtax_rate = 0.009

    yearly_hours_worked = 2080
    yearly_gross_pay = hourly_rate * yearly_hours_worked
    yearly_social_security = social_security_rate * yearly_gross_pay
    yearly_medicare_tax = medicare_tax_rate * yearly_gross_pay
    medicare_surtax = medicare_surtax_rate * yearly_gross_pay if yearly_gross_pay >= 200000 else 0
    yearly_fedtax_total = fed_tax * yearly_gross_pay
    yearly_statetax_total = state_tax * yearly_gross_pay
    yearly_total_deductions = 0

    #Bi-weekly salary calculations
    biweekly_hours_worked = 80
    biweekly_gross_pay = hourly_rate * biweekly_hours_worked
    biweekly_social_security = social_security_rate * biweekly_gross_pay
    biweekly_medicare_tax = medicare_tax_rate * biweekly_gross_pay
    biweekly_fedtax_total = fed_tax * biweekly_gross_pay
    biweekly_statetax_total = state_tax * biweekly_gross_pay
    biweekly_total_deductions = 0

    #Weekly salary calculations
    weekly_hours_worked = 40
    weekly_gross_pay = hourly_rate * weekly_hours_worked
    weekly_social_security = social_security_rate * weekly_gross_pay
    weekly_medicare_tax = medicare_tax_rate * weekly_gross_pay
    weekly_fedtax_total = fed_tax * weekly_gross_pay
    weekly_statetax_total = state_tax * weekly_gross_pay
    weekly_total_deductions = 0

    #Salary Breakdown output
    print("\n--------------------------------------------------------------------------------------------------------------------------")
    print("\n\n\tSalary Breakdown: \t\t\t\t   Yearly \t\tBi-Weekly \t\t   Weekly")

    print(f'\n\n\tEmployee Name: {name}\n')
    print(f'\tHourly Rate: \t\t\t\t ${hourly_rate:>15,.2f} \t ${hourly_rate:>15,.2f} \t ${hourly_rate:>15,.2f}')
    print(f'\n\tGross Pay: \t\t\t\t ${yearly_gross_pay:>15,.2f} \t ${biweekly_gross_pay:>15,.2f} \t ${weekly_gross_pay:>15,.2f}\n')
    print("\tDeductions:") 
    print(f'\t\tFederal Withholding {fed_tax:.1%}: \t ${yearly_fedtax_total:>15,.2f} \t ${biweekly_fedtax_total:>15,.2f} \t ${weekly_fedtax_total:>15,.2f}')
    print(f'\t\tState Withholding {state_tax:.1%}: \t ${yearly_statetax_total:>15,.2f} \t ${biweekly_statetax_total:>15,.2f} \t ${weekly_statetax_total:>15,.2f}')
    print(f'\t\tSocial Security 6.2%: \t\t ${yearly_social_security:>15,.2f} \t ${biweekly_social_security:>15,.2f} \t ${weekly_social_security:>15,.2f}')
    print(f'\t\tMedicare Tax 1.45%: \t\t ${yearly_medicare_tax:>15,.2f} \t ${biweekly_medicare_tax:>15,.2f} \t ${weekly_medicare_tax:>15,.2f}')
    if yearly_gross_pay >= 200000:
        print(f'\t\tMedicare Surtax 0.9%: \t\t ${medicare_surtax:>15,.2f}')

    #Determines if tax should be taken out before or after retirement and calculates accordingly
    if retirement_plan == 2:
        retirement_type = "Trad"
        yearly_retirement = yearly_gross_pay * retirement_withholding
        biweekly_retirement = biweekly_gross_pay * retirement_withholding
        weekly_retirement = weekly_gross_pay * retirement_withholding
        yearly_total_deductions = yearly_fedtax_total + yearly_statetax_total + yearly_social_security + yearly_medicare_tax + medicare_surtax + yearly_retirement
        biweekly_total_deductions = biweekly_fedtax_total + biweekly_statetax_total + biweekly_social_security + biweekly_medicare_tax + biweekly_retirement
        weekly_total_deductions = weekly_fedtax_total + weekly_statetax_total + weekly_social_security + weekly_medicare_tax +weekly_retirement
    elif retirement_plan == 1:
        retirement_type = "Roth"
        yearly_net_pay = yearly_gross_pay - (yearly_fedtax_total + yearly_statetax_total + yearly_social_security + yearly_medicare_tax + medicare_surtax)
        biweekly_net_pay = biweekly_gross_pay - (biweekly_fedtax_total + biweekly_statetax_total + biweekly_social_security + biweekly_medicare_tax)
        weekly_net_pay = weekly_gross_pay - (weekly_fedtax_total + weekly_statetax_total + weekly_social_security + weekly_medicare_tax)
        yearly_retirement = yearly_net_pay * retirement_withholding
        biweekly_retirement = biweekly_net_pay * retirement_withholding
        weekly_retirement = weekly_net_pay * retirement_withholding
        yearly_total_deductions = yearly_fedtax_total + yearly_statetax_total + yearly_social_security + yearly_medicare_tax + medicare_surtax + yearly_retirement
        biweekly_total_deductions = biweekly_fedtax_total + biweekly_statetax_total + biweekly_social_security + biweekly_medicare_tax + biweekly_retirement
        weekly_total_deductions = weekly_fedtax_total + weekly_statetax_total + weekly_social_security + weekly_medicare_tax + weekly_retirement

    yearly_net_pay = yearly_gross_pay - yearly_total_deductions
    biweekly_net_pay = biweekly_gross_pay - biweekly_total_deductions
    weekly_net_pay = weekly_gross_pay - weekly_total_deductions

    print(f'\t\t{retirement_type} Retirement {retirement_withholding:.1%} \t\t ${yearly_retirement:>15,.2f} \t ${biweekly_retirement:>15,.2f} \t ${weekly_retirement:>15,.2f}')
    print(f'\n\tTotal Deductions: \t\t\t ${yearly_total_deductions:15,.2f} \t ${biweekly_total_deductions:>15,.2f} \t ${weekly_total_deductions:>15,.2f}')
    print(f'\n\tNet pay: \t\t\t\t ${yearly_net_pay:>15,.2f} \t ${biweekly_net_pay:>15,.2f} \t ${weekly_net_pay:>15,.2f}\n')
    print("\n--------------------------------------------------------------------------------------------------------------------------")


main()
