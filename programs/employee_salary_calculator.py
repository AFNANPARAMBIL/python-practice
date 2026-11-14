"""Calculate an employee's gross and net salary."""

def nonnegative_amount(label):
    while True:
        try:
            amount = float(input(f"Enter {label}: "))
            if amount >= 0:
                return amount
        except ValueError:
            pass
        print("Please enter a valid non-negative number.")


def main():
    name = input("Enter employee name: ").strip()
    employee_id = input("Enter employee ID: ").strip()
    basic_salary = nonnegative_amount("basic salary")
    hra = nonnegative_amount("HRA")
    travel = nonnegative_amount("travel allowance")
    pf = nonnegative_amount("PF deduction")
    total_allowances = hra + travel
    gross_salary = basic_salary + total_allowances
    net_salary = gross_salary - pf
    print(f"\nEmployee: {name} (ID: {employee_id})")
    print(f"Basic Salary: ₹{basic_salary:.2f}")
    print(f"HRA: ₹{hra:.2f}")
    print(f"Travel Allowance: ₹{travel:.2f}")
    print(f"PF Deduction: ₹{pf:.2f}")
    print(f"Total Allowances: ₹{total_allowances:.2f}")
    print(f"Gross Salary: ₹{gross_salary:.2f}")
    print(f"Net Salary: ₹{net_salary:.2f}")
    if net_salary < 0:
        print("Warning: deductions exceed earnings.")

if __name__ == "__main__":
    main()
