import pandas as pd

emp = pd.read_excel('employee.xlsx')

def bonus(sal):
    if sal>=200000:
        return sal*.25
    elif sal>=120000:
        return sal*.5
    elif sal>=100000:
        return sal*.75
    elif sal>=80000:
        return sal*.1
    else:
        return sal*1.25
emp['Bonus'] = emp.Salary.apply(bonus)
print(emp)