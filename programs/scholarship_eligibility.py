"""Illustrative scholarship eligibility exercise, not a real scheme."""

def scholarship_result(marks, income):
    if marks >= 90 and income <= 200000:
        return "Full scholarship (demo rule)"
    if marks >= 80 and income <= 300000:
        return "75% scholarship (demo rule)"
    if marks >= 70 and income <= 400000:
        return "50% scholarship (demo rule)"
    if marks >= 60:
        return "Merit consideration (demo rule)"
    return "Not eligible under demo rules"


def main():
    print("----- STUDENT SCHOLARSHIP ELIGIBILITY (DEMO) -----")
    name = input("Enter student name: ").strip()
    try:
        marks = float(input("Enter marks percentage: "))
        income = float(input("Enter annual family income (₹): "))
    except ValueError:
        print("Invalid input: marks and income must be numbers.")
        return
    if not 0 <= marks <= 100 or income < 0:
        print("Invalid input: marks must be 0–100 and income non-negative.")
        return
    print(f"Student: {name}")
    print(scholarship_result(marks, income))
    print("Note: These are sample rules, not official scholarship criteria.")

if __name__ == "__main__":
    main()
