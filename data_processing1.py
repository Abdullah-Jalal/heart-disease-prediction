import pandas as pd

data = {"name":["abdullah" , "ahmed"]
        ,"roll_no":["144" , "122"],
        "address":["karachi" , "karachi"]}
# for i in data:
#     for j in data.items():
        # print(j)
# print(data)

# df = pd.DataFrame(data)
# print(df)

df1 = pd.read_excel("employee.xlsx")

# print(df1[['Designation' , 'Age' , 'Salary']])

df1['Bonus'] = 5000


df1['Bonus1'] = [5000 if ((des == "Manager")) or ((des == "Officer")) else 4000 if des == "Engineer" else 3000 for des in  df1.Designation]

df1.drop('Bonus' , axis=1 , inplace=True)

emp = pd.read_excel("employee.xlsx")

emp['Bonus'] = [5000 if  Age>=60
       else 4000 if Age>=50
       else 3000 if Age>=40
       else 2000 if Age>=30
       else 1000 for Age in emp.Age]


emp['increment'] = [
    sal * 0.25 if sal >= 1200000 else
    sal * 0.75 if sal >= 800000 else
    sal * 0.50 if sal >= 100000 else
    sal * 1.00 if sal >= 500000 else
    sal * 1.25
    for sal in emp['Salary']
]
print(emp)