
def weeklyPaid(hours_worked, wage):
    if hours_worked > 40:
        return 40 * wage + (hours_worked - 40) * wage * 1.5
    else:
        return hours_worked * wage
 
 
hours_worked = 50
wage = 100
 
pay = weeklyPaid(hours_worked, wage)
 
print(f"Total gross pay: Rs.{pay:.2f} ")
