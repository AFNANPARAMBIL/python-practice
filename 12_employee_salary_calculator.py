"""Calculate salary components for a sample employee tuple."""

employee = (106, "MEERA PILLAI", "SALES", "SALES MANAGER", 30000)
emp_id, name, department, designation, basic_salary = employee
print("Employee:", employee)
print("ID:", emp_id)
print("Name:", name)
print("Department:", department)
print("Designation:", designation)
print("Basic salary:", basic_salary)

da = basic_salary * 10 / 100
if basic_salary >= 30000:
    hra = basic_salary * 20 / 100
else:
    hra = basic_salary * 15 / 100
pf = basic_salary * 12 / 100
gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf
print("DA:", da)
print("HRA:", hra)
print("PF:", pf)
print("GROSS SALARY:", gross_salary)
print("NET SALARY:", net_salary)
