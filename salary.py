
def getGrossPay(annual_salary, no_of_pay_periods):
    return float(annual_salary/no_of_pay_periods)
 
# driver code
 
 
# annual_salary in lakhs
annual_salary = 12
no_of_pay_periods = 12
pay = getGrossPay(annual_salary, no_of_pay_periods)
 
print(f"Total gross pay: Rs.{pay:.2f} lakhs ")
