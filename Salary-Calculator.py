#Programmer name: Trevor Hudson
#Purpose: To create a payroll program that takes data inputs and calculates net pay
#My submission of this program indicates that I have neither received nor
#given unauthorized assistance in writing this program.
#All coding is my own work.
# User input of name, hours worked, federal and state tax rates
name = str(input("Enter employee's name (first and last): "))
hours_worked = int(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))
fed_tax = float(input("Enter federal withholding rate(decimal): "))
state_tax = float(input("Enter state tax withholding rate(decimal): "))
#calculates pay before deductions
gross_pay = hourly_rate * hours_worked
print()
print()
print()
#displays the user inputed name
print(f'Employee Name: {name}')
print()
#Displays the user uinputed hours and hourly rate
print(f'Hours: {hours_worked}')
print(f'Hourly Rate: \t ${hourly_rate:>10}')
#Prints the calculation of gross pay
print(f'Gross Pay: \t ${gross_pay:>10.2f}')
print()
print("Deductions:")
#Calculates the deduction of federal tax based on user input
fedtax_total = fed_tax * gross_pay
#Calculates state tax based on user input
statetax_total = state_tax * gross_pay
#displays the federal tax deduction 
print(f'\tFederal Withholding {fed_tax:.1%}: \t ${fedtax_total:>10.2f}')
#displays the state tax deduction
print(f'\tState Withholding {state_tax:.1%}: \t ${statetax_total:>10.2f}')
#Calculates the total deduction 
total_deductions = fedtax_total + statetax_total
print(f'\tTotal Deductions: \t\t ${total_deductions:>10.2f}')
#Calculates net pay
net_pay = gross_pay - total_deductions
#displays net pay 
print(f'\nNet pay: \t\t\t\t ${net_pay:>10.2f}\n')

